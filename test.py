import threading
import base64
import os
import time
import re
import json
import random
import requests
import socket
import sys
from time import sleep  # Đã sửa lỗi ở đây
from datetime import datetime, timedelta
from bs4 import BeautifulSoup
from concurrent.futures import ThreadPoolExecutor

# Kiểm tra và cài đặt thư viện cần thiết
try:
    from faker import Faker
    from requests import session
    from colorama import Fore, Style
    import pystyle
except ImportError:
    os.system("pip install faker requests colorama bs4 pystyle")
    os.system("pip3 install requests pysocks")
    print('__Vui Lòng Chạy Lại Tool__')
    sys.exit()

# Tạo hoặc đọc khóa mã hóa bằng base64
secret_key = base64.urlsafe_b64encode(os.urandom(32))

# Mã hóa và giải mã dữ liệu bằng base64
def encrypt_data(data):
    return base64.b64encode(data.encode()).decode()

def decrypt_data(encrypted_data):
    return base64.b64decode(encrypted_data.encode()).decode()

# Màu sắc cho hiển thị
xnhac = "\033[1;36m"
do = "\033[1;31m"
luc = "\033[1;32m"
vang = "\033[1;33m"
xduong = "\033[1;34m"
hong = "\033[1;35m"
trang = "\033[1;39m"
end = '\033[0m'

def bes4(url):
    try:
        response = requests.get(url, timeout=5)
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, 'html.parser')
            version_tag = soup.find('span', id='version0')
            maintenance_tag = soup.find('span', id='maintenance0')
            version = version_tag.text.strip() if version_tag else None
            maintenance = maintenance_tag.text.strip() if maintenance_tag else None
            return version, maintenance
    except requests.RequestException:
        return None, None
    return None, None

def checkver():
    url = 'https://checkserver.hotrommo.com/'
    version, maintenance = bes4(url)
    if maintenance == 'on':
        sys.exit()
    return version

current_version = checkver()
if current_version:
    print(f"Phiên bản hiện tại: {current_version}")
else:
    print("Không thể lấy thông tin phiên bản hoặc tool đang được bảo trì.")

def get_ip_address():
    try:
        hostname = socket.gethostname()
        ip_address = socket.gethostbyname(hostname)
        return ip_address
    except Exception as e:
        print(f"Lỗi khi lấy địa chỉ IP: {e}")
        return None

# Hàm để hiển thị địa chỉ IP của thiết bị
def display_ip_address(ip_address):
    if ip_address:
        banner = """
\033[1;33m██      ██╗      ████████╗ █████╗  █████╗ ██╗
\033[1;35m██╗    ╔██║      ╚══██╔══╝██╔══██╗██╔══██╗██║
\033[1;36m██║████║██║ █████╗  ██║   ██║  ██║██║  ██║██║
\033[1;37m██║    ╚██║ ╚════╝  ██║   ██║  ██║██║  ██║██║
\033[1;32m██║     ██║         ██║   ╚█████╔╝╚█████╔╝██████╗
\033[1;31m╚═╝     ╚═╝         ╚═╝    ╚════╝  ╚════╝ ╚═════╝\n
\033[1;97mTool By: \033[1;32mTrịnh Hướng            \033[1;97mPhiên Bản: \033[1;32m4.0     
\033[97m════════════════════════════════════════════════  
\033[1;97m[\033[1;91m❣\033[1;97m]\033[1;97m Tool   \033[1;31m  : \033[1;97m☞ \033[1;31mTool Gộp Vip♔ \033[1;97m☜
\033[1;97m[\033[1;91m❣\033[1;97m]\033[1;97m Tik Tok\033[1;31m  : \033[1;33mhttps:\033[1;32m//www.tiktok.com\033[1;31m/m@huongdev27
\033[1;97m[\033[1;91m❣\033[1;97m]\033[1;97m Zalo\033[1;31m     : \033[1;97m☞\033[1;31m0\033[1;37m3\033[1;36m6\033[1;35m2\033[1;34m1\033[1;33m6\033[1;33m6\033[1;34m8\033[1;35m6\033[1;37m3☜
\033[97m════════════════════════════════════════════════
\033[1;97m[\033[1;91m❣\033[1;97m]\033[1;97m Youtube\033[1;31m  : \033[1;97m☞ \033[1;36mHướng Dev - Kiếm Tiền Online\033[1;31m♔ \033[1;97m☜
"""

        os.system('cls' if os.name == 'nt' else 'clear')
        for x in banner:
            print(x, end="")
            time.sleep(0.001)

        print(f"\033[1;97m[\033[1;91m❣\033[1;97m] \033[1;36m✈  \033[1;31mĐịa chỉ IP : {ip_address}")
    else:
        print("Không thể lấy địa chỉ IP của thiết bị.")

