# number = int(input('Введите натуральное число: '))
# summ = 0

# while number > 0:
#     digit = number % 10
#     summ = summ + digit
#     number = number // 10

# print("Сумма:", summ)

def digits_sum(num):
    return sum([int(x) for x in num ])
num = input('Введите натуральное число: ')
print(digits_sum(num))