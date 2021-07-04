per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
money = input("Введите сумму планируемого вклада: ")
m = int(money)
p = list(map(float, per_cent.values()))
depos = [i*(m/100.0) for i in p]
deposit = list(map(int, depos))
print(deposit)
print('Максимальная сумма, которую вы можете заработать —', max(deposit))
