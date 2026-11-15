import subprocess

# 1. Bersihkan workspace
subprocess.run(["rm", "-rf", "sd-webui-forge-classic"])

# 2. Jalankan script utama
subprocess.run(["python3", "test-integrasi-kilo-forge-neo/run_forge.py"])
