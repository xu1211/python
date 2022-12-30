#!/usr/bin/python3

import re
"""
mybatisplus注解表对象 转为 openapi3对象
"""

def wordlist(text: str) -> str:
    # print(re.compile('\w+').findall(text))
    return re.compile('\w+').findall(text)


if (__name__ == "__main__"):
    f = open(
        "/Users/yuchunxu/Documents/Project/repository/git.woa.com/DataStudio/wedata/wedata-security/unified-data-security-audit/src/main/java/com/tencent/wedata/security/audit/domain/entity/SecurityAuditAlarmUser.java")

    # lines = f.read()
    # print(lines)
    # print(type(lines))

    # line = f.readline()
    # while line:
    #     print(line)
    #     print(type(line))
    #     line = f.readline()

    lines = f.readlines()
    for line in lines:
        if line.count(" * "):
            res1 = line.strip().strip('*').strip();
            print("    @ApiModelProperty(\"" + res1 + "\")")
        if line.count("private"):
            list = wordlist(line)
            if list[1] == "Date":
                print("    @JsonFormat(locale = \"zh\", timezone = \"GMT+8\", pattern = \"yyyy-MM-dd HH:mm:ss\")")
            Field = list[2]
            print("    @JsonProperty(\"" + Field[0].upper() + Field[1:] + "\")")
            print(line)

    f.close()
