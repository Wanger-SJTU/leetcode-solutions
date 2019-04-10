def decodeString(s, i):
        """
        :type s: str
        :rtype: str
        """
        right = {')',']','}'}
        rst = ''
        while i[0]<len(s) and s[i[0]] not in right:
            if not s[i[0]].isdigit():
                rst += s[i[0]]
                i[0] += 1
            else:
                num = 0
                while i[0]<len(s) and s[i[0]].isdigit():
                    num = num*10 + int(s[i[0]])
                    i[0] += 1
                i[0] += 1
                temp = decodeString(s,i)
                i[0] += 1
                rst += num*temp
        return rst
        
if __name__ == "__main__":
    print(decodeString("asd4(A)", [0]))