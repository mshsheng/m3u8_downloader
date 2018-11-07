import ssl
import urllib.request
import os
from binascii import b2a_hex

# 忽略SSL检验
ssl._create_default_https_context = ssl._create_unverified_context

# 获取key地址
def get_key_url(m3u8_content):
    key_url = ''
    for line in m3u8_content:
        if ('#EXT-X-KEY' in line):
            uri_pos = line.find('URI')
            iv_pos = line.find('IV')
            key_url = line[(uri_pos+5):(iv_pos-2)] # 中间部分即为key地址
            break # 所有ts切片密码一致，故获取一组即可
    return key_url

# 获取key
def get_key(key_url):
    req = urllib.request.Request(key_url)
    data = urllib.request.urlopen(req).read()
    return bytes.decode(b2a_hex(data)) # 从二进制转换到字符串

def decrypt_data(key):
    iv = '00000000000000000000000000000000'
    os.system('openssl aes-128-cbc -d -in temp_e.ts -out temp_d.ts -nosalt -iv {0} -K {1}'.format(iv,key))