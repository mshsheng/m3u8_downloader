# headers打包
def headers_pack():
    referer = input('Referer: ') # 必要参数
    ua = 'Mozilla/5.0 (iPad; CPU iPhone OS 11_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/11.0 Mobile/15E148 Safari/604.1'
    connection = 'keep-alive'
    accept = '*/*'
    cookie = ''
    accept_encoding = 'gzip, deflate, br'
    accept_language = 'zh-CN,zh;q=0.9,en;q=0.8'
    host = 'vod2.xiaoe-tech.com'
    origin = 'https://pc-shop.xiaoe-tech.com'

    headers = {'User-Agent': ua, 'Connection': connection, 'Accept': accept, 'Cookie': cookie,
              'Accept-Encoding': accept_encoding, 'Accept-Language': accept_language,
              'Host': host, 'Origin': origin, 'Referer': referer}

    return headers

# 获取绝对路径
def urls():
    m3u8_url = input('M3U8 URL: ')
    length = m3u8_url.find('drm')+4
    main_url = m3u8_url[0:length]
    urldict = {'m3u8_url': m3u8_url,'main_url': main_url}
    return urldict