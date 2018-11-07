import os

def create_directory(directory_name):
    os.system('mkdir {0}'.format(directory_name))

def write_file(path,data):
    with open(path, 'wb') as file_write:
        file_write.write(data)
        file_write.close()

def merge_file(video_name):
    file_read = open('temp_d.ts','rb')
    data = file_read.read()
    with open(video_name+'.ts', 'ab') as file_write:
        file_write.write(data)
        file_write.close()