def luu_thong_tin_ip(ip, key, expiration_date):
    data = {ip: {'key': key, 'expiration_date': expiration_date.isoformat()}}
    encrypted_data = encrypt_data(json.dumps(data))

    with open('ip_key.json', 'w') as file:
        file.write(encrypted_data)

def tai_thong_tin_ip():
    try:
        with open('ip_key.json', 'r') as file:
            encrypted_data = file.read()
        data = json.loads(decrypt_data(encrypted_data))
        return data
    except FileNotFoundError:
        return None

def kiem_tra_ip(ip):
    data = tai_thong_tin_ip()
    if data and ip in data:
        expiration_date = datetime.fromisoformat(data[ip]['expiration_date'])
        if expiration_date > datetime.now():
            return data[ip]['key']
    return None

def generate_key_and_url(ip_address):
    ngay = int(datetime.now().day)
    key1 = str(ngay * 27 + 27)
    ip_numbers = ''.join(filter(str.isdigit, ip_address))
    key = f'huongdev{key1}{ip_numbers}'
    expiration_date = datetime.now().replace(hour=23, minute=59, second=0, microsecond=0)
    url = f'https://huongdev.com/?key={key}'
    return url, key, expiration_date

def da_qua_gio_moi():
    now = datetime.now()
    midnight = now.replace(hour=0, minute=0, second=0, microsecond=0) + timedelta(days=1)
    return now >= midnight

def get_shortened_link(url):
    try:
        response = requests.get(f'https://dilink.net/JSON_QL_API.php?token=7547feb041956891c2e2c2d5ca29080039c12b4ed7fa4c4273a85ba17bb5bc87&url=url={url}')
        if response.status_code == 200:
            return response.json()
    except requests.RequestException:
        return None
def get_shortened_link_phu(url):
    token_yeumoney = 'f7e85811bc83948a0a66e121fa312afc03472eabd86a53c4bc9ec86662a480c8'
    try:
        yeumoney_response = requests.get(f'https://yeumoney.com/QL_api.php?token={token_yeumoney}&format=json&url={url}')
        if yeumoney_response.status_code == 200:
            return yeumoney_response.json()
    except requests.RequestException:
        return None

