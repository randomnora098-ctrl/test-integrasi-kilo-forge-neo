# Menginstal dependensi
!pip install gradio==4.40.0
!pip install gradio_rangeslider

# Menjalankan script utama
import os
import subprocess

# Repository target
repo_url = "https://github.com/Haoming02/sd-webui-forge-classic.git"
target_branch = "neo"

if not os.path.exists("sd-webui-forge-classic"):
    subprocess.run(["git", "clone", "-b", target_branch, repo_url, "sd-webui-forge-classic"], check=True)

os.chdir("sd-webui-forge-classic")

# Jalankan launch.py
subprocess.run([
    "python3", "launch.py", 
    "--share", 
    "--skip-version-check", 
    "--enable-insecure-extension-access"
], check=True)
