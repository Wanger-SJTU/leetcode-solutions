/*
 * @lc app=leetcode.cn id=478 lang=cpp
 *
 * [478] 在圆内随机生成点
 */

#include "leetcode.h"

// @lc code=start
class Solution
{
private:
  double rad, xc, yc;
  //c++11 random floating point number generation
  mt19937 rng{random_device{}()};
  uniform_real_distribution<double> uni{0, 1};

public:
  Solution(double radius, double x_center, double y_center)
      : rad(radius), xc(x_center), yc(y_center)
  {}

  vector<double> randPoint()
  {
    double d = rad * sqrt(uni(rng));
    double theta = uni(rng) * (2 * M_PI);
    return {d * cos(theta) + xc, d * sin(theta) + yc};
  }
};

/**
 * Your Solution object will be instantiated and called as such:
 * Solution* obj = new Solution(radius, x_center, y_center);
 * vector<double> param_1 = obj->randPoint();
 */
// @lc code=end

int main() {}
