import csv
import mysql.connector as mysql
import dotenv
import os


# Загрузка переменных окружения из .env файла
dotenv.load_dotenv()

# Получение данных подключения из переменных окружения
db_user = os.getenv('DB_USER')
db_password = os.getenv('DB_PASSW')
db_host = os.getenv('DB_HOST')
db_port = os.getenv('DB_PORT')
db_name = os.getenv('DB_NAME')

# Подключение к базе данных
try:
    db = mysql.connect(
        host=db_host,
        user=db_user,
        password=db_password,
        database=db_name,
        port=db_port
    )
    print('-' * 35)
    print("Успешное соединение с базой данных.")
    print('-' * 35)

    cursor = db.cursor()

except mysql.Error as e:
    print(f"Ошибка подключения к базе данных: {e}")
    exit(1)

# Установка пути к файлу CSV
base_path = os.path.dirname(__file__)
homework_path = os.path.dirname(os.path.dirname(base_path))
eugene_okulik_file_path = os.path.join(homework_path, 'eugene_okulik', 'Lesson_16', 'hw_data', 'data.csv')
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

print('-' * 35)

with open(eugene_okulik_file_path, newline='') as csvfile:
    csv_reader = csv.reader(csvfile)
    header = next(csv_reader)

    for row in csv_reader:
        name = row[0]
        second_name = row[1]
        group_title = row[2]
        book_title = row[3]
        subject_title = row[4]
        lesson_title = row[5]
        mark_value = row[6]

    query = '''
    SELECT
        s.name,
        s.second_name,
        g.title AS group_title,
        b.title AS book_title,
        sub.title AS subject_title,
        l.title AS lesson_title,
        m.value AS mark_value
    FROM
        students AS s
    INNER JOIN
        `groups` AS g ON s.group_id = g.id
    LEFT JOIN
        books AS b ON s.id = b.taken_by_student_id
    LEFT JOIN
        marks AS m ON s.id = m.student_id
    LEFT JOIN
        lessons AS l ON m.lesson_id = l.id
    LEFT JOIN
        subjets AS sub ON l.subject_id = sub.id;
   '''

    cursor.execute(query)
    record_exists = cursor.fetchone() is not None

    if record_exists:
        print(f"Запись найдена: {row}")
    else:
        print(f"Запись не найдена: {row}")

db.close()
