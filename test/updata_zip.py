#coding=utf-8
import json
import os
import os.path
import datetime
import re
updatafile_dir = 'E:/'
l = os.listdir(updatafile_dir)
l.sort(key=lambda fn: os.path.getmtime(updatafile_dir+fn) if not os.path.isdir(updatafile_dir+fn) else 0)
d = datetime.datetime.fromtimestamp(os.path.getmtime(updatafile_dir+l[-1]))
file_name = re.findall(r'.*zip$', l[-1])
if file_name.__len__() > 0:
    print('更新包为:'+l[-1])
    name = l[-1]
    version = l[-1].split('.')[0] + '.' + l[-1].split('.')[1] + '.' + l[-1].split('.')[2]
    size = os.path.getsize(updatafile_dir + name)
    size = size // 1024
    print('更新包大小为:', size, 'KB')
    file_gameVersionsKorea = 'C:/Users/zuolei/Desktop/表文件/gameVersionsKorea.json'
    dict = {}
    file = open(file_gameVersionsKorea)
    f = file.read()
    fd = json.loads(f)
    maxId = 1
    zipID = int(l[-1].split('.')[2])
    for i in fd:
        if int(i) > int(maxId):
            maxId = i
        dict[i] = fd[i]
    maxId = int(maxId) + 1
    temp = {}
    if maxId == zipID:
        temp["id"] = maxId
        temp["version"] = version
        temp["size"] = size
        dict[str(maxId)] = temp
        nr = json.dumps(dict, indent=4)
        file = open(file_gameVersionsKorea, 'w', encoding='utf-8')
        file.write(nr)
        file.close()
        print(dict)
    else:
        print('maxID:', maxId, 'zipID:', zipID)
        print(type(maxId), type(zipID))
        exit()