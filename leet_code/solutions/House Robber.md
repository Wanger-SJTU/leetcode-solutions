You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security system connected and it will automatically contact the police if two adjacent houses were broken into on the same night.

> 相邻的两个房子一个晚上内被偷，讲触发报警。

Given a list of non-negative integers representing the amount of money of each house, determine the maximum amount of money you can rob tonight without alerting the police.
> 输入为非负元素的列表，其中元素表示每家的金额。输出为一夜可以偷到的最大数目的金钱。

>Example 1:
>	Input: [1,2,3,1]
>	Output: 4
>
>Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
>             Total amount you can rob = 1 + 3 = 4.
>Example 2:
>
>​	Input: [2,7,9,3,1]
>​	Output: 12
>Explanation: Rob house 1 (money = 2), rob house 3 (money = 9) and rob house 5 (money = 1).
>​             Total amount you can rob = 2 + 9 + 1 = 12.



这个题目实际上就是数组非连续元素求最大值。考虑使用动态规划的方法求解。

首先找到递归方程。 

$$
F(n) = \max(F(n-2)+v_n, F(n-1))
$$

初始化条件，$F(1)=v_1, \quad F(2)=\max(v_1,v_2)$

代码：

```python
class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        if len(nums) <=2:
            return max(nums)
        result = [0,0]
        result[0] = nums[0]
        result[1] = max(nums[0], nums[1])
        for idx, item in enumerate(nums[2:]):
            value = max(result[idx]+item, result[idx+1])
            result.append(value)
        return result[-1]
```