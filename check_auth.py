import os
import requests
from requests.auth import HTTPBasicAuth

def check_auth():
    # Load credentials directly
    key_str = "KGAT_fc91da43e3ae0985271cd34dcb67ecf8" 
    key = key_str.strip() 
    
    usernames_to_test = ["eloantourtelier", "EloanTourtelier", "Eloantourtelier", "eloan_tourtelier"]

    for username in usernames_to_test:
        print(f"\n==========================================")
        print(f"Testing Auth for User: '{username}'")
        print(f"==========================================")
        
        endpoints = {
            # "List Datasets (Public)": "https://www.kaggle.com/api/v1/datasets/list",
            "Download Titanic": "https://www.kaggle.com/api/v1/competitions/data/download-all/titanic",
            "Download mmWave": "https://www.kaggle.com/api/v1/datasets/download/flw-iml/mmwave-dataset"
        }

        for name, url in endpoints.items():
            print(f"--- Testing: {name} ---")
            try:
                # Using stream=True to avoid downloading content, just check headers
                response = requests.get(url, auth=HTTPBasicAuth(username, key), stream=True)
                print(f"Status: {response.status_code}")
                if response.status_code == 200:
                    print("SUCCESS: Auth works for this endpoint.")
                elif response.status_code == 401:
                    print("FAILED (401): Unauthorized. Username/Key combination is WRONG.")
                elif response.status_code == 403:
                    print("FAILED (403): Forbidden. Credentials valid, but access denied (Rules/Phone/Private).")
                else:
                    print(f"FAILED ({response.status_code}): {response.reason}")
                
                response.close()
            except Exception as e:
                print(f"Error: {e}")

if __name__ == "__main__":
    check_auth()
