# -*- coding: UTF-8 -*-
# update.py
# @author wanger
# @description 
# @created Sat Apr 13 2019 18:54:11 GMT+0800 (中国标准时间)
# @last-modified Fri May 10 2019 09:33:59 GMT+0800 (中国标准时间)
#


import os
import os.path as osp
import shutil

root = os.path.dirname(__file__)

pythons = [item for item in os.listdir(root+'/python') if item.endswith('.py')]
cpps = [item for item in os.listdir(root+'/cpp') if item.endswith('.cpp')]
files = {}

for item in pythons:
    if 'update' in item: 
        continue
    key = item.split('.')[0]
    files[key] = files.get(key,[])+[item]

for item in cpps:
    key = item.split('.')[0]
    files[key] = files.get(key,[])+[item]
    
with open(root+'/README.md', 'w',encoding='utf8') as f:
    head = '### Content \n'
    head += 'solved '+str(len(files.keys()))+'\n\n'
    head += 'Problems|Solutions| |\n'
    head += '--:|:--:|:--:\n'
    f.write(head)
    for idx in sorted(files.keys()):
        print(files[idx][0].split('.')[0])
        line = files[idx][0].split('.')[0]
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