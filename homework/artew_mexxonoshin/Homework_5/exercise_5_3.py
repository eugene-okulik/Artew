students = ['Ivanov', 'Petrov', 'Sidorov']
subjects = ['math', 'biology', 'geography']

# Формируем строку с помощью join

students = ', '.join(students)
subjects = ', '.join(subjects)

text = f'Students {students} study these subjects: {subjects }'

print(text)
