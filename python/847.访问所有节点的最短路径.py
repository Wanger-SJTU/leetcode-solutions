#
# @lc app=leetcode.cn id=847 lang=python3
#
# [847] 访问所有节点的最短路径
#
import collections

class Solution:
    def shortestPathLength(self, graph: List[List[int]]) -> int:
        N = len(graph)
        que = collections.deque()
        step,goal = 0, (1 << N) - 1
        visited = [[False]*(1 << N) for _ in range(N)]
        for i in range(N):
            que.append((i, 1 << i))
        while que:
            s = len(que)
            for i in range(s):
                node, state = que.popleft()
                if state == goal:
                    return step
                if visited[node][state]:
                    continue
                visited[node][state] = True
                for nextNode in graph[node]:
                    que.append((nextNode, state | (1 << nextNode)))
            step += 1
        return step

