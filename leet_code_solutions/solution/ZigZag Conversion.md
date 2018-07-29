# Description

The string `"PAYPALISHIRING"` is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

```
P   A   H   N
A P L S I I G
Y   I   R
```

And then read line by line: `"PAHNAPLSIIGYIR"`

Write the code that will take a string and make this conversion given a number of rows:

```
string convert(string s, int numRows);
```

**Example 1:**

```
Input: s = "PAYPALISHIRING", numRows = 3
Output: "PAHNAPLSIIGYIR"
```

**Example 2:**

```
Input: s = "PAYPALISHIRING", numRows = 4
Output: "PINALSIGYAHRPI"
Explanation:

P     I    N
A   L S  I G
Y A   H R
P     I

n=4
P     I     N
A   L S   I G
Y A   H R
P     I

N=5
P              H
A          S   I
Y      I       R
P   L          I      G
A              N
```

很没有意思的一道题。就是找数学规律：

题目的意思是把字符串上下上下走之字形状,然后按行输出,比如包含数字0~22的字符串, 给定行数为5,走之字形如下:

[![image](https://images0.cnblogs.com/blog/517264/201405/201334051213000.png)](https://images0.cnblogs.com/blog/517264/201405/201334017621440.png)

现在要按行输出字符,即:0 8 16 1 7 9 15 17 2…….

如果把以上的数字字符看做是字符在原数组的下标, 给定行数为n = 5, 可以发现以下规律:

(1)第一行和最后一行下标间隔都是`interval = n*2-2 = 8 `; 

(2)中间行的间隔是周期性的,第$i$行的间隔是: `interval–2*i,  2*i,  interval–2*i, 2*i, interval–2*i, 2*i, …`

