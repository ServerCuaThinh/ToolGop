import sys
import os
os.system('clear')
import requests
import threading
import time
import json,requests,time
from time import strftime
from pystyle import Colorate, Colors, Write, Add, Center
__ZALO__ = '0777374145'
__ADMIN__ = 'An Orin'
__FACEBOOK__ = 'anorintool'
__VERSION__ = '1.0'
__NHV__ = '\033[1;91m[\033[1;92m●\033[1;91m]\033[1;97m ➻❥'  
def banner():
    print(f''' 
\033[1;33m██      ██╗      ████████╗ █████╗  █████╗ ██╗
\033[1;35m██╗    ╔██║      ╚══██╔══╝██╔══██╗██╔══██╗██║
\033[1;36m██║████║██║ █████╗  ██║   ██║  ██║██║  ██║██║
\033[1;37m██║    ╚██║ ╚════╝  ██║   ██║  ██║██║  ██║██║
\033[1;32m██║     ██║         ██║   ╚█████╔╝╚█████╔╝██████╗
\033[1;31m╚═╝     ╚═╝         ╚═╝    ╚════╝  ╚════╝ ╚═════╝\n
\033[1;97mTool By: \033[1;32mTrịnh Hướng            \033[1;97mPhiên Bản: \033[1;32m4.0     
\033[97m════════════════════════════════════════════════  
\033[1;97m[\033[1;91m❣\033[1;97m]\033[1;97m Tool\033[1;31m     : \033[1;97m☞ \033[1;31mTool Share Ảo\033[1;33m♔ \033[1;97m🔫
\033[1;97m[\033[1;91m❣\033[1;97m]\033[1;97m Youtube\033[1;31m  : \033[1;97m☞ \033[1;36mHướng Dev - Kiếm Tiền Online\033[1;31m♔ \033[1;97m☜
\033[1;97m[\033[1;91m❣\033[1;97m]\033[1;97m Tik Tok\033[1;31m  : \033[1;33mhttps:\033[1;32m//www.tiktok.com\033[1;31m/m@huongdev27
\033[1;97m[\033[1;91m❣\033[1;97m]\033[1;97m Zalo\033[1;31m     : \033[1;97m☞\033[1;31m0\033[1;37m3\033[1;36m6\033[1;35m2\033[1;34m1\033[1;33m6\033[1;33m6\033[1;34m8\033[1;35m6\033[1;37m3☜
\033[1;97m[\033[1;91m❣\033[1;97m]\033[1;97m Telegram\033[1;31m : \033[1;97m☞\033[1;32mhttps://t.me/+77MuosyD-yk4MGY1🔫\033[1;97m☜
\033[97m════════════════════════════════════════════════
''')
t=(Colorate.Horizontal(Colors.white_to_black,"- - - - - - - - - - - - - - - - - - - - - - - - -"))
print(t)
def clear():
    if(sys.platform.startswith('win')):
        os.system('cls')
    else:
        os.system('clear')
gome_token = []
def get_token(input_file):
    for cookie in input_file:
        header_ = {
            'authority': 'business.facebook.com',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'accept-language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
            'cache-control': 'max-age=0',
            'cookie': cookie,
            'referer': 'https://www.facebook.com/',
            'sec-ch-ua': '".Not/A)Brand";v="99", "Google Chrome";v="103", "Chromium";v="103"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Linux"',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'same-origin',
            'sec-fetch-user': '?1',
            'upgrade-insecure-requests': '1',

        }
        try:
            home_business = requests.get('https://business.facebook.com/content_management', headers=header_).text
            token = home_business.split('EAAG')[1].split('","')[0]
            cookie_token = f'{cookie}|EAAG{token}'
            gome_token.append(cookie_token)
        except:
            pass
    return gome_token

def share(tach, id_share):
    cookie = tach.split('|')[0]
    token = tach.split('|')[1]
    he = {
        'accept': '*/*',
        'accept-encoding': 'gzip, deflate',
        'connection': 'keep-alive',
        'content-length': '0',
        'cookie': cookie,
        'host': 'graph.facebook.com'
    }
    try:
        res = requests.post(f'https://graph.facebook.com/me/feed?link=https://m.facebook.com/{id_share}&published=0&access_token={token}', headers=he).json()
    except:
        pass
    
    
def main_share():
    clear()
    banner()
    input_file = open(input("\033[1;97m[\033[1;91m❣\033[1;97m] \033[1;36m✈  \033[1m\033[38;5;51mNhập tên file chứa Cookies: \033[1;35m")).read().split('\n')
    id_share = input("\033[1;97m[\033[1;91m❣\033[1;97m] \033[1;36m✈  \033[1m\033[38;5;51mNhập ID Cần Share: \033[1;35m")
    delay = int(input("\033[1;97m[\033[1;91m❣\033[1;97m] \033[1;36m✈  \033[1m\033[38;5;51mNhập Delay Share: \033[1;35m"))
    total_share = int(input("\033[1;97m[\033[1;91m❣\033[1;97m] \033[1;36m✈  \033[1m\033[38;5;51mBao Nhiêu Share Thì Dừng Tool: \033[1;35m"))
    all = get_token(input_file)
    total_live = len(all)
    print(f'\033[1;31m────────────────────────────────────────────────────────────')
    if total_live == 0:
        sys.exit()
    stt = 0
    while True:
        for tach in all:
            stt = stt + 1
            threa = threading.Thread(target=share, args=(tach, id_share))
            threa.start()
            print(f'\033[1;91m[\033[1;33m{stt}\033[1;91m]\033[1;31m ❥ \033[1;95mSHARE\033[1;31m ❥\033[1;36m THÀNH CÔNG\033[1;31m ❥ ID ❥\033[1;31m\033[1;93m {id_share} \033[1;31m❥ \n', end='\r')
            time.sleep(delay)
        if stt == total_share:
            break
    gome_token.clear()
    input('\033[38;5;245m[\033[1;32mSUCCESS\033[38;5;245m] \033[1;32mĐã Share Thành Công | Nhấn [Enter] Để Chạy Lại \033[0m\033[0m')
while True:
    try:
        main_share()
    except KeyboardInterrupt:
        print('\n\033[38;5;245m[\033[38;5;9m!\033[38;5;245m] \033[38;5;9mNhớ Đăng Ký Kênh An Orin Nhé^^\033[0m')
        sys.exit()