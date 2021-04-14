/*
 * @lc app=leetcode.cn id=980 lang=cpp
 *
 * [980] 不同路径 III
 */
#include "leetcode.h"
// @lc code=start
class Solution
{
public:
  void dfs(vector<vector<int>>& grid, vector<vector<bool>>& visited, int& count, int i, int j,
           int total, int step)
  {
    if (i < 0 || i >= grid.size() || j < 0 || j > grid[0].size() || visited[i][j] ||
        grid[i][j] == -1) {
      return;
    }
    if (grid[i][j] == 2) {
      count = step == total ? count + 1 : count;
      return;
    }

    visited[i][j] = true;
    step++;
    dfs(grid, visited, count, i + 1, j, total, step);
    dfs(grid, visited, count, i, j + 1, total, step);
    dfs(grid, visited, count, i - 1, j, total, step);
    dfs(grid, visited, count, i, j - 1, total, step);
    step--;
    visited[i][j] = false;
  }

  int uniquePathsIII(vector<vector<int>>& grid)
  {
    int m = grid.size();
    int n = grid[0].size();
    int count = 0;
    vector<int> srt;
    int total_0 = 0;
    vector<vector<bool>> visited(m, vector<bool>(n));
    for (int i = 0; i < m; ++i) {
      for (int j = 0; j < n; ++j) {
        if (grid[i][j] == 1) {
          srt = {i, j};
          continue;
        }
        if (grid[i][j] == 0) {
          total_0++;
        }
      }
    }
    dfs(grid, visited, count, srt[0], srt[1], total_0 + 1, 0);
    return count;
  }
};
// @lc code=end
