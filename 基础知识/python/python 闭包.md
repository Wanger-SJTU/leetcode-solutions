
>关于什么是python闭包（Closures），可以参考[这篇博客](https://foofish.net/python-closure.html)

这个文章呢，是从python闭包，引用外部变量说起，简单介绍一下python的变量绑定机制。
首先我们先看一下下面两段代码：

**code1**

```python
def func():
    aa = [123]
    def func2():
        aa.append([12])
        print(aa)
    return func2
```
**code2**
```python
def func():
    aa = [123]
    def func2():
        aa+=[12]
        print(aa)
    return func2
```
现在问题来了，如果调用一下上面定义的两段函数。会有什么结果呢？
```python
if __name__ == "__main__":
    a = func()
    a()
```
答案就是
>第一段可以正常运行，而第二段代码则会报错。

错误信息为
```python
UnboundLocalError: local variable 'aa' referenced before assignment
```
*注：*
>如果试图去修改，即在函数内部试图改变函数外部声明的值，那就得用global和nonlocal关键字了。

## 分析
我们知道，在定义闭包时候，`inner function`是可以“看到” `outer function` 中定义的变量的。`code1` 中成功运行的代码也说明了这一点。
但是 `code2` 与 `code1` 中的**区别**就在于，`code2` 中是对变量有赋值动作的，而 `code1`是没有的。这很可能就是造成报错的原因。

这个牵扯到python 变量名的查找机制。在介绍之前，我们先进行下面的一个实验：

```python
def func3():
    aa = [1,]
    print(aa)
    print(id(aa))
    def func():
        aa=[1,]
        aa += [2]
        print(id(aa))
        print(aa)
    return func
if __name__ == "__main__":
    a = func3()
    a()
    func3()
```

输出为：
```python
[1]
1935268733448

1935268733448
[1, 2]

[1]
1935268733448
```

## 解决方法
