import os
import argparse


base_path = os.path.dirname(__file__)
homework_path = os.path.dirname(os.path.dirname(base_path))
logs_directory = os.path.join(homework_path, 'eugene_okulik', 'data', 'logs')
# logs_directory = os.path.join(homework_path, 'eugene_okulik', 'data', 'logs', 'rpe-api-error.2022-02-03.0.log')
print(logs_directory)

# Список ожидаемых файлов
logs_files = [
    'rpe-api-error.2022-02-03.0.log',
    'rpe-api-error.2022-02-03.1.log',
    'rpe-api-error.2022-02-03.2.log',
    'rpe-api-error.2022-02-03.3.log',
    'rpe-api-error.2022-02-03.4.log',
    'rpe-api-error.2022-02-03.5.log',
    'rpe-api-error.2022-02-03.6.log',
    'rpe-api-error.2022-02-03.7.log',
    'rpe-api-error.2022-02-03.8.log',
    'rpe-api-error.2022-02-03.9.log',
]

# Файлы которые не найдены
lost_files = []

for logs_file in logs_files:
    file_path = os.path.join(logs_directory, logs_file)
    if not os.path.isfile(file_path):
        lost_files.append(logs_file)

if lost_files:
    print("Следующие файлы недоступны:")
    for lost_file in lost_files:
        print(lost_file)
else:
    print("Все файлы доступны")

print('-' * 25)

# Поиск текста в файле
def find_text_in_file(file_path, search_text, verbose):
    search_result = []  # Здесь будем хранить результат поиска
    if verbose:
        print(f"Начало поиска '{search_text}' в файле {file_path}")
        with open(file_path, 'r', encoding='utf-8') as file:  # Построчное чтение файла
            for line_number, line in enumerate(file, start=1):  # Номер для каждой строки
                if search_text in line:  # Есть ли текст в строке
                    search_result.append((file_path, line_number, line.split()))  # Добавляем инфо файл, № строки, и саму строку
                    if verbose:
                        print(f"Найден '{search_text}', в {file_path}, в строке {line_number}: {line.split()}")
    if search_result:
        print("Поиск завершен. Найденные результаты:")
    else:
        print("Поиск завершен. Результаты не найдены.")
    return search_result


def main(directory, search_text, verbose=False):
    if not os.path.isdir(directory):
        print(f"Ошибка путь к директории {directory} не найден. ")
        return

    all_results = []
    for dirpath, _, filenames in os.walk(directory):
        for filename in filenames:
            if filename.endswith('.log'):
                file_path = os.path.join(dirpath, filename)  # Полный путь к файлу
                search_result = find_text_in_file(file_path, search_text, verbose)  # Поиск текста в файле
                all_results.extend(search_result)  # Добавляем найденное в общий список

    if all_results:
        print("\nРезультаты поиска:")
        for file_path, line_number, line in all_results:
            print(f"Файл: {file_path}, Номер строки: {line_number}, Лог: {line}")
    else:
        print("Ничего не найдено.")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Поиск текста в логах')
    parser.add_argument('directory', type=str, help='Путь к директории с логами')
    parser.add_argument('search_text', type=str, help='Текст для поиска')
    parser.add_argument('--verbose', action='store_true', help='Подробный вывод результатов')

    args = parser.parse_args()
    main(args.directory, args.search_text, args.verbose)

# python exersice_17_1.py -h
# python exersice_17_1.py /Users/qa/project/first_pro_github/Artew/homework/eugene_okulik/data/logs "error" --verbose