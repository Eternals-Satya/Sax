import os
import subprocess
import requests

GITHUB_REPO = "https://github.com/Eternals-Satya"
GISTS_URL = "https://gist.github.com/Eternals-Satya/c804656699ce47339143666224e56af6"

def list_libraries():
    print("Available libraries (from Gist):")
    response = requests.get(GISTS_URL)
    if response.status_code == 200:
        gist_content = response.text
        print(gist_content)  # Tampilkan isi Gist (atau parse jika formatnya lebih rapi)
    else:
        print("Failed to fetch library list from Gist.")

def install_library(library_name):
    repo_url = f"{GITHUB_REPO}/{library_name}.git"
    target_dir = os.path.join(os.getcwd(), library_name)

    if os.path.exists(target_dir):
        print(f"Library '{library_name}' already installed.")
        return

    try:
        print(f"Cloning {repo_url}...")
        subprocess.check_call(["git", "clone", repo_url, target_dir])
        print(f"Library '{library_name}' installed successfully.")
    except subprocess.CalledProcessError:
        print(f"Error: Failed to clone {repo_url}. Check if the library exists.")