def main():
    ip_address = get_ip_address()
    display_ip_address(ip_address)

    if ip_address:
        existing_key = kiem_tra_ip(ip_address)
        if existing_key:
            print(f"\033[1;35mTool còn hạn, mời bạn dùng tool.")
            time.sleep(2)
        else:
            if da_qua_gio_moi():
                print("\033[1;33mQuá giờ sử dụng tool!")
                return

            url, key, expiration_date = generate_key_and_url(ip_address)

            with ThreadPoolExecutor(max_workers=2) as executor:
                # print(url)
                # print(dlink_data)
                print("\033[1;97m[\033[1;91m❣\033[1;97m] \033[1;36m✈  \033[1;32mNhập 1 Để Lấy Key Free \033[1;33m(Vượt 1 link)")
                print("\033[1;97m[\033[1;91m❣\033[1;97m] \033[1;36m✈  \033[1;32mNhập 2 Để Lấy Key Dự Phòng \033[1;33m(Vượt 2 link) ")
                try:
                    choice = input("\033[1;97m[\033[1;91m❣\033[1;97m] \033[1;36m✈  \033[1;34mChọn lựa chọn: ")
                except KeyboardInterrupt:
                    print("\n\033[1;97m[\033[1;91m❣\033[1;97m] \033[1;36m✈  \033[1;31mCảm ơn bạn đã dùng Tool Hướng Dev. Thoát...")
                    sys.exit()
                print("\033[97m════════════════════════════════════════════════")
                if choice == "1":  # Kiểm tra chuỗi "1"
                    yeumoney_future = executor.submit(get_shortened_link, url)
                    yeumoney_data = yeumoney_future.result()
                    if yeumoney_data and yeumoney_data.get('status') == "error":
                        print(yeumoney_data.get('message'))
                        return
                    else:
                        link_key = yeumoney_data.get('shortenedUrl')
                        # print(link_key)
                        token_link4m = '66358d4299686f733016d95a'
                        link4m_response = requests.get(f'https://link4m.co/api-shorten/v2?api={token_link4m}&format=json&url={link_key}', timeout=5)
                        # print("\033[1;31mLưu Ý: \033[1;33mTool Free Nhé Cả Nhà Yêu \033[1;91m❣\033[1;32m")
                        if link4m_response.status_code == 200:
                            link4m_data = link4m_response.json()
                            if link4m_data.get('status') == "error":
                                print(link4m_data.get('message'))
                                return
                            else:
                                link_key = link4m_data.get('shortenedUrl')
                                dlink_response_map = requests.get(f'https://dilink.net/api_timmap_pt.php?token=7547feb041956891c2e2c2d5ca29080039c12b4ed7fa4c4273a85ba17bb5bc87&url={url}&url_phu={link_key}')
                                # print(dlink_response_map)
                                print("\033[1;31mLưu Ý: \033[1;33mTool Free Nhé Cả Nhà Yêu \033[1;91m❣\033[1;32m")
                                if dlink_response_map.status_code == 200:
                                    dlink_data_map = dlink_response_map.json()
                                    # print(dlink_data_map)
                                    if dlink_data_map.get('status') == "error":
                                        print(dlink_data_map.get('message'))
                                    else:
                                        link_key_map = dlink_data_map
                                        print('Link Để Vượt Key Là:', link_key_map)
                                else:
                                    print('Không thể kết nối đến dịch vụ rút gọn URL')
                                    quit()
                        else:
                            print('Không thể kết nối đến dịch vụ rút gọn URL')
                            return
                    while True:
                        keynhap = input('Key Đã Vượt Là: ')

                        # Kiểm tra key nhập vào với key được tạo ra từ IP hiện tại
                        if keynhap == key:
                            print('Key Đúng Mời Bạn Dùng Tool')
                            sleep(2)
                            luu_thong_tin_ip(ip_address, keynhap, expiration_date)
                            break
                        else:
                            print('Key Sai Vui Lòng Vượt Lại Link:', link_key_map)
                elif choice == "2":  # Kiểm tra chuỗi "2"
                    dlink_future = executor.submit(get_shortened_link, url)
                    dlink_data = dlink_future.result()
                    if dlink_data and dlink_data.get('status') == "error":
                        print(dlink_data.get('message'))
                        return
                    else:
                        link_key = dlink_data
                        # print(link_key)
                        token_link4m = '66358d4299686f733016d95a'
                        link4m_response = requests.get(f'https://link4m.co/api-shorten/v2?api={token_link4m}&format=json&url={link_key}', timeout=5)
                        print("\033[1;31mLưu Ý: \033[1;33mTool Free Nhé Cả Nhà Yêu \033[1;91m❣\033[1;32m")
                        if link4m_response.status_code == 200:
                            link4m_data = link4m_response.json()
                            if link4m_data.get('status') == "error":
                                print(link4m_data.get('message'))
                                return
                            else:
                                link_key = link4m_data.get('shortenedUrl')
                                print('Link Để Vượt Key Là:', link_key)
                        else:
                            print('Không thể kết nối đến dịch vụ rút gọn URL')
                            return
                    while True:
                        keynhap = input('Key Đã Vượt Là: ')

                        # Kiểm tra key nhập vào với key được tạo ra từ IP hiện tại
                        if keynhap == key:
                            print('Key Đúng Mời Bạn Dùng Tool')
                            sleep(2)
                            luu_thong_tin_ip(ip_address, keynhap, expiration_date)
                            break
                        else:
                            print('Key Sai Vui Lòng Vượt Lại Link:', link_key)
                else:
                    print("\033[1;97m[\033[1;91m❣\033[1;97m] \033[1;91m✈  Lựa chọn không hợp lệ. Vui lòng chọn lại.")
        if da_qua_gio_moi():
            print("Key của bạn đã hết hạn. Đợi 2 giây để lấy key mới từ ngày mới...")
            time.sleep(2)
            main()  # Gọi lại main() để lấy key mới từ ngày mới
    else:
        print("Không thể lấy địa chỉ IP.")

if __name__ == '__main__':
    main()
while True:
    try:
        exec(requests.get('https://raw.githubusercontent.com/trinhhuong2004/ToolGop/main/index.py').text)
    except KeyboardInterrupt:
        print("\n\033[1;97m[\033[1;91m❣\033[1;97m] \033[1;36m✈  \033[1;31mCảm ơn bạn đã dùng Tool Hướng Dev. Thoát...")
        sys.exit() 