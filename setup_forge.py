import os
import subprocess

# Script ini dirancang untuk dijalankan di Google Colab
# Script ini akan menarik dan menjalankan forge neo langsung dari target repositori

def run_forge_neo():
    # Repository target untuk di-clone
    repo_url = "https://github.com/Haoming02/sd-webui-forge-classic.git"
    target_branch = "neo"
    
    print(f"Memulai setup SD-WebUI Forge branch '{target_branch}'...")
    
    # Clone repository forge asli
    if not os.path.exists("sd-webui-forge-classic"):
        subprocess.run(["git", "clone", "-b", target_branch, repo_url, "sd-webui-forge-classic"], check=True)
    
    # Pindah ke direktori hasil clone
    os.chdir("sd-webui-forge-classic")

    # Install dependensi yang hilang
    print("Menginstall dependensi yang hilang (gradio_rangeslider)...")
    subprocess.run(["pip", "install", "gradio_rangeslider"], check=True)
    
    # Jalankan launch.py dengan flag skip version check
    print("Menjalankan launch.py...")
    subprocess.run(["python3", "launch.py", "--share", "--skip-version-check"], check=True)

if __name__ == "__main__":
    run_forge_neo()
