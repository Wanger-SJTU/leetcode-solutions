
from typing import List

def letterCasePermutation_DFS(S: str) -> List[str]:
    res = [S]
    for i in range(len(S)) : 
        if S[i].isalpha() : 
            res.extend([s[:i] + s[i].swapcase() + s[i+1:] for s in res])
    return res

def letterCasePermutation_BFS(S: str) -> List[str]:
    res = [""]
    for item in S : 
        if item.isalpha() : 
            lower = [s + item.lower() for s in res]
            upper = [s + item.upper() for s in res]
            res = lower + upper
        else:
            res = [s + item for s in res]
    return list(set(res))

if __name__ == "__main__":
    print(letterCasePermutation_BFS("asasf"))