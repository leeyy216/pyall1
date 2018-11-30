from bs4 import BeautifulSoup
import requests
import re
# import wkhtmltopdf,
import pdfkit
import logging
headers = {
	# 'Referer':'http://music.163.com',
	# 'Host':'nusic.163.com',
	'User-Agent':'Mozilla/5.0 (X11; Linux x86_64; rv:38.0) Gecko/20100101 Firefox/38.0',
	# Iceweasel/38.3.0
	'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'
}
start_url = 'https://www.liaoxuefeng.com'

def spider():
	global start_url,headers
	url = start_url + "/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000"
	r = requests.get(url,headers = headers)
	if 200 <= r.status_code < 300 :

		soup = BeautifulSoup(r.content, 'html5lib')
		print ("==========soup has been got.==========")	#20180129
		strsoup = str(soup)
		# with open("E:\\py\\soup.txt",'w', encoding = "UTF-8") as f:
		# 	f.write(strsoup)
		# xprint (soup)

		# tags = soup.find_all('ul',{'class':'uk-nav uk-nav-side'})[2].find_all('a',attrs = {'href':re.compile(r"^/wiki/.*")})
		tags = soup.find('ul',{'id':'x-wiki-index'}).find_all('a',attrs = {'href':re.compile(r"^/wiki/.*")})
		print ("==========tags has been got.==========")	#20180129
		# print (tags)
		# pagenum
		return tags
	return None

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
	
	makebook(spider())