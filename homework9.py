sum_of_depozit = int(input('Введите сумму депозита: '))
srok = int(input('Введите на сколько периодов: '))
percent = int(input('Введите под какой процент: '))

percent = percent/100


for i in range(1, srok+1):
    sum_of_depozit = (percent/12*sum_of_depozit) +sum_of_depozit
    print(sum_of_depozit) 