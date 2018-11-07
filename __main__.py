import decrypt
import download
import file_system
import net_format

# new directory
video_name = input('Video name: ')
#file_system.create_directory(directory_name=video_name)

# m3u8 url
urls=net_format.urls()

# referer
headers = net_format.headers_pack()

# download
main_url = urls['main_url']

m3u8_content = download.m3u8_download(m3u8_url=urls['m3u8_url'],headers=headers)

key_url = decrypt.get_key_url(m3u8_content)
key = decrypt.get_key(key_url)

for line in m3u8_content:
    if (not ('.ts' in line)):
        continue
    ts_url = main_url + line
    download.ts_download(ts_url=ts_url,headers=headers)
    decrypt.decrypt_data(key)
    file_system.merge_file(video_name=video_name)

# decrypt
# write