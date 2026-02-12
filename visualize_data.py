import json
import matplotlib.pyplot as plt
import os

def visualize_radar_data(file_path):
    print(f"Visualizing {file_path}...")
    
    if not os.path.exists(file_path):
        print(f"Error: File not found at {file_path}")
        return

    all_x = []
    all_y = []
    
    try:
        with open(file_path, 'r') as f:
            for i, line in enumerate(f):
                if i > 100: # Limit to first 100 frames for speed/clarity
                    break
                line = line.strip()
                if not line:
                    continue
                
                try:
                    data = json.loads(line)
                    x = data.get('x', [])
                    y = data.get('y', [])
                    all_x.extend(x)
                    all_y.extend(y)

                except json.JSONDecodeError:
                    pass
    except Exception as e:
        print(f"Error reading file: {e}")
        return

    if not all_x:
        print("No X/Y data found to plot.")
        return

    plt.figure(figsize=(10, 10))
    plt.scatter(all_x, all_y, s=5, alpha=0.5)
    plt.title(f"Radar Point Cloud (First {i} frames)")
    plt.xlabel("X (meters)")
    plt.ylabel("Y (meters)")
    plt.grid(True)
    plt.axis('equal') # Ensure scale is equal to see spatial layout correctly
    
    output_path = 'radar_plot.png'
    plt.savefig(output_path)
    print(f"Plot saved to {output_path}")

if __name__ == "__main__":
    target_file = 'data/first.txt'
    visualize_radar_data(target_file)
