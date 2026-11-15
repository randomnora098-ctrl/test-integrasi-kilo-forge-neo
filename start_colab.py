# 1. Bersihkan workspace
!rm -rf sd-webui-forge-classic

# 2. Update/Clone repositori
!rm -rf test-integrasi-kilo-forge-neo
!git clone https://github.com/randomnora098-ctrl/test-integrasi-kilo-forge-neo.git

# 3. Jalankan script utama
!python3 test-integrasi-kilo-forge-neo/run_forge.py
