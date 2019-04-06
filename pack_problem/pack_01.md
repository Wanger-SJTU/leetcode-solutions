
# 背包九讲-01
[背包九讲](https://github.com/tianyicui/pack)的阅读笔记。

注：公式不能正确显示。但是在本地可以显示，也可查看上面的连接。

## 01背包
有 $N$ 件物品和一个容量为 $V$ 的背包。放入第 $i$ 件物品耗费的费用是 $C_i^1$，得到的价值是 $W_i$。求解将哪些物品装入背包可使价值总和最大。

最基础的背包问题，特点是：每种物品仅有一件，可以选择放或不放。
用子问题定义状态：即 $F [i, v]$ 表示前 $i$ 件物品恰放入一个容量为 $v$ 的背包可以获得
的最大价值。则其状态转移方程便是：

$$F[i,v]=\max \{F[i−1;v], F[i−1;v−C_i] + W_i \} $$

将前 $i$ 件物品放入容量为 $v$ 的背包中”这个子问题，若只考虑第 $i$ 件物品的策略（放或不放），那么就可以转化为一个只和前 $i−1$ 件物品相关
的问题。如果不放第 $i$ 件物品，那么问题就转化为“前 $i−1$ 件物品放入容量为 $v$ 的背包中”，价值为 $F[i−1,v]$；如果放第 $i$ 件物品，那么问题就转化为“前 $i−1$ 件物品放入剩下的容量为 $v−C_i$ 的背包中”，此时能获得的最大价值就是 $F[i−1,v−C_i]$ 再加上通过放入第 $i$ 件物品获得的价值 $W_i$。


```python
# python code no optimization
import numpy as np

def DP_01pack(value, weight, num, capacity):
    res = [[0 for i in range(capacity+1)] for j in range(num+1)]
    for i in range(1, num+1):#put i_th item
        for j in range(1, capacity+1):
            if weight[i-1] <= j:#if could be put in bag
                res[i][j] = max(res[i-1][j], (res[i-1][j-weight[i-1]] + value[i-1]))
            else:
                res[i][j] = res[i-1][j]
    return res
```


```python
def show(num, capacity, weight, res):  
    print('max value:',res[num][capacity])  
    x=[False for i in range(num)]  
    j=capacity
    for i in range(n, 0, -1):  
        if res[i][j] > res[i-1][j]:  
            x[i-1]=True  
            j -= w[i-1]  
    print('the result is:')
    print(x)
    for i in range(num):  
        if x[i]:  
            print(str(i+1)+'\t')  
```


```python
n = 6
weight = 10
w=[2,2,3,1,5,2]
v=[2,3,1,5,4,3]
result = DP_01pack(v,w,n,weight)
show(n, weight, w, result)
print(np.array(result))
```

    max value: 15
    the result is:
    [False, True, False, True, True, True]
    2	
    4	
    5	
    6	
    [[ 0  0  0  0  0  0  0  0  0  0  0]
     [ 0  0  2  2  2  2  2  2  2  2  2]
     [ 0  0  3  3  5  5  5  5  5  5  5]
     [ 0  0  3  3  5  5  5  6  6  6  6]
     [ 0  5  5  8  8 10 10 10 11 11 11]
     [ 0  5  5  8  8 10 10 10 12 12 14]
     [ 0  5  5  8  8 11 11 13 13 13 15]]


## 优化空间复杂度
以上方法的时间和空间复杂度均为 $O(VN)$，其中时间复杂度应该已经不能再优化了，但空间复杂度却可以优化到 $O(V)$。
上面的状态转移递推式为

$$F [i; v] = \max \{F [i − 1; v]; F [i − 1; v − C_i] + W_i\}$$
可以为
$$F[v]= max\{F[v]; F[v − C_i] + W_i\}$$

其中的$F[v]=max\{F[v],F[v-c[i]+W_i\}$一句恰就相当于我们的转移方程$f[i][v]=max\{f[i-1][v],f[i-1][v-c[i]]\}$，因为现在的$f[v-c[i]]$就相当于原来的$f[i-1][v-c[i]]$。


```python
def pack01(value, weight, num, capacity):
    F = [0 for i in range(capacity+1)]
    for i in range(num):
        for j in range(1,capacity+1):
            if j >= weight[i]:
                F[j] = max(F[j-1], F[j - weight[i]]+value[i])             
            else:
                F[j] = F[j-1]
    return F
```


```python
n = 6
weight = 10
w=[2,2,3,1,5,2]
v=[2,3,1,5,4,3]
result = pack01(v,w,n,weight)
print(result)
```

    [0, 0, 3, 3, 6, 6, 9, 9, 12, 12, 15]



要求**恰好装满背包**，那么在初始化时除了 $F[0]$ 为 $0$，其它$F[1::V]$ 均设为 $−1$，这样就可以保证最终得到的 $F[V ]$ 是一种恰好装满背包的最优解。

初始化的 $F$ 数组事实上就是在没有任何物品可以放入背包时的合法状态。如果要求背包恰好装满，那么此时只有容量为 0 的背包可以在什么也不装且价值为 0 的情况下被“恰好装满”，其它容量的背包均没有合法的解，属于未定义的状态，应该被赋值为 $-\infty$ 了。如果背包并非必须被装满，那么任何容量的背包都有一个合法解“什么都不装”，这个解的价值为 0，所以初始时状态的值也就全部为 0了

# 一个常数优化
上面伪代码中的
```
for i from 1 to N
    for v from V to C_i
```
中第二重循环的下限可以改进。它可以被优化为
```
for i 1 to N
    for v V to max(V − ΣN_i W_i; C_i)
```
这个优化之所以成立的原因请读者自己思考。（提示：使用二维的转移方程思考较易。）
