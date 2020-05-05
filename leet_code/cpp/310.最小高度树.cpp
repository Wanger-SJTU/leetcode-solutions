/*
 * @lc app=leetcode.cn id=310 lang=cpp
 *
 * [310] 最小高度树
 */
#include "common.h"

class Solution {
 public:
  vector<int> findMinHeightTrees(int n, vector<vector<int>>& edges) {
    vector<unordered_set<int>> graph;
    for (auto edge : edges) {
      graph[edge[0]].insert(edge[1]);
      graph[edge[0]].insert(edge[1]);
    }
    vector<int> parents, child;
    for (int i = 0; i < n; i++) {
      if (graph[i].size() == 1) {
        parents.push_back(i);
      }
    }
    while (true) {
      for (int node : parents) {
        for (int neighbour : graph[node]) {
          graph[neighbour].erase(node);
          if (graph[neighbour].size() == 1)  // new leaf after removing the edge
            child.push_back(neighbour);
        }
        graph[node].clear();
      }
      if (child.empty()) {
        return parents;  // this was the last level of leaf left
      }
      parents = child;
      child.clear();
    }
  }
};

// @lc code=start
class Solution {
 public:
  vector<int> findMinHeightTrees(int n, vector<vector<int>>& edges) {
    if (n == 1) {
      return {0};
    }
    if (n == 2) {
      return {0, 1};
    }

    vector<int> indegree(n);
    vector<unordered_set<int>> graph(n);

    for (auto edge : edges) {
    }
  }
};
// @lc code=end
