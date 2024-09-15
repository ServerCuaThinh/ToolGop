import os
import datetime
from datetime import datetime
import requests,json
import uuid
from time import sleep
van = "dz"
listjob = []
def logo():
	print ('\033[1;34m  █████╗ ███╗   ██╗     ██████╗ ██████╗ ██╗███╗   ██╗')
	print ('\033[1;37m ██╔══██╗████╗  ██║    ██╔═══██╗██╔══██╗██║████╗  ██║')
	print ('\033[1;34m ███████║██╔██╗ ██║    ██║   ██║██████╔╝██║██╔██╗ ██║')
	print ('\033[1;37m ██╔══██║██║╚██╗██║    ██║   ██║██╔══██╗██║██║╚██╗██║')
	print (' \033[1;34m██║  ██║██║ ╚████║    ╚██████╔╝██║  ██║██║██║ ╚████║')
	print ('\033[1;37m ╚═╝  ╚═╝╚═╝  ╚═══╝     ╚═════╝ ╚═╝  ╚═╝╚═╝╚═╝  ╚═══╝')
	print ('\033[1;31m────────────────────────────────────────────────────────────')
	print ('\033[1;31m[\033[1;37m=.=\033[1;31m] \033[1;37m=> \033[1;33mTOOL TDS FB ')
	print ('\033[1;31m[\033[1;37m=.=\033[1;31m] \033[1;37m=> \033[1;35mADMIN: \033[1;36mAN ORIN ')
	print ('\033[1;31m[\033[1;37m=.=\033[1;31m] \033[1;37m=> \033[1;36mFB: \033[1;31manorintool')
	print ('\033[1;31m[\033[1;37m=.=\033[1;31m] \033[1;37m=> \033[1;32mBOX SUPPORT: \033[1;37mhttps://zalo.me/g/dpfbxq529 ')
	print ('\033[1;31m[\033[1;37m=.=\033[1;31m] \033[1;37m=> \033[1;34mYOUTUBE: \033[1;37mhttps://youtube.com/@AnOrinTool403 ')
	print ('\033[1;31m────────────────────────────────────────────────────────────')

def cam_xuc(id_post,ck,loai): 
	headers = {
	'Host':'mbasic.facebook.com',
	'upgrade-insecure-requests':'1',
	'user-agent':'Mozilla/5.0 (Linux; Android 8.1.0; CPH1912 Build/O11019) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.5359.128 Mobile Safari/537.36',
	'accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
	'sec-fetch-site':'none',
	'sec-fetch-mode':'navigate',
	'sec-fetch-user':'?1',
	'sec-fetch-dest':'document',
	'cookie': ck
	}
	url = requests.get('https://www.facebook.com/'+id_post, headers=headers).url
	try : 
		home = requests.get(url, headers=headers).text
		url_type = home.split('<a href="/reactions/picker/?')[1].split('"')[0]
		is_permalink= url_type.split('is_permalink=')[1].split('&amp')[0]
		t_id= url_type.split('t_id=')[1].split('&amp')[0]
		origin_uri= url_type.split('origin_uri=')[1].split('&amp')[0]
		av= url_type.split('av=')[1].split('&amp')[0]
		refid= url_type.split('refid=')[1].split('&amp')[0]
		paipv= url_type.split('paipv=')[1].split('&amp')[0]
		eav= url_type.split('eav=')[1].split('&amp')[0]
		url_cx_1 = f'https://mbasic.facebook.com/reactions/picker/?is_permalink={is_permalink}&ft_id={t_id}&origin_uri={origin_uri}&av={av}&refid={refid}&paipv={paipv}&eav={eav}'
		get_url = requests.get(url_cx_1, headers=headers).text
		if loai == 'LIKE' :
			url_type_1 = get_url.split('<a href="/ufi/reaction/?')[1].split('"')[0]
		elif loai == 'LOVE' :
			url_type_1 = get_url.split('<a href="/ufi/reaction/?')[2].split('"')[0]
		elif loai == 'CARE' :
			url_type_1 = get_url.split('<a href="/ufi/reaction/?')[3].split('"')[0]
		elif loai == 'HAHA' :
			url_type_1 = get_url.split('<a href="/ufi/reaction/?')[4].split('"')[0]
		elif loai == 'WOW' :
			url_type_1 = get_url.split('<a href="/ufi/reaction/?')[5].split('"')[0]
		elif loai == 'SAD' :
			url_type_1 = get_url.split('<a href="/ufi/reaction/?')[6].split('"')[0]
		elif loai == 'ANGRY' :
			url_type_1 = get_url.split('<a href="/ufi/reaction/?')[7].split('"')[0]
		else :
			print ("văn ")
		ft_ent_identifier_1= url_type_1.split('ft_ent_identifier=')[1].split('&amp')[0]
		reaction_type_1= url_type_1.split('reaction_type=')[1].split('&amp')[0]
		is_permalink_1= url_type_1.split('is_permalink=')[1].split('&amp')[0]
		reaction_id_1= url_type_1.split('reaction_id=')[1].split('&amp')[0]
		basic_origin_uri_1= url_type_1.split('basic_origin_uri=')[1].split('&amp')[0]
		_ft__1= url_type_1.split('_ft_=')[1].split('&amp')[0]
		av_1= url_type_1.split('av=')[1].split('&amp')[0]
		eav_1= url_type_1.split('eav=')[1].split('&amp')[0]
		paipv_1= url_type_1.split('paipv=')[1].split('&amp')[0]
		ext_1= url_type_1.split('ext=')[1].split('&amp')[0]
		hash_1= url_type_1.split('hash=')[1].split('&amp')[0]
		url_cx_2_1 = f"https://mbasic.facebook.com/ufi/reaction/?ft_ent_identifier={ft_ent_identifier_1}&reaction_type={reaction_type_1}&reaction_id={reaction_id_1}&is_permalink={is_permalink_1}&basic_origin_uri={basic_origin_uri_1}&_ft_={_ft__1}&av={av_1}&eav={eav_1}&paipv={paipv_1}&ext={ext_1}&hash={hash_1}"
		cam_xuc_1 = requests.get(url_cx_2_1, headers=headers).text
	except:
		cam_xuc_1 = "ERROR"
		
	return cam_xuc_1

