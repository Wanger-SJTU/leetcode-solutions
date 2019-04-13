strs =['abc', '1234567899876543210123456']

new_strs = []


for item in strs:
    if len(item)>8:
        n,p = divmod(len(item),8)
        new_strs+= [item[i*8:i*8+8] for i in range(n)]
        new_strs.append(item[-p:]+'0'*(8-p))
    else:
        new_strs.append(item+'0'*(8-len(item)))

for item in sorted(new_strs):
    print(item, end=' ')