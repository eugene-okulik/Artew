import datetime


# Дана такая дата
my_time = "Jan 15, 2023 - 12:05:33"

# Преобразование строки в объект datetime
python_date = datetime.datetime.strptime(my_time, '%b %d, %Y - %H:%M:%S')
print(python_date)

# Получение полного названия месяца
# print(python_date.month)
full_name_month = python_date.strftime('%B')

print(full_name_month)
