luc = "\033[1;32m"
trang = "\033[1;37m"
do = "\033[1;31m"
vang = "\033[0;93m"
hong = "\033[1;35m"
xduong = "\033[1;34m"
lam = "\033[1;36m"
red='\u001b[31;1m'
yellow='\u001b[33;1m'
green='\u001b[32;1m'
blue='\u001b[34;1m'
tim='\033[1;35m'
xanhlam='\033[1;36m'
xam='\033[1;30m'
black='\033[1;19m'
# Đánh dấu bản quyền
thanh_xau= " \033[1;97m[\033[1;31m+_+\033[1;97m] => "
thanh_dep= " \033[1;97m[\033[1;31m+_+\033[1;97m] => "
##### Cài Thư Viện #####
from pystyle import Add, Center, Anime, Colors, Colorate, Write, System
import requests, json
import os
import sys
from sys import platform
from time import sleep
from datetime import datetime
from time import strftime
from datetime import date
from datetime import datetime
from time import sleep,strftime
time=datetime.now().strftime("%H:%M:%S")
import socket
os.system("cls" if os.name == "nt" else "clear")
os.system('cls')
data_machine = []
today = date.today()
os.system('clear')
#daystime
now = datetime.now()
thu = now.strftime("%A")
ngay_hom_nay = now.strftime("%d")
thang_nay = now.strftime("%m")
nam_ = now.strftime("%Y")
import os,sys
import pywifi
from requests import session
from colorama import Fore, Style
import requests, random, re
from random import randint
import requests,pystyle
from pystyle import Add, Center, Anime, Colors, Colorate, Write, System
from datetime import date
from datetime import datetime
from time import sleep
time=datetime.now().strftime("%H:%M:%S")
from pystyle import *
data_machine = []
today = date.today()
now = datetime.now()
thu = now.strftime("%A")
ngay_hom_nay = now.strftime("%d")
thang_nay = now.strftime("%m")
nam_ = now.strftime("%Y")
def check_internet_connection():
    try:
        response = requests.get("http://www.google.com", timeout=5)
        return True
    except requests.ConnectionError:
        return False

# Kiểm tra kết nối internet
if check_internet_connection():
    print(f"{luc}Vui Lòng Chờ!!!")
    sleep(0.1)
else:
    print(f"{do}Vui Lòng Kiểm Tra Kết NốI!!!")
    sys.exit()
def get_location_by_ip():
    try:
        response = requests.get("https://ipinfo.io")
        data = response.json()

        city = data.get("city")
        region = data.get("region")
        country = data.get("country")
        loc = data.get("loc").split(",")
        latitude, longitude = loc if len(loc) == 2 else (None, None)

        return city, region, country, latitude, longitude
    except Exception as e:
        print(f"Lỗi: {e}")
        return None, None, None, None, None
city, region, country, latitude, longitude = get_location_by_ip()
def get_weather():
    try:
        # Lấy thông tin vị trí từ dịch vụ ipinfo.io
        response = requests.get("https://ipinfo.io")
        data = response.json()
        location = data.get("loc").split(",")
        latitude, longitude = location
        # Lấy thông tin thời tiết từ trang web công cộng
        base_url = f"https://wttr.in/{latitude},{longitude}?format=%t"
        response = requests.get(base_url)
        weather_description = response.text.strip()
        return weather_description
    except Exception as e:
        print(f"Lỗi: {e}")
        return None
