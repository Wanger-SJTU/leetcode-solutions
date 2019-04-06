

def stack_order(l1:list, l2:list)->bool:
    stack = []
    while l2:
        if l1 and l1[0] == l2[0]:
            l1.pop(0)
            l2.pop(0)
        elif stack and stack[-1] == l2[0]:
            stack.pop()
            l2.pop(0)
        elif l1:
            stack.append(l1.pop(0))
        else:
            return False
    return True

if __name__ == "__main__":
    print(stack_order([1,2,3],[3,2,1]))