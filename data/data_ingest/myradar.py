#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
from time import sleep, time

import serial


class myradar:
    def __init__(self, verbose=False):
        self._config_port = None
        self._data_port = None
        self._config_serial = None
        self._data_serial = None
        self.verbose = verbose
        ports = self._find_ports()
        if len(ports) < 2:
            raise RuntimeError("No compatible radar serial ports found in /dev.")
        self._config_port = ports[0]
        self._data_port = ports[1]
        self._config_serial = serial.Serial()
        self._config_serial.port = self._config_port
        self._config_serial.baudrate = 115200
        self._config_serial.timeout = 3
        self._config_serial.open()
        self._data_serial = serial.Serial()
        self._data_serial.port = self._data_port
        self._data_serial.baudrate = 921600
        self._data_serial.timeout = 3
        self._data_serial.open()

    def _find_ports(self):
        devs = sorted(os.listdir("/dev/"))
        ttyusb = ["/dev/" + dev for dev in devs if dev.startswith("ttyUSB")]
        ttyusbserial = ["/dev/" + dev for dev in devs if dev.startswith("tty.usbserial-")]
        cuusbserial = ["/dev/" + dev for dev in devs if dev.startswith("cu.usbserial-")]
        if len(ttyusb) >= 2:
            return ttyusb
        if len(ttyusbserial) >= 2:
            return ttyusbserial
        if len(cuusbserial) >= 2:
            return cuusbserial
        return ttyusb + ttyusbserial + cuusbserial

    def close(self):
        if self._config_serial is None or self._data_serial is None:
            return
        self._config_serial.reset_input_buffer()
        self._config_serial.reset_output_buffer()
        self._data_serial.reset_input_buffer()
        self._data_serial.reset_output_buffer()
        self._config_serial.close()
        self._data_serial.close()

    def sendcmd(self, command):
        if self.verbose:
            print("\x1b[1;31m" + command + "\x1b[0m")
        self._config_serial.write((command + "\n").encode("utf-8"))
        sleep(0.01)
        self.readconfig()

    def readconfig(self):
        res = self._config_serial.read_all().decode()
        while res:
            if self.verbose:
                print("\x1b[1;34m" + res + "\x1b[0m")
            res = self._config_serial.read_all().decode()

    def flush_data(self):
        while self._data_serial.in_waiting > 0:
            self._data_serial.read_all()
            sleep(0.01)

    def is_connected(self):
        return self._config_serial is not None and self._data_serial is not None

    def check(self):
        self.sendcmd("queryDemoStatus")

    def apply_cfg(self, cfg):
        with open(cfg, "r") as handle:
            for line in handle:
                if line and line[0] != "%":
                    self._config_serial.write(line.encode("utf-8"))
                    sleep(0.01)
                    self.readconfig()

    def read_stream(self, duration_s):
        data = bytes()
        deadline = time() + duration_s
        while time() < deadline:
            if self._data_serial.in_waiting > 0:
                data += self._data_serial.read_all()
            sleep(0.01)
        while self._data_serial.in_waiting > 0:
            data += self._data_serial.read_all()
            sleep(0.01)
        return data

    def capture(self, cfg, duration_s):
        self.flush_data()
        self.apply_cfg(cfg)
        sleep(0.1)
        data = self.read_stream(duration_s)
        self.sendcmd("sensorStop")
        return data


if __name__ == "__main__":
    radar = myradar(verbose=False)
    cfgfile = "xwr68xx_AOP.cfg"
    data = radar.capture(cfgfile, 5)
    print(len(data))
    radar.close()