weather_description = get_weather()
System.Clear()
a = " \033[1;97m[\033[1;31m+_+\033[1;97m] => "
total = 0
may = 'mb' if platform[0:3] == 'lin' else 'pc'
def banner():
 os.system("cls" if os.name == "nt" else "clear")
 banner = f"""
\033[1;31m┌═════════════════════════════════════════════════════════════════════════════┐
\033[1;31m██████╗ ███╗  ██╗ █████╗ ███╗   ███╗      ██╗  ██╗███╗  ██╗ █████╗ ███╗   ███╗
\033[1;32m██╔══██╗████╗ ██║██╔══██╗████╗ ████║      ██║  ██║████╗ ██║██╔══██╗████╗ ████║
\033[1;33m██████╦╝██╔██╗██║███████║██╔████╔██║█████╗███████║██╔██╗██║███████║██╔████╔██║
\033[1;34m██╔══██╗██║╚████║██╔══██║██║╚██╔╝██║╚════╝██╔══██║██║╚████║██╔══██║██║╚██╔╝██║
\033[1;36m██████╦╝██║ ╚███║██║  ██║██║ ╚═╝ ██║      ██║  ██║██║ ╚███║██║  ██║██║ ╚═╝ ██║
\033[1;35m╚═════╝ ╚═╝  ╚══╝╚═╝  ╚═╝╚═╝     ╚═╝      ╚═╝  ╚═╝╚═╝  ╚══╝╚═╝  ╚═╝╚═╝     ╚═╝  
\033[1;34m┠═════════════════════════════════════════════════════════════════════════════┨
\033[1;34m ➯ Cre : \033[1;31mBảo Nam x Hoàng Nam
\033[1;34m ➯ Nhóm Zalo : \033[1;37mhttps://zalo.me/g/pdsvkf650
\033[1;34m ➯ Facebook Bảo Nam : \033[1;37mhttps://facebook.com/100093509571156
\033[1;34m ➯ Facebook Hoàng Nam : \033[1;37mhttps://facebook.com/nam.nhn131                              
\033[1;34m└═════════════════════════════════════════════════════════════════════════════┘
\033[1;34m ➯ Loại Tool: \033[1;37mTrao Đổi Sub Tiktok + Tiktok Now
\033[1;34m└═════════════════════════════════════════════════════════════════════════════┘
{do} ➩ {trang}Ngày{trang} : {vang}{ngay_hom_nay}{lam} |{trang} Tháng{trang}: {vang}{thang_nay} {lam}| {trang}Năm{trang}: {vang}{nam_}{lam} | {trang}Thời Gian: {vang}{time}
{do} ➩ {trang}Thành Phố : {vang}{city} {lam}|{trang} Khu Vực: {vang}{region} {lam}| {trang} Quốc gia: {vang}{country} {lam}| {trang} Tọa độ: {vang}{latitude}, {longitude} {lam}| {trang} Nhiệt độ: {vang}{weather_description}
"""
 for X in banner:
  sys.stdout.write(X)
  sys.stdout.flush() 
  sleep(0.00125)
# =======================[ NHẬP KEY ]=======================  
def bonam(so):
	for i in range(so):
		print(red+'────', end = '' )
	print('')
class TraoDoiSub_Api (object):
	def __init__ (self, token):
		self.token = token
	
	def main(self):
		try:
			main = requests.get('https://traodoisub.com/api/?fields=profile&access_token='+self.token).json()
			try:
				return main['data']
			except:
				False
		except:
			return False
	def run(self, user):
		try:
			run = requests.get(f'https://traodoisub.com/api/?fields=tiktok_run&id={user}&access_token={self.token}').json()
			try:
				return run['data']
			except:
				return False
		except:
			return False
	#tiktok_like, tiktok_follow
	def get_job(self, type):
		try:
			get = requests.get(f'https://traodoisub.com/api/?fields={type}&access_token={self.token}')
			return get
		except:
			return False
	
	def cache(self, id, type):
#TIKTOK_LIKE_CACHE, TIKTOK_FOLLOW_CACHE
		try:
			cache = requests.get(f'https://traodoisub.com/api/coin/?type={type}&id={id}&access_token={self.token}').json()
			try:
				cache['cache']
				return True
			except:
				return False
		except:
			return False

	def nhan_xu(self, id, type):
		try:
			nhan = requests.get(f'https://traodoisub.com/api/coin/?type={type}&id={id}&access_token={self.token}')
			try:
				xu = nhan.json()['data']['xu']
				msg = nhan.json()['data']['msg']
				job = nhan.json()['data']['job_success']
				xuthem = nhan.json()['data']['xu_them']
				global total
				total+=xuthem
				bonam(14)
				print(f'{trang}Nhận Thành Công {job} Nhiệm Vụ {red}| {lam}{msg} {red}| {luc}TOTAL {vang}{total} {luc}Xu {red}| {vang}{xu} ')
				bonam(14)
				if job == 0:
					return 0
			except:
				if '"code":"error","msg"' in nhan.text:
					hien = nhan.json()['msg']; print(red+hien, end = '\r'); sleep(2); print(' '*len(hien), end = '\r')
				else:
					print(red+'Nhận Xu Thất Bại !', end = '\r'); sleep(2); print('                                                       ', end = '\r')
				return False
		except:
			print(red+'Nhận Xu Thất Bại !', end = '\r'); sleep(2); print('                                                       ', end = '\r')
			return False
