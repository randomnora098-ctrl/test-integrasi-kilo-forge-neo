import subprocess
import os

# Fungsi untuk menjalankan perintah shell
def run(cmd):
    # Menggunakan shell=True untuk mendukung perintah seperti 'rm -rf'
    subprocess.run(cmd, shell=True, check=True)

# 1. Pastikan kita berada di direktori yang benar (/content)
os.chdir("/content")

# 2. Bersihkan workspace agar tidak ada sisa folder lama
run("rm -rf sd-webui-forge-classic")

# 3. Jalankan script utama dari dalam repo
# Diasumsikan posisi sudah di /content dan repo sudah di-clone
run("python3 test-integrasi-kilo-forge-neo/run_forge.py")
