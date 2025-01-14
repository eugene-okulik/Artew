# Последовательность от 1 до 100

for number in range(1, 101):
    if number % 3 == 0 and number % 5 == 0:
        print('FuzzBuzz')
    elif number % 3 == 0:
        print('Fuzz')
    elif number % 5 == 0:
        print('Buzz')
    else:
        print(number)
