from pystyle import Add, Center, Anime, Colors, Colorate, Write, System
from calendar import weekheader
from time import sleep
import requests
stt=0
from time import sleep
import requests
import os, sys, requests, random
import time
from random import choice, randint, shuffle
try:
  from pystyle import Center, Anime, Colors, Colorate
except:
  os.system('pip install pystyle')
def banner():
 banner = f"""
\033[1;34m  █████╗ ███╗   ██╗     ██████╗ ██████╗ ██╗███╗   ██╗
\033[1;37m ██╔══██╗████╗  ██║    ██╔═══██╗██╔══██╗██║████╗  ██║
\033[1;34m ███████║██╔██╗ ██║    ██║   ██║██████╔╝██║██╔██╗ ██║
\033[1;37m ██╔══██║██║╚██╗██║    ██║   ██║██╔══██╗██║██║╚██╗██║
\033[1;34m ██║  ██║██║ ╚████║    ╚██████╔╝██║  ██║██║██║ ╚████║
\033[1;37m ╚═╝  ╚═╝╚═╝  ╚═══╝     ╚═════╝ ╚═╝  ╚═╝╚═╝╚═╝  ╚═══╝
\033[1;31m────────────────────────────────────────────────────────────
\033[1;31m[\033[1;37m=.=\033[1;31m] \033[1;37m=> \033[1;33mTOOL AUTO SPAM SMS + CALL
\033[1;31m[\033[1;37m=.=\033[1;31m] \033[1;37m=> \033[1;35mADMIN: \033[1;36mAN ORIN
\033[1;31m[\033[1;37m=.=\033[1;31m] \033[1;37m=> \033[1;36mFB: \033[1;31manorintool
\033[1;31m[\033[1;37m=.=\033[1;31m] \033[1;37m=> \033[1;32mBOX SUPPORT: \033[1;37mhttps://zalo.me/g/dpfbxq529
\033[1;31m[\033[1;37m=.=\033[1;31m] \033[1;37m=> \033[1;34mYOUTUBE: \033[1;37mhttps://youtube.com/@AnOrinTool403
\033[1;31m────────────────────────────────────────────────────────────
"""
 for X in banner:
  sys.stdout.write(X)
  sys.stdout.flush() 
  sleep(0.00125)
# =======================[ NHẬP KEY ]=======================
os.system("cls" if os.name == "nt" else "clear")
banner()
key = input("\033[1;31m[\033[1;37m=.=\033[1;31m] \033[1;37m=> \033[1;32mNHẬP KEY: \033[1;33m")
os.system("cls" if os.name == "nt" else "clear")
banner()
phone = input("\033[1;31m[\033[1;37m=.=\033[1;31m] \033[1;37m=> \033[1;32mNHẬP SỐ CẦN SPAM: \033[1;33m")
print("\033[1;31m────────────────────────────────────────────────────────────")
print("\033[1;31m[\033[1;37m=.=\033[1;31m] \033[1;37m=> \33[1;32mĐÃ BẮT ĐẦU...")
time.sleep(2)
while True:
    stt=stt+1
    requests.get(f'https://keysiuvip.tk/spamPhone.php?key={key}&phone={phone}')
    print(f"\33[1;37m[\33[1;32m{stt}\33[1;37m] \33[1;31mSENT OTP \33[1;97m| \33[1;33mPHONE: \33[1;37m{phone} \33[1;97m| \33[1;36mSPAM \33[1;97m| STATUS: \33[1;32mThành Công \33[1;37m|")
    time.sleep(1)
    