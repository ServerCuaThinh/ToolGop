import requests
import os,sys
import requests,json
from time import sleep
from datetime import datetime, timedelta
import base64,requests,os
#màu
xnhac = "\033[1;36m"
do = "\033[1;31m"
luc = "\033[1;32m"
vang = "\033[1;33m"
xduong = "\033[1;34m"
hong = "\033[1;35m"
trang = "\033[1;37m"
whiteb="\033[1;37m"
red="\033[0;31m"
redb="\033[1;31m"
end='\033[0m'
#đánh dấu bản quyền
ndp_tool="\033[1;31m[\033[1;37m=.=\033[1;31m] \033[1;37m=>  "
thanh = "\033[1;37m- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -"
#Config
__ZALO__ = '0777374145'
__ADMIN__ = 'An Orin'
__FACEBOOK__ = 'anorintool'
__VERSION__ = '1.0'
def banner():
 banner = f"""
\033[1;34m  █████╗ ███╗   ██╗     ██████╗ ██████╗ ██╗███╗   ██╗
\033[1;37m ██╔══██╗████╗  ██║    ██╔═══██╗██╔══██╗██║████╗  ██║
\033[1;34m ███████║██╔██╗ ██║    ██║   ██║██████╔╝██║██╔██╗ ██║
\033[1;37m ██╔══██║██║╚██╗██║    ██║   ██║██╔══██╗██║██║╚██╗██║
\033[1;34m ██║  ██║██║ ╚████║    ╚██████╔╝██║  ██║██║██║ ╚████║
\033[1;37m ╚═╝  ╚═╝╚═╝  ╚═══╝     ╚═════╝ ╚═╝  ╚═╝╚═╝╚═╝  ╚═══╝
\033[1;31m────────────────────────────────────────────────────────────
\033[1;31m[\033[1;37m=.=\033[1;31m] \033[1;37m=> \033[1;33mTOOL TẠO THẺ THANH TOÀN
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
cookies = {
    'ezosuibasgeneris-1': '769dc2f4-d5af-4e00-75ea-86599a5ea5df',
    'ezds': 'ffid%3D2%2Cw%3D360%2Ch%3D800',
    'ezohw': 'w%3D360%2Ch%3D664',
    '_pbjs_userid_consent_data': '3524755945110770',
    '__gads': 'ID=f60114b84467d081:T=1679075153:S=ALNI_MZwEjVx0ThzBphMRcd24_Hp-hQ2rA',
    '__gpi': 'UID=00000bdb02ad3d91:T=1679075153:RT=1679075153:S=ALNI_MaU54155RJxp6-MYGV6BtpXJu38rg',
    '__qca': 'P0-1158498630-1679075151265',
    '_cc_id': '6e9ae40841ab7c99e1d5ce9403691dc7',
    'cto_bundle': 'HJbiRF9pcXNJaE93bXZvbVM1M3hMVDAzcmNIMkp3Y0hmRm1WQk9oUzlmeXhkQk55aDF5YVVOR2VqMERyV0F3VlJaS1ptVXhGRTRrTFBJelhKdWtHZ3VsMXIwSjJoWkJVVkNUVXZBMDAzcWlXRUVvZ00lMkJVZElVNzNPTURqODhpQnllVkRjZllJbnp4dldzU2FpTlFjcE8lMkZYRzNBJTNEJTNE',
    'cto_bidid': 'VLbJQl9BbHBkd3dzS0pMR05KZXk2SkE3SG1SZ2YlMkJiSlZWYWlzV244aktENlg0aXc0bkI5UnN5TzdJbldLbWpjb2ZsYTBxS2hWUEVVNlNUVkFnVG45a3ozTVA3R2xvbjVCJTJCcHNaSmFRbHFWRXk4VWMlM0Q',
    'ezoadgid_232529': '-1',
    'ezoref_232529': '',
    'ezoab_232529': 'mod150',
    'ezepvv': '44',
    'ezovid_232529': '1257532229',
    'lp_232529': 'https://randommer.io/Card',
    'ezovuuid_232529': '73feb81d-5c80-4656-7eba-e4674d5d5223',
    'ezux_lpl_232529': '1680587458474|79d9f081-f19e-40bc-5e63-41342b94d069|true',
    'ezux_et_232529': '0',
    'ezux_tos_232529': '2',
    'active_template::232529': 'pub_site_mobile.1680587463',
    'ezopvc_232529': '2',
    'ezovuuidtime_232529': '1680587464',
}

headers = {
    'authority': 'randommer.io',
    'accept': '*/*',
    'accept-language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
    # 'cookie': 'ezosuibasgeneris-1=769dc2f4-d5af-4e00-75ea-86599a5ea5df; ezds=ffid%3D2%2Cw%3D360%2Ch%3D800; ezohw=w%3D360%2Ch%3D664; _pbjs_userid_consent_data=3524755945110770; __gads=ID=f60114b84467d081:T=1679075153:S=ALNI_MZwEjVx0ThzBphMRcd24_Hp-hQ2rA; __gpi=UID=00000bdb02ad3d91:T=1679075153:RT=1679075153:S=ALNI_MaU54155RJxp6-MYGV6BtpXJu38rg; __qca=P0-1158498630-1679075151265; _cc_id=6e9ae40841ab7c99e1d5ce9403691dc7; cto_bundle=HJbiRF9pcXNJaE93bXZvbVM1M3hMVDAzcmNIMkp3Y0hmRm1WQk9oUzlmeXhkQk55aDF5YVVOR2VqMERyV0F3VlJaS1ptVXhGRTRrTFBJelhKdWtHZ3VsMXIwSjJoWkJVVkNUVXZBMDAzcWlXRUVvZ00lMkJVZElVNzNPTURqODhpQnllVkRjZllJbnp4dldzU2FpTlFjcE8lMkZYRzNBJTNEJTNE; cto_bidid=VLbJQl9BbHBkd3dzS0pMR05KZXk2SkE3SG1SZ2YlMkJiSlZWYWlzV244aktENlg0aXc0bkI5UnN5TzdJbldLbWpjb2ZsYTBxS2hWUEVVNlNUVkFnVG45a3ozTVA3R2xvbjVCJTJCcHNaSmFRbHFWRXk4VWMlM0Q; ezoadgid_232529=-1; ezoref_232529=; ezoab_232529=mod150; ezepvv=44; ezovid_232529=1257532229; lp_232529=https://randommer.io/Card; ezovuuid_232529=73feb81d-5c80-4656-7eba-e4674d5d5223; ezux_lpl_232529=1680587458474|79d9f081-f19e-40bc-5e63-41342b94d069|true; ezux_et_232529=0; ezux_tos_232529=2; active_template::232529=pub_site_mobile.1680587463; ezopvc_232529=2; ezovuuidtime_232529=1680587464',
    'origin': 'https://randommer.io',
    'sec-ch-ua': '"Chromium";v="107", "Not=A?Brand";v="24"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Linux; Android 11; CPH2239) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Mobile Safari/537.36',
    'x-requested-with': 'XMLHttpRequest',
}

data = {
    'Type': 'visa',
    'X-Requested-With': 'XMLHttpRequest',
}

link = requests.post('https://randommer.io/Card', cookies=cookies, headers=headers, data=data).json()
the = link['type']
ngay = link['date']
ten = link['fullName']
id = link['cardNumber']
phantram = link['pin']
print("\033[1;31m[\033[1;37m=.=\033[1;31m] \033[1;37m=> \033[1;37mLoại Thẻ: "+the)
print("\033[1;31m[\033[1;37m=.=\033[1;31m] \033[1;37m=> \033[1;37mSử dụng đến: "+ngay)
print("\033[1;31m[\033[1;37m=.=\033[1;31m] \033[1;37m=> \033[1;37mTên chủ thẻ: "+ten)
print("\033[1;31m[\033[1;37m=.=\033[1;31m] \033[1;37m=> \033[1;37mId card: "+id)