# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import requests
import re
import io
import sys
# import wkhtmltopdf,
import pdfkit
import logging
import time
headers = {
	# 'Referer':'http://music.163.com',
	# 'Host':'nusic.163.com',
	'User-Agent':'Mozilla/5.0 (X11; Linux x86_64; rv:38.0) Gecko/20100101 Firefox/38.0',
	# Iceweasel/38.3.0
	'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'
}
# 贴心萌宝荒唐爹
start_url = 'http://www.biqugecom.com/13/13172/'

def spider():
	global start_url,headers
	sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='gb18030')  

	booklist = requests.get(start_url,headers = headers)
	booklistsoup = BeautifulSoup(booklist.content, 'html5lib')
	# print(booklistsoup)
	# titlesoup = booklistsoup.find("dt",text="《贴心萌宝荒唐爹》正文卷")
	# titlesoup = booklistsoup.find("a",text="第220章突然见面").parent
	titlesoup = booklistsoup.find("a",text="第693章他捡回了她").parent
	# print(titlesoup)
	# pattern = re.compile("《贴心萌宝荒唐爹》正文卷")
	# elements = booklistsoup.find_next_siblings("dt",text=pattern)
	elements = titlesoup.find_next_siblings("dd")
	print ("==========elements has been got.==========")
	# print(str(elements))
	# url = start_url + "/23828662.html"
	for element in elements:
		# /13/13172/23828662.html
		# url1 = element.find('a',attrs = {'href':re.compile(r"^/13/13172/[1-9]*")}).get('href')
		# print(element)
		url1 = element.find("a").get("href")
		print(url1)
		url = 'http://www.biqugecom.com' + url1
		time.sleep(10)
		r = requests.get(url,headers = headers)

		if 200 <= r.status_code < 300 :

			contentsoup = BeautifulSoup(r.content, 'html5lib')
			# print ("========== contentsoup has been caught. ==========")	#20180129
			# contentsoup = soup.find('dt',{'id':'content'})
			# strsoup = str(soup)
			# with open("E:\\py\\soup.txt",'w', encoding = "UTF-8") as f:
			# 	f.write(strsoup)
			# xprint (soup)

			# tags = soup.find_all('ul',{'class':'uk-nav uk-nav-side'})[2].find_all('a',attrs = {'href':re.compile(r"^/wiki/.*")})
			# tags = soup.find('div',{'id':'content'}).get_text()})
			bookname = str(contentsoup.find('div',{'class':'bookname'}).find('h1').get_text())
			content1 = str(contentsoup.find('div',{'id':'content'}).get_text())
			# print ("==========content has been got.==========")	#20180129
			writetitleinto(bookname)
			writeinto(content1)
			# pagenum
			# return content1
		else:
			print("200 <= r.status_code < 300    ????")
			return None

	print("     Done!     ")

def writeinto(content1):

	if content1:
		
		# print ("========== Begin to write. ==========")	#20180129
		# print (tags)
		# print (content1)
		with open("E:\\py\\tiexinmengbao2.txt",'a', encoding='utf-8') as f:
			f.write(content1)
			f.write("\n\n===========================================================================\n\n")
		# f = open("out.txt","w",encoding='utf-8')
	else:
		print("========== Nothing to write. Please check. ==========")

def writetitleinto(bookname):

	if bookname:
		
		with open("E:\\py\\tiexinmengbao2.txt",'a', encoding='utf-8') as f:
			f.write(bookname)
			f.write("\n—————————————————— \n")
		# f = open("out.txt","w",encoding='utf-8')
	else:
		print("========== Nothing to write. Please check. ==========")

# s = requests.session()
# s = BeautifulSoup(s.get(play_url,headers = headers).contents,'html5lib')
# main = s.find('ul',{'class':'f-hide'})

# for music in main.find_all('a'):
# 	print('{} : {}'.format(music.text,music['href']))
# urls = soup.find_all('ul',class_ = "uk-nav uk-nav-side").find_all('a',attrs = {'href':re.compile(r"^/wiki/*")})
# print(str(soup).encode("GBK", 'ignore'))
def makebook(tags):
	if tags is None:
		return 
	
	global start_url,headers
	for tag in tags:
		url = start_url + tag.get('href')
		print (url)
		r = requests.get(url,headers = headers)
		print (r.status_code)

		if 200 <= r.status_code < 300 :
			soup = BeautifulSoup(r.content, 'html5lib')
			content = soup.find_all('div',{'class':'x-wiki-content x-main-content'})
			# print (r.status_code)
			strcontent = str(content)
			with open("E:\\py\\makebook1.html",'a') as f:
				f.write(strcontent)

	options = {
	        'page-size': 'Letter',
	        'encoding': "UTF-8",
	        'custom-header': [
	            ('Accept-Encoding', 'gzip')
	        ]
	    }
	pdfkit.from_file("makebook1.html", output_path = "E:\\py\\lxfpdf.pdf" , options=options)
# print(str(urls).encode("GBK", 'ignore'))

# print (strcontent)

if __name__ == '__main__':
	spider()
	# makebook(spider())