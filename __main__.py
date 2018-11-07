import decrypt
import download
import file_system
import net_format

# 输出文件名
video_name = input('Video name: ')

# 获取m3u8地址
urls=net_format.urls()
main_url = urls['main_url']

# referer参数
headers = net_format.headers_pack()

# m3u8下载
m3u8_content = download.m3u8_download(m3u8_url=urls['m3u8_url'],headers=headers)

# 获取key
key_url = decrypt.get_key_url(m3u8_content)
key = decrypt.get_key(key_url)

# 循环下载ts切片
file_index = 0
for line in m3u8_content:
    if (not ('.ts' in line)):
        continue
    ts_url = main_url + line
    # 下载ts切片
    print('Downloading ts file #{0}'.format(file_index))
    download.ts_download(ts_url=ts_url,headers=headers)
    print('Downloaded ts file #{0}'.format(file_index))
    # 解密
    print('Decrypting ts file #{0}'.format(file_index))
    decrypt.decrypt_data(key=key)
    print('Decrypted ts file #{0}'.format(file_index))
    # 合并
    print('Merging ts file #{0}'.format(file_index))
    file_system.merge_file(video_name=video_name)
    print('Merged ts file #{0}'.format(file_index))
    file_index+=1