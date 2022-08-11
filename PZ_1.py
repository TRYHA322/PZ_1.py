# Задание №1
i = 1
a = 'Строка'
print(i, a)
b = int(input('Введите число'))
print(b)
c = input('Введите строку')
print(c)
# Задание №2
time = int(input('Введите время в секундах: '))
sec = time % 60
hour = time // 3600
mint = (time - hour*3600 - sec) // 60
print('{}:{}:{}'.format(hour, mint, sec))
# Задание №3
n = input('Введите число: ')
print(int(n)+int(n+n)+int(n+n+n))
# Задание №4
num = int(input('Введите число: '))
big = 0
b = len(str(num))
while b != 0:
    a = num % 10
    num = num//10
    if a > big:
        big = a
    b -= 1
print(big)
# Задание №5
rev = int(input('Введите прибыль: '))
costs = int(input('Введите издержки: '))
if rev > costs:
    print('Прибыль')
else:
    print('Убыток')
# Задание №6
rev = int(input('Введите прибыль: '))
costs = int(input('Введите издержки: '))
if rev > costs:
    print('Рентабельность выручки: {}'.format((rev - costs) / rev))
    pers = int(input('Введите числиность сотрудников: '))
    print('Прибыль на одного сотрудника: {}'.format((rev-costs) / pers))
else:
    print('Убыток')
# Задание №7
a = int(input('Результат в первый день: '))
b = int(input('Необходимый результат: '))
c = 1
while a < b:
    c += 1
    a = 1.1 * a
print('На {}-й день результат достигнет не менее {} км'.format(c , b))



