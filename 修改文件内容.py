import re,os
def alter(file, old_str, new_str):
    with open(file, "r", encoding="utf-8") as f1,open("%s.bak" % file, "w", encoding="utf-8") as f2:
        for line in f1:
            f2.write(re.sub(old_str,new_str,line))
    os.remove(file)
    os.rename("%s.bak" % file, file)
def settingName():
    u = 'C:\\Users\\Administrator\\Desktop\\dqwj'
    href = os.walk(u)
    for root, dirs, files in href:
        for n in files:
            old_file_name = u + '\\' + n
            alter(old_file_name,'400-838-','400-838-5616')
if __name__ == '__main__':
    settingName()
