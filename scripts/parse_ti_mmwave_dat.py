#!/usr/bin/env python3

from __future__ import annotations

import argparse
import json
import struct
from pathlib import Path


MAGIC_WORD = bytes((2, 1, 4, 3, 6, 5, 8, 7))
DETECTED_POINTS_TLV = 1
SIDE_INFO_TLV = 7


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("input_path")
    parser.add_argument("--json-out")
    return parser.parse_args()


def find_packet_offsets(data: bytes) -> list[int]:
    first_offset = data.find(MAGIC_WORD)
    if first_offset < 0:
        return []
    offsets = []
    offset = first_offset
    while offset + 40 <= len(data):
        if data[offset : offset + 8] != MAGIC_WORD:
            break
        total_length = struct.unpack_from("<I", data, offset + 12)[0]
        if total_length < 40 or offset + total_length > len(data):
            break
        offsets.append(offset)
        offset += total_length
    return offsets


def parse_points(payload: bytes) -> list[dict]:
    points = []
    for offset in range(0, len(payload), 16):
        x, y, z, velocity = struct.unpack_from("<4f", payload, offset)
        points.append(
            {
                "x": round(x, 6),
                "y": round(y, 6),
                "z": round(z, 6),
                "velocity": round(velocity, 6),
            }
        )
    return points


def parse_side_info(payload: bytes) -> list[dict]:
    entries = []
    for offset in range(0, len(payload), 4):
        snr, noise = struct.unpack_from("<2h", payload, offset)
        entries.append({"snr": snr, "noise": noise})
    return entries


def merge_point_features(points: list[dict], side_info: list[dict]) -> list[dict]:
    merged = []
    for index, point in enumerate(points):
        item = dict(point)
        if index < len(side_info):
            item.update(side_info[index])
        merged.append(item)
    return merged


def parse_frame(data: bytes, offset: int) -> dict:
    _, _, _, _, frame_number, _, _, num_tlvs, _ = struct.unpack_from(
        "<8s8I", data, offset
    )
    cursor = offset + 40
    points = []
    side_info = []
    for _ in range(num_tlvs):
        tlv_type, tlv_length = struct.unpack_from("<II", data, cursor)
        payload_start = cursor + 8
        payload_end = payload_start + tlv_length
        payload = data[payload_start:payload_end]
        if tlv_type == DETECTED_POINTS_TLV:
            points = parse_points(payload)
        if tlv_type == SIDE_INFO_TLV:
            side_info = parse_side_info(payload)
        cursor = payload_end
    return {
        "frame_number": frame_number,
        "points": merge_point_features(points, side_info),
    }


def parse_file(path: Path) -> list[dict]:
    return parse_data(path.read_bytes())


def parse_data(data: bytes) -> list[dict]:
    return [parse_frame(data, offset) for offset in find_packet_offsets(data)]


def main() -> None:
    args = parse_args()
    input_path = Path(args.input_path)
    json_out = Path(args.json_out) if args.json_out else input_path.with_suffix(".parsed.json")
    frames = parse_file(input_path)
    json_out.write_text(json.dumps({"frames": frames}, indent=2))
    print(json_out)


if __name__ == "__main__":
    main()
