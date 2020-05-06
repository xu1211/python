#!/usr/bin/python3
# -*- coding: UTF-8 -*- 

str = input("请输入：");
print ("你输入的内容是: ", str)

#文件 打开
with open('./test.txt', 'a+', encoding='utf8') as f:
    #写
    f.write("\n追加:" + str)
    ## 移动到文件起始位置
    f.seek(0)
    #读
    print (f.read())
#关
f.close()
 
'''
#os 模块用来处理文件和目录
#重命名文件
os.rename(current_file_name, new_file_name)
#删除文件
os.remove(file_name)
#当前目录
os.chdir("newdir")
#当前目录下创建目录
os.mkdir("newdir")
#删除目录
os.rmdir('dirname')
'''