# Даны числа x и y. Получить x − y / 1 + xy

x = float(input('Введите число x: '))
y = float(input('Введите число y: '))

z = (x - y) / 1 + x * y
print('Результат: (x - y) / 1 + x * y =', z)
