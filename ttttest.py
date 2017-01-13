#2017-1-9

#https://mail.qq.com/
#https://mail.qq.com/cgi-bin/login?vt=passport&vm=wpt&ft=loginpage&target=&account=627088113&qqmailkey=7b15e9ed6725fe94b518dd177fe769cd5cc61393d05499b9350de63641989fc9

#http://mail.163.com/
import urllib.request

#def getOpener(head):
    
url = 'https://mail.163.com/'

userName = '13524328545'
#'这里填你的知乎帐号'
password = 'LyyLee216'
#'这里填你的知乎密码'
postDict = {
       # '_xsrf':_xsrf,
        'userName': userName,
        'password': password,
       # 'formToken': 'hb8RADlIoxuvAi1qoJTx8XgqbDi4cKjY'
}
postData = urllib.parse.urlencode(postDict).encode()
op = opener.open(url, postData)

data = op.read()
#data = ungzip(data)
 
print(data.decode())
