import json
import os

def parse_radar_data(file_path):
    print(f"Parsing {file_path}...")
    
    if not os.path.exists(file_path):
        print(f"Error: File not found at {file_path}")
        return

    frames = []
    total_objects = 0
    
    try:
        with open(file_path, 'r') as f:
            for line_num, line in enumerate(f, 1):
                line = line.strip()
                if not line:
                    continue
                
                try:
                    data = json.loads(line)
                    frames.append(data)
                    
                    # Basic validation of expected fields
                    num_obj = data.get('numObj', 0)
                    total_objects += num_obj
                    
                    # Verify lists match numObj
                    x_vals = data.get('x', [])
                    if len(x_vals) != num_obj and num_obj > 0:
                        print(f"Warning Line {line_num}: numObj is {num_obj} but x list has {len(x_vals)} items.")

                except json.JSONDecodeError as e:
                    print(f"Error decoding JSON on line {line_num}: {e}")
    except Exception as e:
        print(f"Error reading file: {e}")
        return

    print("\n--- Summary ---")
    print(f"Total Frames Parsed: {len(frames)}")
    print(f"Total Objects Detected: {total_objects}")
    if len(frames) > 0:
        avg_objs = total_objects / len(frames)
        print(f"Average Objects per Frame: {avg_objs:.2f}")
        
        print("\n--- First Frame Structure ---")
        first_frame = frames[0]
        for key, value in first_frame.items():
            if isinstance(value, list):
                print(f"  {key}: List with {len(value)} items (First item: {value[0] if value else 'Empty'})")
            else:
                print(f"  {key}: {value}")

if __name__ == "__main__":
    # Adjust path if script is not in the same dir as data
    target_file = 'data/first.txt'
    parse_radar_data(target_file)
