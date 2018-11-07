import os

# 创建新文件夹
def create_directory(directory_name):
    os.system('mkdir {0}'.format(directory_name))

# 写文件
def write_file(path,data):
    with open(path, 'wb') as file_write: # wb:覆盖式二进制写入
        file_write.write(data)
        file_write.close()

# 合并文件
def merge_file(video_name):
    file_read = open('temp_d.ts','rb')
    data = file_read.read()
    with open(video_name+'.ts', 'ab') as file_write: # ab:追加式二进制写入
        file_write.write(data)
        file_write.close()