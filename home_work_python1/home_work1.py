# Вводим числа
num1 = int(input('Enter number: '))
num2 = int(input('Enter number: '))
num3 = int(input('Enter number: '))
num4 = int(input('Enter number: '))
num5 = int(input('Enter number: '))
num6 = int(input('Enter number: '))

# Вычисляем сумму всех чисел
summ = num1+num2+num3+num4+num5+num6
# Вычисляем произведение всех чисел
composition = num1*num2*num3*num4*num5*num6
# Вычисляем среднее орифметическое чисел
middle = (num1+num2+num3+num4+num5+num6)/6
# Выводим ответы
print(summ)
print(composition)
print(round(middle, 2))