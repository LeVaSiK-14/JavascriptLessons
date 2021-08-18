from datetime import datetime
from datetime import date

final_costs = dict()

band = {
        'members': {
            'freddy_mercury': {'role': 'singer', 'date': date(1956,12,21)},
            'nurbek_atabekov': {'role': 'drummer', 'date': date(1988,12,12)},
            'curt_cobein': {'role': 'drummer', 'date': date(1977,7,8)}
            },
        'concerts' : {
            'london':  {'concert_date': date(2021,12,31), 'expenses': [142,123,41,142,531], 'income': 10000},
            'bishkek': {'concert_date': date(2021,12,31), 'expenses': [142,123,41,142,531], 'income': 10000}
            }
}

def update_person():
    update_user_person = dict()
    name = input("Введите имя которое нужно заменить/добавить: ")
    name = name.replace(" ", '_').strip("_").lower()
    print(name)
    user_date = input("Введите его дату рождения: (напр.1999 12 31)")
    user_date = user_date.replace(" ", ',').strip(",").split(",")
    print(user_date, type(user_date))
    year, month, day = map(int, user_date)
    user_date = date(year,month,day)
    role = input("Введите его роль в группе: ")
    role = role.replace(" ", '').lower()
    update_user_person[name] = {'role' : role, 'date' : user_date}
    print(update_user_person)
    band['members'].update(update_user_person)
    print(band['members'])

def update_concert():
    update_user_concert = dict()
    name = input("Введите название концерта который нужно заменить/добавить: ")
    name = name.replace(" ", '_').strip("_").lower()
    print(name)
    user_date = input("Введите его дату: (напр.12 31)")
    user_date = user_date.replace(" ", ',').strip(",").split(",")
    month, day = map(int, user_date)
    user_date = date(21,month,day)
    zat_v_conc = input("Введите все затраты")
    b = [i for i in zat_v_conc if not '0'<=i<='9']
    print(b)
    for index_of_letter in b:
        zat_v_conc = zat_v_conc.replace(index_of_letter, " ")
    print(zat_v_conc)
    zat_v_conc = zat_v_conc.split(" ")
    print(zat_v_conc)
    zat_v_conc = [x for x in zat_v_conc if x]
    print(zat_v_conc)
    zat_v_conc = list(map(int,zat_v_conc))
    print(zat_v_conc)
    update_user_concert[name] = {'concert_date' : user_date, 'expenses' : zat_v_conc}
    band['concerts'].update(update_user_concert)
    print(band['concerts'])

print("Это прога для менеджера группы")
print('''можешь ввести одну из следующих команд, -\n)
    1)update member, update concert\n
    2)delete concert, delete member\n
    3)concert go\n
    4)list, list of members, list of concerts 
     ''')
dict_of_expanses = dict()
while True:
    
    a = input("").lower()
    a = a.replace(" ", '_').strip("_").lower()
    # a = a.strip("_")
    print(a)
    if a == 'update_member':
        update_person()
        print("Список всех участников: ", end="")
        print(*band['members'].keys(), sep=", ")
    elif a == 'concert_go':
        for index in band['concerts'].keys():
            print(f"Вы провели концерт в {index}")
            name = input("Введите цель траты")
            zat_v_conc = input("Введите все затраты")
            b = [i for i in zat_v_conc if not '0'<=i<='9']
            print(b)
            for index_of_letter in b:
                zat_v_conc = zat_v_conc.replace(index_of_letter, " ")
            print(zat_v_conc)
            zat_v_conc = zat_v_conc.split(" ")
            print(zat_v_conc)
            zat_v_conc = [x for x in zat_v_conc if x]
            print(zat_v_conc)
            zat_v_conc = sum(list(map(int,zat_v_conc)))
            print(zat_v_conc)
            final_costs[index] = zat_v_conc
            band['concerts'][index]['income'] -= zat_v_conc
            print(band['concerts'][index]['income'])
        print("1) название города в котором был концерт, 2) чистый доход")
        print(final_costs)
    elif a == 'list':
        print(band)
    elif a == 'list_of_members':
        print(band['members'])
    elif a == 'list_of_concerts':
        print(band['concerts'])
    elif a == 'delete_concert':
        name = input("введите название удаляемого концерта")
        name = name.replace(" ", '_').strip("_").lower()
        if name in band['concerts'].keys():
            del band['concerts'][name]
        else:
            print("Вы ввели неверно название концерта, проверьте лист концертов и попробуйте снова")
    elif a == 'delete_member':
        name = input("введите имя удаляемого участника")
        name = name.replace(" ", '_').strip("_").lower()
        if name in band['members'].keys():
            del band['members'][name]
        else: 
            print("Вы ввели неверно имя участника, проверьте лист участников и попробуйте снова")



return_members()