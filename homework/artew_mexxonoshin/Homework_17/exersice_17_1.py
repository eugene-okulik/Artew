import os
import argparse


# Поиск текста в файле
def find_text_in_file(correct_file_path, search_text, verbose):
    search_result = []  # Здесь будем хранить результат поиска
    search_text_lower = search_text.lower()  # Приводим текст для поиска к нижнему регистру
    if verbose:
        print(f"Начало поиска '{search_text}' в файле {correct_file_path}")
        with open(correct_file_path, 'r', encoding='utf-8') as file:  # Построчное чтение файла
            for line_number, line in enumerate(file, start=1):  # Номер для каждой строки
                if search_text_lower in line.lower():  # Есть ли текст в строке и приводим к нижнему регистру
                    # Добавляем инфо файл, № строки, и саму строку
                    search_result.append((correct_file_path, line_number, line.strip()))
                    if verbose:
                        print(f"Найден '{search_text}', в {correct_file_path}, в строке {line_number}: {line.strip().split()}")
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
                correct_file_path = os.path.join(dirpath, filename)  # Полный путь к файлу
                search_result = find_text_in_file(correct_file_path, search_text, verbose)  # Поиск текста в файле
                all_results.extend(search_result)  # Добавляем найденное в общий список

    if all_results:
        print("\nРезультаты поиска:")
        for correct_file_path, line_number, line in all_results:
            print(f"Файл: {correct_file_path}, Номер строки: {line_number}, Лог: {line}")
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
