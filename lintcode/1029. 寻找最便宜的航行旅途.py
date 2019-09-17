
from collections import deque
class Solution:
    """
    @param n: a integer
    @param flights: a 2D array
    @param src: a integer
    @param dst: a integer
    @param K: a integer
    @return: return a integer
    """
    def findCheapestPrice_BFS(self, n, flights, src, dst, K):
        # write your code here
        a = {}
        for item in flights:
            a[item[0]] = a.get(item[0], []) + [item[1:]]

        minCost = float('inf')
        next_vis = deque()
        while K >= 0:
            
        def DFS(K, src, cost):
            nonlocal minCost
            if src == dst:
                minCost = min(minCost, cost)
            if K >= 0 and cost < minCost:
                for nxt in a[src]:
                    if nxt[0] not in visisted:
                        visisted.add(nxt[0])
                        DFS(K-1, nxt[0], nxt[1]+cost)
                        visisted.remove(nxt[0])
        DFS(K, src, 0)
        return -1 if minCost == float('inf') else minCost

    def findCheapestPrice_DFS(self, n, flights, src, dst, K):
        # write your code here
        a = {}
        for item in flights:
            a[item[0]] = a.get(item[0], []) + [item[1:]]
        visisted = set()
        minCost = float('inf')

        def DFS(K, src, cost):
            nonlocal minCost
            if src == dst:
                minCost = min(minCost, cost)
            if K >= 0 and cost < minCost:
                for nxt in a[src]:
                    if nxt[0] not in visisted:
                        visisted.add(nxt[0])
                        DFS(K-1, nxt[0], nxt[1]+cost)
                        visisted.remove(nxt[0])
        DFS(K, src, 0)
        return -1 if minCost == float('inf') else minCost
