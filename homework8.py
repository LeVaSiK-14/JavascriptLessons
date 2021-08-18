def funct(*args):
    list_ = list()
    for i in args:
        func_l = lambda i: list_.append(i) if i%2==0 and i%3==0 else False
        func_l(i)
    print(list_)

funct(1, 3, 6, 6,5,7,2,8,6,2,876, 36,6,8)


func = lambda a: a*2
print(func(4))

func1 = lambda a, b: a**b
print(func1(2, 4))

func3 = lambda *args: sum(args)
print(func3(3, 6, 1, 5, 15, 6, 4))