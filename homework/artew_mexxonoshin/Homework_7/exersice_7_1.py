number = 7  # Загаданная цифра

while True:
    guess_user_number = input('Угадай цифру от 0 до 9 или введите "exit" для выхода: ')
    if guess_user_number.lower() == 'exit':
        print('Вы НЕугадайка!')
        break
    if not guess_user_number.isdigit():
        print("Вы ввели не цифру, пжлста, введите цифру от 0 до 9: ")
        continue
    guess_user_number = int(guess_user_number)
    if not 0 <= guess_user_number <= 9:
        print('Введите цифру от 0 до 9: ')
        continue
    if guess_user_number == number:
        print('Вы угадали!')
        break

print('Спасибо за участие')
