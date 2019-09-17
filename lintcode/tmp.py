

def func0():
    aa = [123]
    def func2():
        aa.append([12])
        print(aa)
    return func2

def func1():
    aa = [123]
    def func2():
        aa+=[12]
        print(aa)
    return func2

def func3():
    aa = [1,123]
    print(aa)
    print(id(aa))
    def func():
        aa=[1,123,213]
        aa += [2]
        print(id(aa))
        print(aa)
    return func
if __name__ == "__main__":
    a = func3()
    a()
    func3()
