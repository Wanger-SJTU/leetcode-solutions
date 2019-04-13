
'''
单位1的埃及分数分解问题：

最近流行套路白富美数学题征婚，我也来出一个题目很简单的数学题，
有本事的数学爱好者和IT男、IT女可以来试试。
埃及分数是指分子是1的分数，也叫单位分数。
古代埃及人在进行分数运算时。只使用分子是1的分数。
因此这种分数也叫做埃及分数，或者叫单分子分数。单位分数分解很有意思。

1的单位分数分解很容易解答也很多，
但我们加强一下，要求其中一项是所有其它项的乘积，
就是求 ∑1/ai+1/Πai=1的整数解。
比如1=1/2+1/3+1/(2*3)，
1=1/2+1/3+1/7+1/(2*3*7)，
所以{2,3}、｛2，3，7｝就是要求的两组解。
现在如果谁求出一个不包含偶数的解，我可以个人奖励1000元，
帮忙推荐等，可以邮件联系yuange1975@hotmail.com。

ref:
1. http://www.wikiwand.com/zh-sg/%E5%8F%A4%E5%9F%83%E5%8F%8A%E5%88%86%E6%95%B8
'''
eps=1e-15
def sum(nums):
    res = 0
    for item in nums:
        res += 1/item
    return res

def frac1():
    base = 2
    second = [3]
    res = [base]
    while True:
        step = second[-1]
        while 1 - sum(res) > eps:
            while step%2==0:
                step += 1
            if step > 1e15:
                return
            tmp_sum = sum(res)
            while tmp_sum+1/step >1:
                step+=1
            res.append(step)
        if 1 - sum(res) < eps:
            print(res)
            second.append(res[1])
        res = [base]

if __name__ == "__main__":
    frac1()


