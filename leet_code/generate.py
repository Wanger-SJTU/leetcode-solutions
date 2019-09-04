
import os

def split(name):
    return name.split('.')[0]

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
