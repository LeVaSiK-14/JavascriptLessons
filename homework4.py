# TODO ONE

# accounts = {'John': 'john123', 'Alice': 'supagirl1995', 'Charles': 'coolguy69'}

# def change(acc):
#     saved_accounts = dict()
#     for name in acc:
#         password = acc[name]
#         new_password = []
#         for letter in password:
#             a = chr(ord(letter)+5)
#             new_password.append(a)
#         new_line = (''.join(new_password))
#         saved_accounts[name] = new_line
#     return saved_accounts

# hash_password = (change(accounts))
# print(hash_password)

# def decodes(acc):
#     decode_accounts = {}
#     for name in acc:
#         password = acc[name]
#         new_password = []
#         for letter in password:
#             a = chr(ord(letter)-5)
#             new_password.append(a)
#         new_line = (''.join(new_password))
#         decode_accounts[name] = new_line
#     return decode_accounts

# print(decodes(hash_password))



# attempts = 0
# while attempts != 3:
#     username = input('Enter username: ')
#     password = input('Enter password: ')

#     attempts += 1
#     if username in hash_password:
#         if hash_password[username] == password:
#             print(f'Hello, {username}!')
#             break
#         else:
#             print('ERROR.....\nInvalid password\nTry again')
#     else:
#         if attempts == 3:
#             print('Attemps is finish( ')
#             continue
#         print('ERROR.....\nInvalid login\nTry again!')


# TODO TWO (1)

# new_list = []
# def funk(list_):
#     i = 0
#     while i < 20:
#         i += 1
#         if i % 2 == 0:
#             list_.append(i)
#     return(list_)
# print(funk(new_list))


# TODO TWO (2)

# new_string = ''
# vowels = 'aioue'

# def funk2(stroke, vow):
#     index = 0
#     text = 'Hello world'
#     while index < len(text):
#         if text[index] not in vow:
#             stroke += text[index]
#         index += 1
#     return(stroke)
# print(funk2(new_string, vowels))


# TODO TWO (3)

# def funk3():
#     new_dict = {}
#     i = -2
#     while i < 48:
#         i += 2
#         if i % 3 == 0 and i % 5:
#             new_dict[i] = 'FooBar'
#         elif i % 3 == 0:
#             new_dict[i] = 'Foo'
#         elif i % 5 == 0:
#             new_dict[i] = 'Bar'
#     print(new_dict)
# funk3()