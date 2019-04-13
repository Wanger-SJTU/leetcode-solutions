import sys

line = sys.stdin.readline().strip()
newStr = ""

left = {'(', '[', '{'}
nums,chars = [],[]

i,length = 0,len(line)

while i < length:
    j = i+1
    if line[i].isdigit():
        num = int(line[i])
        while j<length:
            if line[j].isdigit():
                num = num*10 + int(line[j])
                j+=1
            else:
                break
        nums.append(num)
    elif line[i] in left or line[i].isalpha():
        chars.append(line[i])
    else:
        t,tmpchar = chars.pop(),[]
        while t not in left:
            tmpchar.append(t)
            t = chars.pop()
        tchars = nums.pop()*''.join(tmpchar[::-1])
        chars.append(tchars)
    i = j
    
print("".join(chars)[::-1])
        

