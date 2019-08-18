
import os

files = os.listdir('./python')

for file in files:
    file = file[:-2]+'md'
    file = os.path.join('./solutions',file)
    f = open(file, 'w')
    f.close()