# python3.5
# creater: Liyy
# Data: 2017.8.1

# 使用DES加密与解密,可对byte[],String类型进行加密与解密 密文可使用String,byte[]存储. 方法: void
# getKey(String strKey)从strKey的字条生成一个Key String getEncString(String
# strMing)对strMing进行加密,返回String密文 String getDesString(String
# strMi)对strMin进行解密,返回String明文 byte[] getEncCode(byte[] byteS)byte[]型的加密 byte[]
# getDesCode(byte[] byteD)byte[]型的解密

# For Python3, you'll need to use bytes, i.e.:
#   data = b"Please encrypt my data"
#   k = des(b"DESCRYPT", CBC, b"\0\0\0\0\0\0\0\0", pad=None, padmode=PAD_PKCS5)

import base64
from pyDes import *
from crypto import *
import random
import sha1
def getKey(string strKey):
	crypto.cipher
# secret_key = input("secret_key: ")	# 密钥
# token = input("token: ")	#string

data = "userPhone=12345678901"
# k = triple_des("123456781234567812345678", CBC, "\0\0\0\0\0\0\0\0", pad=None, padmode=PAD_PKCS5)
k = des(secret_key, CBC, "\0\0\0\0\0\0\0\0", pad=None, padmode=PAD_PKCS5)

d = k.encrypt(data)
# print "Encrypted: %r" % d
# print "Decrypted: %r" % k.decrypt(d)
assert k.decrypt(d, padmode=PAD_PKCS5) == data

secret_key = input("secret_key: ")
token = input("token: ")

result = 


def DesEncrypt(str):    # include getKey
    KeyGenerator _generator = KeyGenerator.getInstance("DES");
    SecureRandom secureRandom = SecureRandom.getInstance("SHA1PRNG");
    secureRandom.setSeed(strKey.getBytes("UTF-8"));
    _generator.init(secureRandom);
    this.key = _generator.generateKey();
    _generator = null;


