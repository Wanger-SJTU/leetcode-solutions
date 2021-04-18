/*
 * @lc app=leetcode.cn id=743 lang=cpp
 *
 * [743] 网络延迟时间
 */

#include "leetcode.h"

// @lc code=start
class Solution
{
public:
  int networkDelayTime(vector<vector<int>>& times, int n, int k)
  {
    vector<vector<int>> graph(n + 1, vector<int>(n + 1, INT_MAX / 2));  // INT_MAX/2 防止溢出
    vector<int> dis_record(n + 1, INT_MAX / 2);  // dis_record 表示的是起始点k到当前下标节点的距离
    for (vector<int>& src_dst_dis : times) {
      int src = src_dst_dis[0];
      int dst = src_dst_dis[1];
      int dis = src_dst_dis[2];
      graph[src][dst] = dis;
    }

    for (int i = 1; i <= n; i++) {  //效率不高 但做法是对的
      dis_record[i] = graph[k][i];
    }

    dis_record[0] = 0;
    dis_record[k] = 0;

    //是否已经访问过了 记录
    vector<bool> visited(n + 1, false);
    visited[k] = true;  //实际上是过滤掉了 k-k这个路径

    //这里为什么到n-1 就结束呢？ 实际上只剩下n-1
    //个节点需要遍历了？为什么遍历n次就不行了？---对于N个节点的图，最短路径最多n-1条边，每次循环，至少
    for (int i = 1; i < n; i++) {
      //找到当前的最短路径 并初始化第一组邻接距离表格
      int min_dis = INT_MAX / 2;
      int min_dis_idx = 0;
      for (int j = 1; j <= n; j++) {  //找到当前最小的那个点
        if (dis_record[j] < min_dis && visited[j] == false) {
          min_dis = dis_record[j];
          min_dis_idx = j;
        }
      }

      if (min_dis == INT_MAX / 2) {  //没有办法找到最近的节点
        return -1;
      }
      visited[min_dis_idx] = true;

      for (int aa = 1; aa <= n; aa++) {  //更新距离操作
        if (graph[min_dis_idx][aa] != INT_MAX / 2 &&
            dis_record[aa] > dis_record[min_dis_idx] + graph[min_dis_idx][aa]) {
          dis_record[aa] = dis_record[min_dis_idx] + graph[min_dis_idx][aa];
        }
      }
    }

    int rst = *max_element(dis_record.begin(), dis_record.end());
    if (rst == INT_MAX / 2) {
      return -1;
    }
    return rst;
  }
};
// @lc code=end

int main() {}
