# size_array=int(input("Введите размер массива: "))
# fibanachi=[1,1]
# for i in range(2, size_array):
#     fibanachi.append(fibanachi[-2]+fibanachi[-1])
# print(fibanachi)

def fibanachi(number):
    if number == 1 or number == 2:
        return [1,1]
    fibanachi_list = fibanachi(number-1)
    fibanachi_list.append(fibanachi_list[-1]+fibanachi_list[-2])
    return (fibanachi_list)

num = int(input('Enter length array: '))
print(fibanachi(num))