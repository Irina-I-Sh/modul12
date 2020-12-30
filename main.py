money = int(input('Введите сумму вклада '))
per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
plist = list(per_cent.values())
deposit = [money * float(plist[0]) / 100, money * float(plist[1]) / 100, money * float(plist[2]) / 100, money * float(plist[3]) / 100]
print('Накопленные средства за год вклада в каждом из банков:', deposit)
print('Максимальная сумма, которую вы можете заработать - ', max(deposit))