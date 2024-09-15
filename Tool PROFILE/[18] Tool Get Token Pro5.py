# ==========================================
# TOOL BY NGUYENDUCPHAT
# TOOL GET TOKEN PRO5 PYTHON VERSION 1.0
# FB.COM/NguyenDucPhat.Copyright
# ZALO: 0396735565
# ==========================================
luc = "\033[1;32m"
trang = "\033[1;37m"
do = "\033[1;31m"
vang = "\033[0;93m"
hong = "\033[1;35m"
xduong = "\033[1;34m"
xnhac = "\033[1;36m"
# Đánh Dấu Bản Quyền
ndp_tool = do + "[" + trang + "=.=" + do + "] " + trang + "=> "
ndp = do + "[" + trang + "=.=" + do + "] " + trang + "=> "
# Config
__SHOP__ = 'ShopDucPhat.Tk'
__ZALO__ = '0396.735.565'
__ADMIN__ = 'Nguyễn Đức Phát'
__FACEBOOK__ = 'NguyenDucPhat.Copyright'
__VERSION__ = '1.0'
dem = 0
# import lib
import requests, threading
import os, sys
from time import sleep
from datetime import datetime
try:
	import requests,pystyle
except:
	print (luc + "Bạn Chưa Tải Thư Viện \n Bắt Đầu Tải ")
	os.system('pip install requests && pip install bs4 && pip install pystyle')
# ==========================[ FUNCTION ]===========================================
def echo(a):
   for i in range(len(a)):
     sys.stdout.write(a[i])
     sys.stdout.flush()
     sleep(0.001)
   print()
def banner():
    banner = f"""
\033[1;34m  █████╗ ███╗   ██╗     ██████╗ ██████╗ ██╗███╗   ██╗
\033[1;37m ██╔══██╗████╗  ██║    ██╔═══██╗██╔══██╗██║████╗  ██║
\033[1;34m ███████║██╔██╗ ██║    ██║   ██║██████╔╝██║██╔██╗ ██║
\033[1;37m ██╔══██║██║╚██╗██║    ██║   ██║██╔══██╗██║██║╚██╗██║
\033[1;34m ██║  ██║██║ ╚████║    ╚██████╔╝██║  ██║██║██║ ╚████║
\033[1;37m ╚═╝  ╚═╝╚═╝  ╚═══╝     ╚═════╝ ╚═╝  ╚═╝╚═╝╚═╝  ╚═══╝
\033[1;31m────────────────────────────────────────────────────────────
\033[1;31m[\033[1;37m=.=\033[1;31m] \033[1;37m=> \033[1;33mTOOL GET TOKEN PRO5
\033[1;31m[\033[1;37m=.=\033[1;31m] \033[1;37m=> \033[1;35mADMIN: \033[1;36mAN ORIN
\033[1;31m[\033[1;37m=.=\033[1;31m] \033[1;37m=> \033[1;36mFB: \033[1;31manorintool
\033[1;31m[\033[1;37m=.=\033[1;31m] \033[1;37m=> \033[1;32mBOX SUPPORT: \033[1;37mhttps://zalo.me/g/dpfbxq529
\033[1;31m[\033[1;37m=.=\033[1;31m] \033[1;37m=> \033[1;34mYOUTUBE: \033[1;37mhttps://youtube.com/@AnOrinTool403
\033[1;31m────────────────────────────────────────────────────────────"""
    echo(banner)
def clear():
    os.system("cls" if os.name == "nt" else "clear")
def thanh():
    print('\033[1;37m- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -')
# =================[ CLEAR + THÔNG SỐ ADMIN ]===========================
clear()
banner()
token = input(ndp_tool+luc+'Vui Lòng Nhập Token Facebook'+trang+': '+vang)
thanh()
file_save = input(ndp_tool+luc+'Vui Lòng Nhập Tên File Muốn Lưu'+trang+': '+vang)
# JSON GET TOKEN PRO5+PAGE THƯỜNG
thanh()
get_token = requests.get('https://graph.facebook.com/me/accounts?access_token='+token).json()['data']
# RUN
for get in get_token:
    time = datetime.now().strftime("%H:%M:%S")
    dem = dem+1
    tokenpro5 = get['access_token']
    namepro5 = get["name"]
    idpro5 = get['id']
    print(''+do+'['+vang+str(dem)+do+'] | '+xnhac+str(time)+do+' | '+vang+'SUCCESS '+do+' | '+trang+str(idpro5)+do+' | '+trang+str(namepro5)+do+' | '+trang+str(tokenpro5)+'')
    thanh()
    open(''+file_save+'', "a+").write(f'{idpro5}|{tokenpro5}\n')
print(ndp_tool+do+'['+vang+'SUCCESS'+do+']'+trang+': '+luc+'Đã Lưu Thành Công Vào File, '+xnhac+file_save+' ')