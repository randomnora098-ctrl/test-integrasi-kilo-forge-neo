import subprocess
import os
import shutil

# Fungsi untuk menjalankan perintah shell
def run(cmd):
    subprocess.run(cmd, shell=True, check=True)

# 1. Bersihkan workspace untuk Forge (opsional, tergantung kebutuhan)
if os.path.exists("sd-webui-forge-classic"):
    shutil.rmtree("sd-webui-forge-classic")

# 2. Cek apakah folder repo ada, jika ada lakukan pull, jika tidak clone
repo_dir = "test-integrasi-kilo-forge-neo"
if os.path.exists(repo_dir):
    print("Repositori ditemukan, melakukan update...")
    subprocess.run(["git", "-C", repo_dir, "pull"], check=True)
else:
    print("Repositori tidak ditemukan, melakukan clone...")
    subprocess.run(["git", "clone", "https://github.com/randomnora098-ctrl/test-integrasi-kilo-forge-neo.git"], check=True)

# 3. Jalankan script utama
subprocess.run(["python3", "test-integrasi-kilo-forge-neo/run_forge.py"], check=True)
