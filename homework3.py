# TODO ONE

# list_ = [5, 3, 8, 13, 5, 6, 8, 15, 13, 5, 5, 8]
# a = set(list_)
# d = (list(a))
# c = (list(a))
# c.append(d)
# print(c)


# TODO TWO

# magazine = {
#     'Levasik': [95, 100, 85, 100, 70],
#     'Radmir': [100, 50, 100, 80, 100],
#     'Hamza': [95, 30, 100, 100, 70],
#     'Dastan': [100, 100, 100, 90, 10],
#     'Aziz': [10, 40, 85, 95, 100],
#     'Alisher': [45, 55, 100, 100, 100],
#     'Mila': [100, 100, 100, 100, 100]
# }
# list_all = []
# for keys, values in magazine.items():
#     middle = (keys, sum(values)/5)
#     list_all = list_all+(list(middle))
# nums = []
# for i in range(len(list_all)):
#     if i % 2 != 0:
#         nums.append(list_all[i])
# for i in range(len(nums)):
#     for j in range(len(nums)-i-1):
#         if nums[j] > nums[j+1]:
#             nums[j], nums[j+1] = nums[j+1], nums[j]

# better_rating = (nums[-1])
# l = iter(list_all)
# dict_all = (dict(zip(l, l)))
# better_student = (list(dict_all.keys())[list(dict_all.values()).index(better_rating)])
# answer = (f'Лучший студент {better_student} набрал(a) {better_rating} баллов')
# print(answer)


# TODO THREE

# users = {'admin': 'pass123', 'Jack': 'super007', 'Adele': 'singer1995'}
# attempts = 0
# while attempts != 3:
#     username = input('Enter username: ')
#     password = input('Enter password: ')

#     attempts += 1
#     if username in users:
#         if users[username] == password:
#             print(f'Hello, {username}!')
#             break
#         else:
#             print('ERROR.....\nInvalid password\nTry again')
#     else:
#         if attempts == 3:
#             print('Attemps is finish( ')
#             continue
#         print('ERROR.....\nInvalid login\nTry again!')

