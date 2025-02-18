import os

file_path = 'homework/eugene_okulik/hw_13/data.txt'

try:
    if os.path.exists(file_path):
        with open(file_path, 'r') as file:
            content = file.read()
            print(content)
    else:
        print(f'Файл {file_path} не найден! ')
except FileNotFoundError:
    print(f'Файл {file_path} не найден! ')
except Exception as e:
    print(f'Произошла ошибка: {e}')
