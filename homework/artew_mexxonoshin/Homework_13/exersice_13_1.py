import os
import datetime


# print(os.path.dirname(__file__))

base_path = os.path.dirname(__file__)
# file_path = f'{base_path}/data.txt'
# file_path = os.path.join(base_path, 'data.txt')
# print(file_path)

homework_path = os.path.dirname(os.path.dirname(base_path))
eugene_okulik_file_path = os.path.join(homework_path, 'eugene_okulik', 'hw_13', 'data.txt')
print(eugene_okulik_file_path)

try:
    with open(eugene_okulik_file_path, 'r') as eugene_okulik_file:
        data = eugene_okulik_file.read()
    print("Содержимое файла:")
    print(data)
except FileNotFoundError:
    print("Файл не найден. Проверьте путь к файлу.")
except Exception as e:
    print(f"Произошла ошибка: {e}")

print('-------------------------------')

# Исходная дата + 7 дней
date_str_1 = "2023-11-27 20:34:13.212967"
date_1 = datetime.datetime.strptime(date_str_1, "%Y-%m-%d %H:%M:%S.%f")
days_to_add = 7
new_date_1 = date_1 + datetime.timedelta(days=days_to_add)
formatted_date = new_date_1.strftime("%Y-%m-%d %H:%M:%S.%f")

print(f"1. {formatted_date} - Дата на неделю больше от исходной {date_str_1}")

# Получение названия дня недели
date_str_2 = "2023-07-15 18:25:10.121473"
date_obj = datetime.datetime.strptime(date_str_2, "%Y-%m-%d %H:%M:%S.%f")
day_of_week = date_obj.strftime("%A")

print(f"2. {date_str_2} - 15 июля 2023 года — это {day_of_week}")

# Сколько дней с указанной даты
date_str_3 = "2023-06-12 15:23:45.312167"
date_obj_3 = datetime.datetime.strptime(date_str_3, "%Y-%m-%d %H:%M:%S.%f")
current_date = datetime.datetime.now()
difference = current_date - date_obj_3
days_ago = difference.days

print(f"3. {date_str_3} - была {days_ago} дней назад")
