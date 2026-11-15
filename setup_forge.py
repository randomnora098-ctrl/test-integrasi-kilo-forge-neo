import os
import subprocess

# Mengarahkan kerja ke folder forge neo
os.chdir("/home/ryan/Documents/kilo-workspace/forge neo")

# Script ini dirancang untuk menjalankan SD-WebUI Forge (Neo branch)
# Link repo: https://github.com/Haoming02/sd-webui-forge-classic/tree/neo
# Pastikan lingkungan Google Colab memiliki dependensi yang diperlukan.

def run_forge_neo():
    print("Memulai instalasi/setup SD-WebUI Forge (Neo branch)...")
    
    # Clone repository
    if not os.path.exists("sd-webui-forge-classic"):
        subprocess.run(["git", "clone", "-b", "neo", "https://github.com/Haoming02/sd-webui-forge-classic.git", "sd-webui-forge-classic"], check=True)
    
    os.chdir("sd-webui-forge-classic")
    
    # Menjalankan launch.py (asumsi dependensi sudah terinstal atau akan ditangani oleh launch.py)
    print("Menjalankan launch.py...")
    subprocess.run(["python3", "launch.py", "--share"], check=True)

if __name__ == "__main__":
    run_forge_neo()
