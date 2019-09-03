# -*- coding: UTF-8 -*-
# update.py
# @author wanger
# @description
# @created 2019-04-13T18:54:11.650Z+08:00
# @last-modified 2019-09-03T00:40:23.740Z+08:00
#


import os
import os.path as osp
import shutil

def TimeStampToTime(timestamp):
    timeStruct = time.localtime(timestamp)
    return time.strftime('%Y-%m-%d %H:%M:%S',timeStruct)

def get_FileSize(filePath):
    fsize = os.path.getsize(filePath)
    fsize = fsize/float(1024*1024)
    return round(fsize,2)

def get_FileAccessTime(filePath):
    t = os.path.getatime(filePath)
    return t

def get_FileCreateTime(filePath):
    t = os.path.getctime(filePath)
    return t

def get_FileModifyTime(filePath):
    return os.path.getmtime(filePath)

pythons = [item for item in os.listdir('./python') if item.endswith('.py')]
cpps = [item for item in os.listdir('./cpp') if item.endswith('.cpp')]
files = {}

for item in pythons:
    if 'update' in item:
        continue
    key = int(item.split('.')[0])
    if key not in files:
        files[key] = files.get(key,[])+[item]
    else:
        pre_t = get_FileCreateTime(osp.join('./python', files[key][0]))
        cur_t = get_FileCreateTime(osp.join('./python', item))
        if pre_t > cur_t:
            files[key] = [item]

for item in cpps:
    key = int(item.split('.')[0])
    files[key] = files.get(key,[])+[item]

with open('./README.md', 'w', encoding='utf8') as f:
    head = '### Content \n'
    head += 'solved '+str(len(files.keys()))+'\n\n'
    head += 'index|Problems|Solutions| |\n'
    head += '--|:--:|:--:|:--:\n'
    f.write(head)
    for idx in sorted(files.keys()):
        line = files[idx][0].split('.')[0] + '|'+ \
            files[idx][0].split('.')[1]
        for i, file in enumerate(files[idx]):
            if i == 0:
                path = './python/'+file
                line+= '|[python]('+path+')'
            if i == 1:
                path = './cpp/'+file
                line+= '|[cpp]('+path+')|'
        line += '\n'
        f.write(line)
    #    f.write('--|--|--\n')
