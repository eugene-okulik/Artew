# Генератор для бесконечной последовательности чисел Фибоначчи
def fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b


fibonacci_gen = fibonacci()


# Функция для получения n-го числа из генератора
def fibonacci_number(n):
    number = None
    for _ in range(n):
        number = next(fibonacci_gen)
    return number


# Получение числа Фибоначчи для 5, 200, 1000 и 100000
fifth = fibonacci_number(10)
two_hundredth = fibonacci_number(200)
thousandth = fibonacci_number(1000)
# hundred_thousandth = fibonacci_number(100000)

print(f"Пятое число Фибоначчи: {fifth}")
print(f"Двухсотое число Фибоначчи: {two_hundredth}")
print(f"Тысячное число Фибоначчи: {thousandth}")
# print(f"Стотысячное число Фибоначчи: {hundred_thousandth}")
