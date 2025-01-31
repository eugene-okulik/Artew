def operation_select(func):
    def wrapper(first, second):
        if second == 0 and (first == second or first > second):
            return 'Деление на 0 невозможно.'

        if first == second and first < 0:
            operation = '*'
        elif first == second:
            operation = '+'
        elif first > second:
            operation = '-'
        else:  # Это будет случай, когда second > first
            operation = '/'

        return func(first, second, operation)
    return wrapper


@operation_select
def calc(first, second, operation):
    if operation == '/':
        return first / second
    elif operation == '+':
        return first + second
    elif operation == '-':
        return first - second
    elif operation == '*':
        return first * second
    else:
        return 'Неизвестная операция'


print(calc(5,3)) # 2
print(calc(2,2)) # 4
print(calc(1,0)) # Деление на 0
print(calc(2,10)) # 0.2
print(calc(-5,-5)) # 25


PRICE_LIST = '''тетрадь 50р
книга 200р
ручка 100р
карандаш 70р
альбом 120р
пенал 300р
рюкзак 500р'''

# dict comprehension

price_list = {line.split()[0]: int(line.split()[1][:-1])for line in PRICE_LIST.strip().split('\n')}

print(price_list)
