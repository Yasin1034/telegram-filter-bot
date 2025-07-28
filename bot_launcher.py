import getpass
import subprocess
import os
import sys

# Şifreyi kullanıcıdan al (her seferinde değişebilir)
sifre = getpass.getpass("Şifreyi girin: ")

# Burada her seferlik şifreyi manuel belirle (örnek: 3749)
dogru_sifre = "46888"

if sifre == dogru_sifre:
    print("✅ Giriş başarılı, bot arka planda başlatılıyor...")

    # Python ve bot dosyasının yolu
    python_path = r"C:\Users\bilgiislem.stajyer\AppData\Local\Programs\Python\Python311\python.exe"
    bot_path = os.path.abspath("bot.py")

    # Arkaplanda çalıştır (CMD kapanır, bot çalışmaya devam eder)
    subprocess.Popen(
        [python_path, bot_path],
        creationflags=subprocess.DETACHED_PROCESS | subprocess.CREATE_NEW_PROCESS_GROUP
    )
    sys.exit()

else:
    print("❌ Hatalı şifre.")
    input("Çıkmak için Enter'a bas...")
