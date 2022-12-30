#!/usr/bin/python3

from xml.dom.minidom import parse
from domain.maven import maven
import xml.dom.minidom
import json


'''
功能： 打印所有引用的包
格式：

sax 一次性读取整个文档，把文档中所有元素保存在内存中的一个树结构里
'''

# 格式化输出
def pretty(d):
    return json.dumps(d, indent=4, ensure_ascii=False)


if (__name__ == "__main__"):
    def __init__(self):
        # 当前group
        self.GroupId = ""
        # 当前ArtifactId
        self.ArtifactId = ""


    # 使用minidom解析器打开 XML 文档
    DOMTree = xml.dom.minidom.parse(
        "/Users/yuchunxu/Documents/Project/repository/e.coding.net/linglong3/phase3/member/pom.xml")
    # DOM树最外层
    project = DOMTree.documentElement

    # 获取依赖关系树 dependencies
    dependencies = project.getElementsByTagName("dependencies")[0]
    # 获取依赖关系列表 dependency
    dependencyS = dependencies.getElementsByTagName("dependency")
    # 遍历依赖
    for dependency in dependencyS:
        # 获取 groupId，保存在 maven.dependencies 字典
        groupIds = dependency.getElementsByTagName(maven.dependenciesKey[0])
        if len(groupIds) > 0:
            groupId = groupIds[0]
            GroupId = groupId.childNodes[0].data
            # print("Type: %s" % groupId.childNodes[0].data)
            if not GroupId in maven.dependencies:
                maven.dependencies[GroupId] = 0

        # 获取 artifactId，保存在 maven.artifact
        artifactIds = dependency.getElementsByTagName(maven.dependenciesKey[1])
        if len(artifactIds) > 0:
            artifactId = artifactIds[0]
            ArtifactId = artifactId.childNodes[0].data
            # print("Type: %s" % artifactId.childNodes[0].data)
            if not ArtifactId in maven.artifact:
                maven.artifact.append(ArtifactId)

        # versions = dependency.getElementsByTagName(maven.dependenciesKey[2])
        # if len(versions) > 0:
        #     version = versions[0]
        #     maven.artifact[ArtifactId] = version.childNodes[0].data
        #     # print("Type: %s" % version.childNodes[0].data)

        maven.artifact.sort()
        # artifactId 放在对应 GroupId下
        maven.dependencies[GroupId] = maven.artifact

        GroupId = ""
        ArtifactId = ""

    # a = sorted(maven.dependencies.items(), key=lambda x: x[0], reverse=True)
    print(pretty(maven.dependencies))
