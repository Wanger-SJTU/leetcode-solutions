
import os


root = os.path.dirname(__file__)
files = os.listdir(os.path.join(root,'src'))

for file in files:
    file = file[:-2]+'md'
    file = os.path.join(root, 'solution', file)
    if not os.path.exists(file):
        f = open(file, 'w')
        f.close()
