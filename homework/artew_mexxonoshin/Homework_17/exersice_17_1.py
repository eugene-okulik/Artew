import os
import argparse
import glob

parser = argparse.ArgumentParser(description='Поиск текста в логах')
parser.add_argument('directory', type=str, help='Путь к директории с логами')
parser.add_argument('search_text', type=str, help='Текст для поиска в лог-файлах')

args = parser.parse_args()


# Поиск текста в файле
def get_context(input_string, search_text, log_size=4):
    word_list = input_string.split()

    if search_text in word_list:
        found_index = word_list.index(search_text)
        # Определяем начальный и конечный индексы
        left_start = max(0, found_index - log_size)
        right_end = min(len(word_list), found_index + log_size + 1)
        # Возвращаем строку с логом
        return " ".join(word_list[left_start:right_end])
    return None

# Поиск всех .log файлов в указанной директории
log_files = glob.glob(os.path.join(args.directory, "*.log"))

if not log_files:
    print(f"В директории {args.directory} не найдено .log файлов.")
else:
    found_any = False
    for file_path in log_files:
        # Проверяем, существует ли файл
        if os.path.exists(file_path):
            with open(file_path, "r", encoding="utf-8") as file:
                for line_number, line in enumerate(file):  # Читаем файл построчно
                    if args.search_text in line:
                        # Получаем контекст вокруг найденного текста
                        context = get_context(line, args.search_text)
                        # Если контекст найден, выводим информацию
                        if context:
                            print(f"Лог_файл: {file_path}, Строка: {line_number + 1}")
                            print(f"Лог: {context}")
                            print("-" * 50)
                            found_any = True
        else:
            print(f"Лог_файл не найден: {file_path}")
    if not found_any:
        print(f"Текст '{args.search_text}' не найден в логах директории {args.directory}.")

# python exersice_17_1.py -h
# python exersice_17_1.py /Users/qa/project/first_pro_github/Artew/homework/eugene_okulik/data/logs "error"