def follow(id,ck):
	url = f'https://mbasic.facebook.com/profile.php?id={id}'
	headers = {
	'Host':'mbasic.facebook.com',
	'upgrade-insecure-requests':'1',
	'user-agent':'Mozilla/5.0 (Linux; Android 8.1.0; CPH1912 Build/O11019) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.5359.128 Mobile Safari/537.36',
	'accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
	'sec-fetch-site':'none',
	'sec-fetch-mode':'navigate',
	'sec-fetch-user':'?1',
	'sec-fetch-dest':'document',
	'cookie': ck
	}
	home = requests.get(url, headers=headers).text
	try :
		url_type = home.split('<a href="/a/subscribe.php?')[1].split('"')[0]
		id= url_type.split('id=')[1].split('&amp')[0]
		eav= url_type.split('eav=')[1].split('&amp')[0]
		gfid= url_type.split('gfid=')[1].split('&amp')[0]
		paipv= url_type.split('paipv=')[1].split('&amp')[0]
		refid= url_type.split('refid=')[1].split('&amp')[0]
		url_sub = f'https://mbasic.facebook.com/a/subscribe.php?id={id}&eav={eav}&gfid={gfid}&paipv={paipv}&refid={refid}'
		follow = requests.get(url_sub, headers=headers).text
		
	except:
		follow= "ERROR"
		
	return follow 
	
def check_tt(ck):
	url = 'https://mbasic.facebook.com/menu/bookmarks/?ref_component=mbasic_home_header&ref_page=%2Fwap%2Fhome.php'
	headers = {
	'Host':'mbasic.facebook.com',
	'upgrade-insecure-requests':'1',
	'user-agent':'Mozilla/5.0 (Linux; Android 8.1.0; CPH1912 Build/O11019) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.5359.128 Mobile Safari/537.36',
	'accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
	'sec-fetch-site':'none',
	'sec-fetch-mode':'navigate',
	'sec-fetch-user':'?1',
	'sec-fetch-dest':'document',
	'cookie': ck
	}
	home = requests.get(url, headers=headers).text
	name = home.split('class="bn bo">')[1].split('<')[0]
	try :
		id = ck.split('c_user=')[1].split(';')[0]
	except:
		print (" Không Thể Get Được ID Facebook")
		id = input (' Nhập ID Facebook: ' )
	return json.dumps({"name": name,"id":id})


def cau_hinh(id, TDS_token, name):
    # Sửa dấu thừa ở cuối URL
    urlch = f"https://traodoisub.com/api/?fields=run&id={id}&access_token={TDS_token}"
    
    # Gửi yêu cầu GET
    ch = requests.get(url=urlch)
    
    try:
        # Kiểm tra nếu dữ liệu trả về là JSON và chứa các khóa cần thiết
        data = ch.json()
        if "data" in data and "msg" in data["data"]:
            checkch = data["data"]["msg"]
            print(f"Cấu Hình | ID: {id} | Name: {name}")
        else:
            print(f"Lỗi: Không tìm thấy 'data' hoặc 'msg' trong phản hồi.")
    
    # Bắt lỗi nếu không phải JSON hoặc có lỗi khi truy cập khóa
    except Exception as e:
        print(f"Cấu Hình Thất Bại {id} - Lỗi: {e}")
        exit()


def chon_job(listjob):
	print (" BẠN MUỐN CHẠY 3 JOB LIKE KHÔNG : [y/n] ")
	chon_1 = input(' Nhập : ')
	if chon_1 == "y" :
		job_1 = "like"
		listjob.append(job_1)
		job_3 = "likegiare"
		listjob.append(job_3)
		job_4 = "likesieure"
		listjob.append(job_4)
	print (" BẠN MUỐN CHẠY JOB REACTION KHÔNG : [y/n] ")
	chon_5 = input(' Nhập : ')
	if chon_5 == "y" :
		job_5 = "reaction"
		listjob.append(job_5)

	print (" BẠN MUỐN CHẠY JOB FOLLOW KHÔNG : [y/n] ")
	chon_2 = input(' Nhập : ')
	if chon_2 == "y" :
		job_2 = "follow"
		listjob.append(job_2)
		
	return listjob

