import ssl
import urllib.request
import os
from binascii import b2a_hex

ssl._create_default_https_context = ssl._create_unverified_context

def get_key_url(m3u8_content):
    key_url = ''
    for line in m3u8_content:
        if ('#EXT-X-KEY' in line):
            uri_pos = line.find('URI')
            iv_pos = line.find('IV')
            key_url = line[(uri_pos+5):(iv_pos-2)]
            break
    return key_url

def get_key(key_url):
    req = urllib.request.Request(key_url)
    data = urllib.request.urlopen(req).read()
    return bytes.decode(b2a_hex(data))

def decrypt_data(key):
    iv = '00000000000000000000000000000000'
    os.system('openssl aes-128-cbc -d -in temp_e.ts -out temp_d.ts -nosalt -iv {0} -K {1}'.format(iv,key))