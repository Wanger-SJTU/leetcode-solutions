strs =['abc', '123456789']

new_strs = []


for item in strs:
    if len(item)>8:
        new_strs.append(item[:8])
        new_strs.append(item[8:]+'0'*(8-len(item[8:])))
    else:
        new_strs.append(item+'0'*(8-len(item)))

for item in sorted(new_strs):
    print(item, end=' ')