
'''
You are given two non-empty linked lists representing two non-negative integers.
The digits are stored in reverse order and each of their nodes contain a single digit.
Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
'''
'''
 342
+465
-----
 807
'''
class ListNode(object):
	"""docstring for ListNode"""
	def __init__(self, value = 0):
		super(ListNode, self).__init__()
		self.data = value
		self.next  = None



class Solution(object):
	def addTwoNumbers(self,l1,l2):
		result =[]
		carry = False
		index = 0
		while True:
			if index < len(l1) and index < len(l2):
				result.append((l1[index]+l2[index])%10)
				if carry:
					result[-1] = result[-1] +1
					carry = False
				if (l1[index]+l2[index]) >= 10:
					carry = True
				index = index + 1
			else:
				break
		#print(index, len(l1), len(l2))
		#pdb.set_trace()
		while index < len(l1):
			if carry:
				tmp = 1 +l1[index]
				result.append(tmp%10)
				if tmp >= 10:
					index += 1
				else:
					carry = False
					result+=(l1[index+1:])
					break
			else:
				result +=(l1[index:])
				break

		while index < len(l2):
			if carry:
				tmp = 1 +l2[index]
				result.append(tmp%10)
				if tmp >= 10:
					index += 1
				else:
					carry = False
					result.append(l2[index+1:])
					break
			else:
				result +=(l2[index:])
				break
		return result

	def addTwoNumbers1(self, l1, l2):
        if l1 == None: return l2
        if l2 == None: return l1
        flag = 0
        dummy = ListNode(0); p = dummy
        while l1 and l2:
            p.next = ListNode((l1.val+l2.val+flag) % 10)
            flag = (l1.val+l2.val+flag) / 10
            l1 = l1.next; l2 = l2.next; p = p.next
        if l2:
            while l2:
                p.next = ListNode((l2.val+flag) % 10)
                flag = (l2.val+flag) / 10
                l2 = l2.next; p = p.next
        if l1:
            while l1:
                p.next = ListNode((l1.val+flag) % 10)
                flag = (l1.val+flag) / 10
                l1 = l1.next; p = p.next
        if flag == 1: p.next = ListNode(1)
        return dummy.next

if __name__ == '__main__':
	l1 =[2,4,3]
	l2 =[5,6,4,5]
	s = Solution()
	print(s.addTwoNumbers(l1,l2))