os.system('clear')
logo()

### vào việc 
while True :
	token = input('\033[1;31m[\033[1;37m=.=\033[1;31m] \033[1;37m=> \033[1;32mNhập Token TDS : \033[1;33m')
	try : 
		check_xu = requests.get('https://traodoisub.com/api/?fields=profile&access_token='+token, timeout=5).json()
		tdstk = check_xu['data']['user']
		xu_5 = check_xu['data']['xu']
		break
	except:
		print ("\033[1;31m[\033[1;37m=.=\033[1;31m] \033[1;37m=> \033[1;31mToken Không Hợp Lệ ")
		continue
while True :
	ck = input('\033[1;31m[\033[1;37m=.=\033[1;31m] \033[1;37m=> \033[1;31mNhập Cookie Facebook : ')
	data_tt = check_tt(ck)
	try : 
		##data_tt = check_tt(ck)
		name = json.loads(data_tt)["name"]
		id = json.loads(data_tt)["id"]
		break
	except:
		print ("\033[1;31m[\033[1;37m=.=\033[1;31m] \033[1;37m=> \033[1;31mFacebook Không Hợp Lệ ")
		continue
print('-'*60)
ccc = chon_job(listjob)
print('-'*60)
dl = int(input(' Nhập Delay : '))
os.system('clear')
logo()
print (f' TÀI KHOẢN : {tdstk}')
print (f' XU HIỆN TẠI : {xu_5}')
print('-'*60)
cau_hinh(id, token, name)
tt = 0 
print('-'*60)

while True :
	ttt = 0 
	for cc in listjob:
		ttt += 1 
	for job in listjob:
		job_1 = requests.get(f'https://traodoisub.com/api/?fields={job}&access_token={token}')
		a = job_1.json()
		if ttt == 5 :
			print(f'[ĐANG TÌM JOB] => {job}    ',end='\r')
			try :
				b = a["error"] 
				for i in range(10,-1,-1):
					print(f'[TÌM JOB SAU] => {i} GIÂY   ',end='\r')
					sleep(1)
				continue 
			except :
				print(f'[TÌM THẤY JOB] => {job}    ',end='\r')
		elif ttt == 4 :
			try :
				b = a["error"] 
				for i in range(10,-1,-1):
					print(f'[TÌM JOB SAU] => {i} GIÂY   ',end='\r')
					sleep(1)
				continue 
			except :
				print(f'[TÌM THẤY JOB] => {job}    ',end='\r')
		elif ttt == 3 :
			try :
				b = a["error"] 
				for i in range(10,-1,-1):
					print(f'[TÌM JOB SAU] => {i} GIÂY   ',end='\r')
					sleep(1)
				continue 
			except :
				print(f'[TÌM THẤY JOB] => {job}    ',end='\r')
		else :
			try :
				b = a["error"] 
				for i in range(10,-1,-1):
					print(f'[TÌM JOB SAU] => {i} GIÂY   ',end='\r')
					sleep(1)
				continue 
			except :
				print(f'[TÌM THẤY JOB] => {job}    ',end='\r')
				
		if van == "dz" :
			for job_2 in a:
				id_job = job_2["id"]
				if job == "like" :
					type_1 = 'LIKE'
					type_2 = 'LIKE'
					cx = cam_xuc(id_job,ck,type_2)
				elif job == "likegiare" :
					type_1 = "LIKEGIARE"
					type_2 = 'LIKE'
					
					cam_xuc(id_job,ck,type_2)
				elif job == "likesieure" :
					type_1 = "LIKESIEURE"
					type_2 = 'LIKE'
					cx = cam_xuc(id_job,ck,type_2)
				elif job == "reaction" :
					type_1 = job_2["type"]
					cx = cam_xuc(id_job,ck,type_1)
				elif job == "follow" :
					type_1 = "FOLLOW"
					fl = follow(id_job,ck)
					print (fl)
					
				nhan = requests.get(f'https://traodoisub.com/api/coin/?type={type_1}&id={id_job}&access_token={token}')
				try :
					nhan_1 = nhan.json()["error"] 
					print (f' ERROR => {id_job} ',end='\r')
					sleep(1)
				except :
					tt += 1
					gio = datetime.now().strftime("%H:%M:%S")
					xu_1 = nhan.json()["data"]["msg"]
					xu_2 = nhan.json()["data"]["xu"]
					print (f" {tt} | {type_1} | {id_job} | {xu_1} | {xu_2} Xu")
				for i in range(dl,-1,-1):
					print(f'[ ĐANG DELAY CHẠY LẠI SAU ] => {i} GIÂY',end='\r')
					sleep(1)
						
					