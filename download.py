import ssl
import urllib.request
import file_system

# 忽略SSL检验
ssl._create_default_https_context = ssl._create_unverified_context

# 获取m3u8
def m3u8_download(m3u8_url,headers):
    req = urllib.request.Request(m3u8_url,headers=headers)
    data = urllib.request.urlopen(req).read()
    data_utf8 = data.decode('utf8') # UTF-8编码
    m3u8_content = data_utf8.split('\n') # m3u8 按行分割
    return m3u8_content

# 下载被加密的ts切片
def ts_download(ts_url,headers):
    req = urllib.request.Request(ts_url, headers=headers)
    path = 'temp_e.ts' # 'e' stands for 'encrypted'
    data = urllib.request.urlopen(req).read()
    file_system.write_file(path=path,data=data)
