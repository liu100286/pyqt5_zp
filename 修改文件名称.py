import os
def file_name():
    u  = 'C:\\Users\\Administrator\\Desktop\\dqwj'
    href = os.walk(u)
    for root, dirs, files in href:
        print(root) #当前目录路径
        print(dirs) #当前路径下所有子目录
        print(files) #当前路径下所有非目录子文件
        # for n in files:
        #     # 读取文件修改文案名称
        #     old_file_name = u+'\\'+n
        #     # print(old_file_name)
        #     new_file_name =  u+'\\sm'+n
        #     os.rename(old_file_name, new_file_name)
if __name__ == '__main__':
    file_name()