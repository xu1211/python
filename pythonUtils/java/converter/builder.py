#!/usr/bin/python3

import re

"""
@Builder对象 生成构造方法
"""


# 行分词
def wordlist(text: str) -> str:
    # print(re.compile('\w+').findall(text))
    return re.compile('\w+').findall(text)


if (__name__ == "__main__"):
    # 打开对象文件
    basepath = "/Users/yuchunxu/Documents/Project/repository/git.woa.com/DataStudio/wedata/wedata-security/unified-data-security-audit/src/main/java/com/tencent/wedata/security/audit/"
    f = open(
        basepath + "domain/dto/SecurityAuditAlarmDTO.java"
    )

    # 一行行读
    lines = f.readlines()
    for line in lines:
        # 找到类名
        if line.count("public class"):
            list = wordlist(line)
            # 打印 类.builder()
            print(list[2] + ".builder()")
        # 找到字段名
        if line.count("private"):
            str_list = line.split()
            # print(str_list)
            Field = str_list[2].strip(';')
            # 打印 .字段(param.get驼峰字段) todo title错误
            print("                ." + Field + "(param.get" + Field.title() + "())")
    f.close()
    print("                .build();")
