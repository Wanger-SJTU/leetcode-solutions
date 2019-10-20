from collections import defaultdict

class Solution:
    """
    @param ListA: The relation between ListB's books
    @param ListB: The relation between ListA's books
    @return: The answer
    """
    def maximumAssociationSet(self, ListA, ListB):
        # Write your code here
        res = []
        if not ListA or not ListB:
            return res
        record = {}
        cnt = defaultdict(int)
        for item in ListA:
            record[item] = record.get(item, item)

        for item in ListB:
            record[item] = record.get(item, item)
        print(record)
        for i, item in enumerate(ListA):
            root1 = self.unionFind(record, ListA[i])
            root2 = self.unionFind(record, ListB[i])
            if root1 != root2:
                record[root1] = root2
        for k,v in record.items():
            record[k] = self.unionFind(record, k)
        
        for k in record.keys():
            cnt[record[k]] += 1
        
        key,value = sorted(cnt.items(),key=lambda x: x[1])[-1]
        for k,v in record.items():
            if v == key:
                res.append(k)
        return res

    def unionFind(self, record, item):
        while record[item] != item:
            record[item] = record[record[item]]
            item = record[item]
        return item

if __name__ == "__main__":
    s = Solution()
    a = ["abc","abc","abc"]
    b = ["bcd","acd","def"]
    print(s.maximumAssociationSet(a,b))