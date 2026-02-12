import os
import zipfile
import sys

# Set config dir to current directory BEFORE importing kaggle to avoid permission issues
os.environ['KAGGLE_CONFIG_DIR'] = os.getcwd()

# from kaggle.api.kaggle_api_extended import KaggleApi

def download_dataset():
    print("Function download_dataset() started.", flush=True)
    
    # Load credentials from .env
    env_path = '.env'
    print(f"Loading credentials from {env_path}...", flush=True)
    
    if os.path.exists(env_path):
        with open(env_path, 'r') as f:
            for line in f:
                if 'KAGGLE_API_TOKEN' in line:
                    try:
                        parts = line.split('=')
                        if len(parts) > 1:
                            key = parts[1].strip() # Do NOT strip prefix for new tokens
                            os.environ['KAGGLE_KEY'] = key
                            print("KAGGLE_KEY found and set.", flush=True)
                    except Exception as e:
                        print(f"Error parsing .env: {e}", flush=True)
    else:
        print(".env NOT found. Expecting KAGGLE_KEY in environment.", flush=True)
    
    # Set username (hardcoded as provided by user)
    os.environ['KAGGLE_USERNAME'] = 'eloantourtelier'
    
    print("Importing KaggleApi...", flush=True)
    from kaggle.api.kaggle_api_extended import KaggleApi

    # Initialize API
    try:
        print("Authenticating with Kaggle...", flush=True)
        api = KaggleApi()
        api.authenticate()
        print("Authentication successful.", flush=True)
    except Exception as e:
        print(f"Authentication failed: {e}", flush=True)
        return

    dataset_slug = 'flw-iml/mmwave-dataset'
    download_path = './'

    print(f"Downloading dataset '{dataset_slug}'...", flush=True)
    
    try:
        api.dataset_download_files(dataset_slug, path=download_path, unzip=True)
        print("Download and extraction complete.", flush=True)
    except Exception as e:
        print(f"Download failed: {e}", flush=True)

if __name__ == "__main__":
    print("Script started.", flush=True)
    download_dataset()