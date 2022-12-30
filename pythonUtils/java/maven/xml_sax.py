#!/usr/bin/python3

import xml.sax
import json
from domain.maven import maven

'''
从上往下，加载一点，读取一点，处理一点。对内存要求比较低
加载到哪个元素，触发哪个元素的处理事件
    开始加载文档：startDocument()
    加载到起始标签：startElement(name, attrs)
    加载到标签之间的字符：characters(content) 
    加载到结束标签：endElement(name) 
    完成加载文档：endDocument()
'''
# 格式化输出
def pretty(d):
    return json.dumps(d, indent=4, ensure_ascii=False)


class MavenHandler(xml.sax.ContentHandler, maven):
    def __init__(self):
        # 当前标签name
        self.CurrentData = ""
        # 当前group
        self.GroupId = ""
        self.ArtifactId = ""


    # 元素开始事件处理
    def startElement(self, tag, attributes):
        # print("当前标签", tag)

        self.CurrentData = tag
        if tag == maven.Element[0]:
            print()
            print(">>>>>>>>>>>>>", maven.Element[0])

        if tag == maven.Element[1]:
            print()
            print(">>>>>>>>>>>>>", maven.Element[1])

        if tag == maven.Element[2]:
            print()
            print(">>>>>>>>>>>>>", maven.Element[2])

    # 内容事件处理
    def characters(self, content):
        # print("当前内容", content)
        if self.CurrentData == 'groupId':
            self.GroupId = content

            if 'groupId' in maven.dependencies:
                maven.dependencies[content] = 0
        elif self.CurrentData == 'artifactId':
            self.ArtifactId = content

            maven.artifact[content] = 0
        elif self.CurrentData == 'version':
            maven.artifact[self.ArtifactId] = content
        maven.dependencies[self.GroupId] = maven.artifact

    # 元素结束事件处理
    def endElement(self, tag):
        if tag == maven.Element[0]:
            print(pretty(maven.dependencies))
        # if self.CurrentData == 'groupId':
        #
        # if self.CurrentData == 'artifactId':
        #
        # if self.CurrentData == 'version':
        #     print(maven.dependencies[self.GroupId])
        self.CurrentData = ""
        self.GroupId = ""

    def endDocument(self):
        print("end")


if (__name__ == "__main__"):
    # 创建一个 XMLReader SAX解析对象
    parser = xml.sax.make_parser()
    # turn off namepsaces
    parser.setFeature(xml.sax.handler.feature_namespaces, 0)

    # 重写 ContextHandler
    Handler = MavenHandler()
    parser.setContentHandler(Handler)

    parser.parse(
        "/Users/yuchunxu/Documents/Project/repository/git.woa.com/qidian_energize/member/member/pom.xml")

# /Users/yuchunxu/Documents/Project/repository/git.woa.com/qidian_energize/member/member/pom.xml
# /Users/yuchunxu/Documents/Project/repository/e.coding.net/linglong3/phase3/member/pom.xml
