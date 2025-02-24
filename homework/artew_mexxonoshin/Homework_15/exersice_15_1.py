import mysql.connector as mysql

# Создание подключения к базе данных

db = mysql.connect(
    user='st-onl',
    passwd='AVNS_tegPDkI5BlB2lW5eASC',
    host='db-mysql-fra1-09136-do-user-7651996-0.b.db.ondigitalocean.com',
    port=25060,
    database='st-onl'
)

# Создание курсора
cursor = db.cursor(dictionary=True)

# Создайте студента (student)
insert_query = "INSERT INTO students (name, second_name) VALUES (%s, %s)"
cursor.execute(insert_query, ('Artew_py_sql', 'Mexx_py_sql'))

# Сохраните id нового студента
student_id = cursor.lastrowid

select_query = "SELECT * FROM students WHERE name = %s AND second_name = %s"
cursor.execute(select_query, ('Artew_py_sql', 'Mexx_py_sql'))
data1 = cursor.fetchall()

print("Студент:", data1)

# Создайте несколько книг (books) и укажите, что ваш созданный студент взял их
insert_query2 = "INSERT INTO books (title, taken_by_student_id) VALUES (%s, %s)"
cursor.execute(insert_query2, ('book873_py_sql', student_id))
cursor.execute(insert_query2, ('book874_py_sql', student_id))

select_query2 = "SELECT * FROM books where taken_by_student_id = %s"
cursor.execute(select_query2, (student_id,))
data2 = cursor.fetchall()

print("Книги:", data2)


# Создайте группу (group) и определите своего студента туда
insert_query3 = "INSERT INTO `groups` (title, start_date, end_date) VALUES (%s, %s, %s)"
cursor.execute(insert_query3, ('groups873_py_sql', 'des 2024', 'march 2025'))

# Сохраните id группы
group_id = cursor.lastrowid

select_query3 = "SELECT * FROM `groups` WHERE id = %s"
cursor.execute(select_query3, (group_id,))
data3 = cursor.fetchall()

print("Группа:", data3)

update_query1 = "UPDATE students SET group_id = %s WHERE id = %s"
cursor.execute(update_query1, (group_id, student_id))

select_query4 = "SELECT * FROM students WHERE id = %s"
cursor.execute(select_query4, (student_id,))
updated_student_group = cursor.fetchone()

print("Group_id_in_students:", updated_student_group)


# Создайте несколько учебных предметов (subjects)
insert_query4 = "INSERT INTO subjets (title) VALUES (%s)"
cursor.execute(insert_query4, ('subject_Okulik_py_sql',))
subject_id1 = cursor.lastrowid  # Первый ид

cursor.execute(insert_query4, ('subject2_Okulik_py_sql',))
subject_id2 = cursor.lastrowid  # Второй ид

# Ид наших предметов
subject_ids = (subject_id1, subject_id2)

select_query5 = "SELECT * FROM subjets WHERE title IN (%s, %s)"
cursor.execute(select_query5, ('subject_Okulik_py_sql', 'subject2_Okulik_py_sql'))
data4 = cursor.fetchall()

print("Предметы:", data4)

# Создайте по два занятия для каждого предмета (lessons)

for subject_id in subject_ids:
    insert_query5 = "INSERT INTO lessons (title, subject_id) VALUES ('lesson13_py_sql', %s)"
    cursor.execute(insert_query5, (subject_id,))
    insert_query6 = "INSERT INTO lessons (title, subject_id) VALUES ('lesson14_py_sql', %s)"
    cursor.execute(insert_query6, (subject_id,))

select_query6 = "SELECT * FROM lessons WHERE subject_id IN (%s, %s)"
cursor.execute(select_query6, subject_ids)
data5 = cursor.fetchall()


print("Занятия для предметов:")
for record in data5:
    print(f"ID урока: {record['id']}, Название урока: {record['title']}, ID предмета: {record['subject_id']}")

lesson_ids = [lesson['id'] for lesson in data5]

# Поставьте своему студенту оценки (marks) для всех созданных вами занятий

for lesson_id in lesson_ids:
    insert_query7 = "INSERT INTO marks (value, lesson_id, student_id) VALUES (5, %s, %s)"
    cursor.execute(insert_query7, (lesson_id, student_id))
    insert_query8 = "INSERT INTO marks (value, lesson_id, student_id) VALUES (4, %s, %s)"
    cursor.execute(insert_query8, (lesson_id, student_id))

select_query7 = "SELECT * FROM marks WHERE student_id = %s"
cursor.execute(select_query7, (student_id,))
data6 = cursor.fetchall()
print("Оценки для предметов:")
for record in data6:
    print(f"ID: {record['id']}, Оценка: {record['value']}, ID урока: {record['lesson_id']},"
          f"ID студента: {record['student_id']}")

# Получите информацию из базы данных:

# Все оценки студента стр 105

# Все книги, которые находятся у студента

select_query8 = "SELECT * FROM books WHERE taken_by_student_id = %s"
cursor.execute(select_query8, (student_id,))
data7 = cursor.fetchall()
print("Все книги, которые находятся у студента", data7)

# Для вашего студента выведите всё, что о нем есть в базе: группа, книги, оценки с названиями занятий и предметов
# (всё одним запросом с использованием Join)

select_query9 = """
SELECT *
FROM students AS s
INNER JOIN `groups` AS g ON s.group_id = g.id
LEFT JOIN books AS b ON s.id = b.taken_by_student_id
LEFT JOIN marks AS m ON s.id = m.student_id
LEFT JOIN lessons AS l ON m.lesson_id = l.id
LEFT JOIN subjets AS sub ON l.subject_id = sub.id
WHERE s.id = %s
"""

cursor.execute(select_query9, (student_id,))
data8 = cursor.fetchall()
print("JOIN")
for item in data8:
    print(f"ID: {item['id']}, Name: {item['name']},"
          f"Second Name: {item['second_name']},"
          f"Group ID: {item['group_id']}, Title: {item['title']},"
          f"Start Date: {item['start_date']}, End Date: {item['end_date']},"
          f"Taken by Student ID: {item['taken_by_student_id']}, Value: {item['value']},"
          f"Lesson ID: {item['lesson_id']}, Student ID: {item['student_id']}, Subject ID: {item['subject_id']}")

# Сохранение изменений
db.commit()

db.close()
