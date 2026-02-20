import requests
import os

def download_file(url, save_path):
    r = requests.get(url)
    with open(save_path, "wb") as f:
        f.write(r.content)

if __name__ == "__main__":
    url = input("Dataset URL: ")
    folder = "downloads/"
    os.makedirs(folder, exist_ok=True)
    filename = url.split("/")[-1]
    download_file(url, os.path.join(folder, filename))
    print("Downloaded:", filename)