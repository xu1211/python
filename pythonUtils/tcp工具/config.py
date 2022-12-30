import json
'''读取配置文件address.json'''

with open('address.json', 'r') as f:
    data = json.load(f)

ipList = []
portList = []

def getIp():
    j=0
    for i in data['ip']:
        ipList.append(data['ip'][j][str(j)])
        j += 1
    return ipList

def getPort():
    j=0
    for i in data['port']:
        portList.append(data['port'][j][str(j)])
        j += 1
    return portList