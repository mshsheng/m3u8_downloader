import urllib
import urllib.request
import ssl

ssl._create_default_https_context = ssl._create_unverified_context

cookie = ''
ua = 'Mozilla/5.0 (iPad; CPU iPhone OS 11_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/11.0 Mobile/15E148 Safari/604.1'
referer = 'https://pc-shop.xiaoe-tech.com/app9v7Df3ju4703/video_details?id=v_5b090d2e26867_DoejMN7L'

header = {'User-Agent': ua,'Connection': 'keep-alive','Accept': '*/*','Cookie': cookie,'Accept-Encoding': 'gzip, deflate, br','Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8','Host': 'vod2.xiaoe-tech.com','Origin':'https://pc-shop.xiaoe-tech.com','Referer': referer}

url='https://vod2.xiaoe-tech.com/9764a7a5vodtransgzp1252524126/35c740f57447398156283767261/drm/'
fm3u8=open('v.f230.m3u','r')
m3u8=fm3u8.readlines()

j=0
for i in range(0,len(m3u8)):
    if (not m3u8[i].startswith('v.f230.ts')):
        continue    
    downurl = url+m3u8[i]
    j+=1
    print(j)
    print(downurl)
    req = urllib.request.Request(downurl, headers=header)
    path = 'v'+str(j)+'.ts'
    data = urllib.request.urlopen(req).read()
    with open(path, 'wb') as fw:
        fw.write(data)
        fw.close()
            
fm3u8.close()
