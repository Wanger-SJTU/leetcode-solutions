#
# @lc app=leetcode id=207 lang=python3
#
# [207] Course Schedule
#
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        pass

    def topologySort(self, numCourses: int, prerequisites: List[List[int]]):
        indegree = [0 for i in range(numCourses)] 
        connection = {i:[] for i in range(numCourses)}
        for link in prerequisites:
            connection[link[1]].append(link[0])
            indegree[link[0]] += 1
        zero_indegree = []
        for i in range(numCourses):
            if indegree[i] == 0:
                zero_indegree.append(i)
        i = 0
        while i<len(zero_indegree):
            for node in connection[zero_indegree[i]]:
                indegree[node] -= 1
                if  indegree[node] == 0:
                    zero_indegree.append(node)
            i += 1
        if len(zero_indegree) == numCourses:
            return True
        else:
            return False

    
    def DFS(self, numCourses: int, prerequisites: List[List[int]]):
        record = [[0 for _ in range(numCourses)] 
                    for _ in range(numCourses)]
        
        visited = [False for _ in range(numCourses)] 
        
        for item in prerequisites:
            record[item[1]][item[0]] = 1
        # sort
        def dfs(num):
            for i in range(numCourses):
                if record[num][i]==1:
                    visited[num] = True
                    if visited[i]:
                        return False
                    else:
                        if not dfs(i):
                            return False
                        visited[num] = False
            return True

        for i in range(numCourses):
            if not dfs(i):
                return False
        return True

        