def delay(dl):
  try:
    for i in range(dl, -1, -1):
       print(f'{vang}[{trang}Nam~Tool{vang}][{trang}'+str(i)+vang+']           ',end='\r')
       sleep(1)
  except:
     sleep(dl)
     print(dl,end='\r')

def chuyen(link, may):
	if may == 'mb':
		os.system(f'xdg-open {link}')
	else:
		os.system(f'cmd /c start {link}')




#----------------------------------------------------------------------------



def main():
	dem=0
	banner()
	while True:
		if os.path.exists('configtds.txt'):
			with open('configtds.txt', 'r') as f:
				token = f.read()
			tds = TraoDoiSub_Api(token)
			data = tds.main()
			try:
				print(f'{thanh_xau}{trang}Nhập {red}[{vang}1{red}] {trang}Giữ Lại Tài Khoản '+vang+ data['user'] )
				print(f'{thanh_xau}{trang}Nhập {red}[{vang}2{red}] {trang}Nhập Access_Token TDS Mới')
				chon = input(f'{thanh_xau}{trang}Nhập {lam}==>: {vang}')
				if chon == '2':
					os.remove('configtds.txt')
				elif chon == '1':
					pass
				else:
					print(red+'Lựa chọn không xác định !!!');bonam(14)
					continue 
			except:
				os.remove('configtds.txt')
		if not os.path.exists('configtds.txt'):
			token = input(f'{thanh_xau}{trang}Nhập Access_Token TDS: {vang}')
			with open('configtds.txt', 'w') as f:
				f.write(token)
		with open('configtds.txt', 'r') as f:
			token = f.read()
		tds = TraoDoiSub_Api(token)
		data = tds.main()
		try:
			xu = data['xu']
			xudie = data['xudie']
			user = data['user']
			print(lam+' Đăng Nhập Thành Công ')
			break
		except:
			print(red+'Access Token Không Hợp Lệ! Xin Thử Lại ')
			os.remove('configtds.txt')
			continue 
	bonam(14)
	
		
