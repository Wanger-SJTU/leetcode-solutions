/*
 * @lc app=leetcode.cn id=1293 lang=cpp
 *
 * [1293] 网格中的最短路径
 */
#include "common.h"
// @lc code=start
class Solution {
public:
  vector<vector<int>> visited;
  bool isValid(int x, int y, int m, int n, int currK) {
    if (x < 0 || y < 0 || x >= m || y >= n) {
      return false;
    } else {
      if (visited[x][y] > currK) {
        visited[x][y] = currK;
        return true;
      } else {
        return false;
      }
    }
  }
  int shortestPath(vector<vector<int>> &grid, int k) {
    int m = grid.size();
    int n = grid[0].size();
    queue<pair<pair<pair<int, int>, int>, int>> q;
    visited.resize(m, vector<int>(n, INT_MAX));
    q.push(make_pair(make_pair(make_pair(0, 0), 0), 0));
    int dir_x[4] = {-1, 1, 0, 0};
    int dir_y[4] = {0, 0, 1, -1};
    if (grid[0][0] == 0) {
      visited[0][0] = 0;
    } else {
      visited[0][0] = 1;
    }
    while (!q.empty()) {
      pair<pair<pair<int, int>, int>, int> p = q.front();
      q.pop();
      pair<pair<int, int>, int> p1 = p.first;
      pair<int, int> dir = p1.first;
      int currK = p1.second;
      int x = dir.first;
      int y = dir.second;
      int steps = p.second;
      // cout << x << " " << y << " " << currK <<  " " << steps << endl;
      if (x == m - 1 && y == n - 1) {
        return steps;
      }
      for (int i = 0; i < 4; i++) {
        int new_x = x + dir_x[i];
        int new_y = y + dir_y[i];
        if (isValid(new_x, new_y, m, n, currK)) {
          if (grid[new_x][new_y] == 1) {
            if (currK < k) {
              q.push(make_pair(make_pair(make_pair(new_x, new_y), currK + 1),
                               steps + 1));
            }
          } else {
            q.push(make_pair(make_pair(make_pair(new_x, new_y), currK),
                             steps + 1));
          }
        }
      }
    }
    return -1;
  }
};
// @lc code=end
