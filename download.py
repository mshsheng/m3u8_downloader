import ssl
import urllib.request
import file_system

ssl._create_default_https_context = ssl._create_unverified_context

def m3u8_download(m3u8_url,headers):
    req = urllib.request.Request(m3u8_url,headers=headers)
    path = 'temp.m3u8'
    data = urllib.request.urlopen(req).read()
    data_utf8 = data.decode('utf8')
    m3u8_content = data_utf8.split('\n')
    return m3u8_content

def ts_download(ts_url,headers):
    req = urllib.request.Request(ts_url, headers=headers)
    path = 'temp_e.ts'
    data = urllib.request.urlopen(req).read()
    file_system.write_file(path=path,data=data)