#while True:
	#cookie=input('Nhập Cookie Tiktok: ')
	#try:
		#headers={'Host':'www.tiktok.com','sec-ch-ua':'";Not A Brand";v="99", "Chromium";v="94"','sec-ch-ua-mobile':'?1','user-agent':'Mozilla/5.0 (Linux; Android 11; vivo 1904) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.56 Mobile Safari/537.36','sec-ch-ua-platform':'"Android"','accept':'*/*','sec-fetch-site':'same-origin','sec-fetch-mode':'cors','sec-fetch-dest':'empty','referer':'https://www.tiktok.com/foryou?is_from_webapp=v1&is_copy_url=1','accept-language':'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5','cookie':cookie}
		#info = requests.post(f'https://www.tiktok.com/passport/web/account/info/?aid=1459&app_language=vi-VN&app_name=tiktok_web&battery_info=0.79&browser_language=vi-VN&browser_name=Mozilla&browser_online=true&browser_platform=Linux%20aarch64&browser_version=5.0%20%28Linux%3B%20Android%2011%3B%20vivo%201904%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F94.0.4606.56%20Mobile%20Safari%2F537.36&channel=tiktok_web&cookie_enabled=true&device_id=7126951839819712002&device_platform=web_mobile&focus_state=true&from_page=fyp&history_len=28&is_fullscreen=false&is_page_visible=true&os=android&priority_region=VN&referer=&region=VN&screen_height=772&screen_width=360&tz_name=Asia%2FSaigon&webcast_language=vi-VN',headers=headers).json()
		#id_tikok=info['data']['user_id_str']
		#user_tiktok=info['data']['username']
		#name_tiktok=info['data']['screen_name']
		#print('User Tiktok:',user_tiktok)
		#sleep(1)
		#break
	#except:
		#print('Kiểm Tra Lại Cookie')

	banner()
	print(f'{thanh_xau}{trang}Tên Tài Khoản: {vang}{user} ')
	print(f'{thanh_xau}{trang}Xu Hiện Tại: {vang}{xu}')
	print(f'{thanh_xau}{trang}Xu Bị Phạt: {vang}{xudie} ')
	while True:
		namtool=0
		bonam(14)
		print(f'{thanh_xau}{trang}Nhập {red}[{vang}1{red}] {trang}Để Chạy Nhiệm Vụ Tim')
		print(f'{thanh_xau}{trang}Nhập {red}[{vang}2{red}] {trang}Để Chạy Nhiệm Vụ Follow')
		print(f'{thanh_xau}{trang}Nhập {red}[{vang}3{red}] {trang}Để Chạy Nhiệm Vụ Follow Tiktok Now')
		nhiem_vu=input(f'{thanh_xau}{trang}Nhập Số Để Chạy Nhiệm Vụ: {vang}')
		dl = int(input(f'{thanh_xau}{trang}Nhập Delay: {vang}'))
		while True:
			if namtool == 2:
				break
			namtool = 0
			bonam(14)
			nv_nhan=int(input(f'{thanh_xau}{trang}Sau Bao Nhiêu Nhiệm Vụ Thì Nhận Xu: {vang}'))
			if nv_nhan < 8:
				print(red+'Trên 8 Nhiệm Vụ Mới Được Nhận Tiền!')
				continue
			if nv_nhan > 15:
				print(red+'Nhận Xu Dưới 15 Nhiệm Vụ Để Tránh Lỗi')
				continue
			user_cau_hinh=input(f'{thanh_xau}{trang}Nhập User Name Tik Tok Cần Cấu Hình: {vang}')
			cau_hinh=tds.run(user_cau_hinh)
			if cau_hinh != False:
				user=cau_hinh['uniqueID']
				id_acc=cau_hinh['id']
				bonam(14)
				print(f'{trang}Đang Cấu Hình ID: {vang}{id_acc} {red}| {trang}User: {vang}{user} {red}| ')
				bonam(14)
			else:
				print(f'{red}Cấu Hinh Thất Bại User: {vang}{user_cau_hinh} ')
				continue 
			while True:
				if namtool==1 or namtool==2:break
				if '1' in nhiem_vu:
					listlike = tds.get_job('tiktok_like')
					if listlike == False:
						print(red+'Không Get Được Nhiệm Vụ Like              ', end = '\r');sleep(2); print('                                                        ', end = '\r')
					elif 'error' in listlike.text:
						if listlike.json()['error'] == 'Thao tác quá nhanh vui lòng chậm lại':
							coun = listlike.json()['countdown']
							print(f'{red}Đang Get Nhiệm Vụ Like, COUNTDOWN: {str(round(coun, 3))} ', end = '\r'); sleep(2); print('                                                       ', end = '\r')
						elif listlike.json()['error'] == 'Vui lòng ấn NHẬN TẤT CẢ rồi sau đó tiếp tục làm nhiệm vụ để tránh lỗi!':
							nhan = tds.nhan_xu('TIKTOK_LIKE_API', 'TIKTOK_LIKE') #TIKTOK_LIKE, TIKTOK_FOLLOW, TIKTOK_COMMENT
						else:
							print(red+listlike.json()['error'] , end ='\r');sleep(2); print('                                                        ', end = '\r')
					else:
						try:
							listlike = listlike.json()['data']
						except:
							print(red+'Hết Nhiệm Vụ Like                             ', end = '\r');sleep(2); print('                                                        ', end = '\r')
							continue
						if len(listlike) == 0:
							print(red+'Hết Nhiệm Vụ Like                             ', end = '\r');sleep(2); print('                                                        ', end = '\r')
						else:
							print(f'{trang}Tìm Thấy {vang}{len(listlike)} {trang}Nhiệm Vụ Like                       ', end = '\r');sleep(2); print('                                                        ', end = '\r')
							for i in listlike:
								id = i['id']
								link = i['link']
								chuyen(link, may)
								cache = tds.cache(id, 'TIKTOK_LIKE_CACHE')
								if cache != True:
									tg=datetime.now().strftime('%H:%M:%S')
									hien = f'{vang}[{red}X{vang}] {red}| {lam}{tg} {red}| {vang}TIM {red}| {trang}{id} {red}|'; print(hien, end = '\r');sleep(1); print('                                                                                        ', end = '\r')
								else:
									dem+=1
									tg=datetime.now().strftime('%H:%M:%S')
									print(f'{vang}[{trang}{dem}{vang}] {red}| {lam}{tg} {red}| {Colorate.Horizontal(Colors.yellow_to_red, "TIM")} {red}| {trang}{id} {red}|')
									delay(dl)
									if dem % nv_nhan == 0:
										nhan = tds.nhan_xu('TIKTOK_LIKE_API', 'TIKTOK_LIKE')
										if nhan == 0:
											print(red+'Nhận Xu Thất Bại Acc Tiktok Của Bạn Ổn Chứ ') 
											print(f'{thanh_xau}{trang}Nhập {red}[{vang}1{red}] {trang}Để Thay Nhiệm Vụ ')
											print(f'{thanh_xau}{trang}Nhập {red}[{vang}2{red}] {trang}Thay Acc Tiktok ')
											print(f'{thanh_xau}{trang}Nhấn {red}[{vang}Enter{red}] {trang}Để Tiếp Tục')
											chon=input(f'{thanh_xau}{trang}Nhập {red}==>: {vang}')
											if chon == '1':
												namtool=2
												break
											elif chon =='2':
												namtool = 1
												break
											bonam(14)
				if namtool==1 or namtool==2:break
				if '2' in nhiem_vu:
					listfollow = tds.get_job('tiktok_follow')
					if listfollow == False:
						print(red+'Không Get Được Nhiệm Vụ Follow              ', end = '\r');sleep(2); print('                                                        ', end = '\r')
					elif 'error' in listfollow.text:
						if listfollow.json()['error'] == 'Thao tác quá nhanh vui lòng chậm lại':
							coun = listfollow.json()['countdown']
							print(red+f'Đang Get Nhiệm Vụ Follow, COUNTDOWN: {str(round(coun, 3))} ', end = '\r'); sleep(2); print('                                                       ', end = '\r')
						elif listfollow.json()['error'] == 'Vui lòng ấn NHẬN TẤT CẢ rồi sau đó tiếp tục làm nhiệm vụ để tránh lỗi!':
							nhan = tds.nhan_xu('TIKTOK_FOLLOW_API', 'TIKTOK_FOLLOW') #TIKTOK_LIKE, TIKTOK_FOLLOW, TIKTOK_COMMENT
						else:
							print(red+listfollow.json()['error'] , end ='\r');sleep(2); print('                                                        ', end = '\r')
					else:
						try:
							listfollow = listfollow.json()['data']
						except:
							print(red+'Hết Nhiệm Vụ Follow                             ', end = '\r');sleep(2); print('                                                        ', end = '\r')
							continue
						if len(listfollow) == 0:
							print(red+'Hết Nhiệm Vụ Follow                             ', end = '\r');sleep(2); print('                                                        ', end = '\r')
						else:
							print(trang+f'Tìm Thấy {vang}{len(listfollow)} {trang}Nhiệm Vụ Follow                       ', end = '\r');sleep(2); print('                                                        ', end = '\r')
							for i in listfollow:
								id = i['id']
								link = i['link']
								chuyen(link, may)
								cache = tds.cache(id, 'TIKTOK_FOLLOW_CACHE')
								if cache != True:
									tg=datetime.now().strftime('%H:%M:%S')
									hien = f'{vang}[{red}X{vang}] {red}| {lam}{tg} {red}| {vang}FOLLOW {red}| {trang}{id} {red}|'; print(hien, end = '\r');sleep(1); print('                                                                                        ', end = '\r')
								else:
									dem+=1
									tg=datetime.now().strftime('%H:%M:%S')
									print(f'{vang}[{trang}{dem}{vang}] {red}| {lam}{tg} {red}| {Colorate.Horizontal(Colors.yellow_to_red, "FOLLOW")} {red}| {trang}{id} {red}|')
									delay(dl)
									if dem % nv_nhan == 0:
										nhan = tds.nhan_xu('TIKTOK_FOLLOW_API', 'TIKTOK_FOLLOW')
										if nhan == 0:
											print(trang+'Nhận Xu Thất Bại Acc Tiktok Của Bạn Ổn Chứ ') 
											print(f'{thanh_xau}{trang}Nhập {red}[{vang}1{red}] {trang}Để Thay Nhiệm Vụ ')
											print(f'{thanh_xau}{trang}Nhập {red}[{vang}2{red}] {trang}Thay Acc Tiktok ')
											print(f'{thanh_xau}{trang}Nhấn {red}[{vang}Enter{red}] {trang}Để Tiếp Tục')
											chon=input(f'{thanh_xau}{trang}Nhập {red}==>: {vang}')
											if chon == '1':
												namtool=2
												break
											elif chon =='2':
												namtool = 1
												break
											bonam(14)
				if namtool==1 or namtool==2:break
				if '3' in nhiem_vu:
					listfollow = tds.get_job('tiktok_follow')
					if listfollow == False:
						print(red+'Không Get Được Nhiệm Vụ Follow              ', end = '\r');sleep(2); print('                                                        ', end = '\r')
					elif 'error' in listfollow.text:
						if listfollow.json()['error'] == 'Thao tác quá nhanh vui lòng chậm lại':
							coun = listfollow.json()['countdown']
							print(f'{red}Đang Get Nhiệm Vụ Follow, COUNTDOWN: {str(round(coun, 3))} ', end = '\r'); sleep(2); print('                                                       ', end = '\r')
						elif listfollow.json()['error'] == 'Vui lòng ấn NHẬN TẤT CẢ rồi sau đó tiếp tục làm nhiệm vụ để tránh lỗi!':
							nhan = tds.nhan_xu('TIKTOK_FOLLOW_API', 'TIKTOK_FOLLOW') #TIKTOK_LIKE, TIKTOK_FOLLOW, TIKTOK_COMMENT
						else:
							print(red+listfollow.json()['error'] , end ='\r');sleep(2); print('                                                        ', end = '\r')
					else:
						try:
							listfollow = listfollow.json()['data']
						except:
							print(red+'Hết Nhiệm Vụ Follow                             ', end = '\r');sleep(2); print('                                                        ', end = '\r')
							continue
						if len(listfollow) == 0:
							print(red+'Hết Nhiệm Vụ Follow                             ', end = '\r');sleep(2); print('                                                        ', end = '\r')
						else:
							print(f'{trang}Tìm Thấy {vang}{len(listfollow)} {trang}Nhiệm Vụ Follow                       ', end = '\r');sleep(2); print('                                                        ', end = '\r')
							for i in listfollow:
								id = i['id']
								uid = id.split('_')[0] 
								link = i['link']
								que = i['uniqueID']
								if may == 'mb':
									chuyen(f'tiktoknow://user/profile?user_id={uid}', may)
								else:
									chuyen(f'https://now.tiktok.com/@{que}', may)
								cache = tds.cache(id, 'TIKTOK_FOLLOW_CACHE')
								if cache != True:
									tg=datetime.now().strftime('%H:%M:%S')
									hien = f'{vang}[{red}X{vang}] {red}| {lam}{tg} {red}| {vang}FOLLOW_TIKTOK_NOW {red}| {trang}{id} {red}|'; print(hien, end = '\r');sleep(1); print('                                                                                        ', end = '\r')
								else:
									dem+=1
									tg=datetime.now().strftime('%H:%M:%S')
									print(f'{vang}[{trang}{dem}{vang}] {red}| {lam}{tg} {red}| {Colorate.Horizontal(Colors.yellow_to_red, "FOLLOW_TIKTOK_NOW")} {red}| {trang}{id} {red}|')
									delay(dl)
									if dem % nv_nhan == 0:
										nhan = tds.nhan_xu('TIKTOK_FOLLOW_API', 'TIKTOK_FOLLOW')
										if nhan == 0:
											print(trang+'Nhận Xu Thất Bại Acc Tiktok Của Bạn Ổn Chứ ') 
											print(f'{thanh_xau}{trang}Nhập {red}[{vang}1{red}] {trang}Để Thay Nhiệm Vụ ')
											print(f'{thanh_xau}{trang}Nhập {red}[{vang}2{red}] {trang}Thay Acc Tiktok ')
											print(f'{thanh_xau}{trang}Nhấn {red}[{vang}Enter{red}] {trang}Để Tiếp Tục')
											chon=input(f'{thanh_xau}{trang}Nhập {red}==>: {vang}')
											if chon == '1':
												namtool=2
												break
											elif chon =='2':
												namtool = 1
												break
											bonam(14)
main()