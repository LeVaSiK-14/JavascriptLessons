# TODO INE

# def sumFunc(*args):
#     return sum(args)

# print(sumFunc(12, 10, 5))
# print(sumFunc(1,2,3,4,5,6,7,8))
# print(sumFunc(13, 15))


# TODO TWO

# def func(name, **kwargs):
#     return (name, kwargs)

# print(func('John', age=23, gender='male', favorite_sports=['football', 'tennis']))


# TODO THREE

# def func(lenght, kol):
#     list_ = [0 for i in range(1, kol+1)]
#     list_main = [list_ for j in range(1, lenght+1)]
#     print(list_main)

# func(3, 4)


# TODO FOUR

# def simple_numbers(number):
#     count = 0
#     dict_of_simple = dict()
#     dict_of_simple[1] = False
#     for first in range(2,number+1):                     # тут те самые нужные числа
#         for divisor in range(1,number+1):               # тут я их делю
#             if first % divisor == 0:                    # если без остатка, то +1
#                 count +=1                               # если делился не только на 1, то тру
#         if count > 2:
#             dict_of_simple[first] = False
#         else:
#             dict_of_simple[first] = True
#         count = 0
#     return dict_of_simple

# number = int(input("Введите число: "))
# print(simple_numbers(number))