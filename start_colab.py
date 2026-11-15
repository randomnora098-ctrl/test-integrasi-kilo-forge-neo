import subprocess
import os

# Fungsi untuk menjalankan perintah shell
def run(cmd):
    subprocess.run(cmd, shell=True, check=True)

# 1. Bersihkan workspace
run("rm -rf sd-webui-forge-classic")

# 2. Jalankan script utama
run("python3 test-integrasi-kilo-forge-neo/run_forge.py")
