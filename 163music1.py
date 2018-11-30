import requests
from bs4 import BeautifulSoup

headers = {
	'Referer':'http://music.163.com',
	'Host':'nusic.163.com',
	'User-Agent':'Mozilla/5.0 (X11; Linux x86_64; rv:38.0) Gecko/20100101 Firefox/38.0',
	# Iceweasel/38.3.0
	'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'
}

play_url = 'http://music.163.com/playlist?id=317113395'

s = requests.session()
s = BeautifulSoup(s.get(play_url,headers = headers).contents)
main = s.find('ul',{'class':'f-hide'})

for music in main.find_all('a'):
	print('{} : {}'.format(music.text,music['href']))