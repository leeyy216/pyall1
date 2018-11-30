from bs4 import BeautifulSoup
import requests
import re
# import wkhtmltopdf,
import pdfkit
import logging
import xlwt

headers = {
	# 'Referer':'http://music.163.com',
	# 'Host':'nusic.163.com',
	'User-Agent':'Mozilla/5.0 (X11; Linux x86_64; rv:38.0) Gecko/20100101 Firefox/38.0',
	# Iceweasel/38.3.0
	'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'
}

# start_url = 'http://store.steampowered.com/games/'
start_url = 'http://store.steampowered.com/tags/zh-cn/'

def spider():
	global start_url,headers
	url = start_url + "模拟/"
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

def wtexl():
	rdworkbook = xlrd.open_workbook(r"blogexcel.xlsx")
	all_sheets_list = rdworkbook.sheet_names()
	print("All sheets namme in File:",all_sheets_list)
	#确定所需infosheet
	info_sheet = rdworkbook.sheet_by_index(1)
	print("infosheet is %s" %info_sheet.name)
	#遍历infosheet中所有行
	num_rows = info_sheet.nrows
	for curr_row in range(num_rows):
		row = info_sheet.row_values(curr_row)
		from_sch,stu_num,stu_name,into_sch = row[0],row[1],row[2],row[3]
		#print('%s from %s whose num is %s go into %s' %(stu_name,from_sch,stu_num,into_sch))
		Enrollinfo.objects.get_or_create(from_sch = from_sch,stu_num = stu_num,stu_name = stu_name,into_sch = into_sch)
		#print('row%s is %s' %(curr_row,row))
		print('------------row%s has been saved to db!------------' %curr_row)

	#遍历infosheet中所有列
	num_cols = info_sheet.ncols
	for curr_col in range(num_cols):
		col = info_sheet.col_values(curr_col)
		print('col%s is %s' %(curr_col,col))


if __name__ == '__main__':
	
	makebook(spider())