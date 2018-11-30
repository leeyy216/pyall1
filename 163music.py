import base64
import random
import json
import requests
import crypto,pycrypto
from crypto.Cipher import AES

#consts here

first_key = "0CoJUm6Qyw8W8jud"

iv = "0102030405060708"

def pksc7_padding(string):
    aes_block_size = 16
    padding_size = aes_block_size - len(string) % 16
    return string.ljust(len(string)+padding_size, chr(padding_size))

def make_json_data(url_id):
    fixed = {}
    fixed['br'] = 128000
    fixed['csrf_token'] = '' #in the cookie
    fixed['ids'] = '[{}]'.format(url_id)
    return json.dumps(fixed, separators=(',', ':'))


def random_string():
    base_str = '1234567890ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
    r_str = ''
    for i in range(0, 16):
        r_str += base_str[random.randint(0, len(base_str) - 1)]
    return r_str

def RSA_string(input_str):
    modular = 157794750267131502212476817800345498121872783333389747424011531025366277535262539913701806290766479189477533597854989606803194253978660329941980786072432806427833685472618792592200595694346872951301770580765135349259590167490536138082469680638514416594216629258349130257685001248172188325316586707301643237607
    exp = 65537

#first do LE packing
    to_number = 0
    rev_str = input_str[::-1]
    for i in rev_str:
        to_number = to_number * 256 + ord(i)
#then calc ras with exp and modular
    encSecKey = hex(pow(to_number, exp, modular))[2:]
    return encSecKey.rjust(256, '0')
    
def AES_128_CBC_b64_wrapper(data, key, iv):
    obj = AES.new(key, AES.MODE_CBC, iv)
    input_data = pksc7_padding(data)
    out = obj.encrypt(input_data)
    return base64.b64encode(out).decode('utf8')

def netease_req(ids='468490608', snd_key=None, encSecKey=None):
    data = make_json_data(ids)
    if snd_key is None:
        snd_key = random_string()
        encSecKey = RSA_string(snd_key)
    first_pass = AES_128_CBC_b64_wrapper(data, first_key, iv)
    second_pass = AES_128_CBC_b64_wrapper(first_pass, snd_key, iv)

    payload = {}
    payload['params'] = second_pass
    payload['encSecKey'] = encSecKey

    return payload

if __name__ == '__main__':
    url = 'http://music.163.com/weapi/song/enhance/player/url?csfr_token='
    snd_key = random_string()
    encSecKey = RSA_string(snd_key)
    test_ids = ['306672', '254095', '208934']
    for test_id in test_ids:
        payload = netease_req(test_id, snd_key, encSecKey)
        r = requests.post(url, data=payload)
        print(json.loads(r.content.decode('utf8')))