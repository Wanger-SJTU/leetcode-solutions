
import os
import argparse

def split(name):
    return name.split('.')[0]

def generate():
    root = os.path.dirname(__file__)
    files = os.listdir(os.path.join(root,'python'))
    cur_files = os.listdir(os.path.join(root,'solutions'))
    cur_files = set(map(split, cur_files))
    for file in files:
        file = file[:-2]+'md'
        if split(file) not in cur_files:
            file = os.path.join(root, 'solutions', file)
            f = open(file, 'w')
            f.close()

def delete():
    root = os.path.dirname(__file__)
    dirname = os.path.join(root, 'solutions')
    for file in os.listdir(dirname):
        fp = os.path.join(dirname, file)
        sz = os.path.getsize(fp)
        if sz == 0:
            os.remove(fp)
delete()
