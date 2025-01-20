import random

# ф-ция рандомный бонус
def bonus_random():
    return random.randint(0, 10000)

# ф-ция для расчета общей зарплаты с учетом рандомного бонуса
def bonus_salary():
    salary = int(input('Ваша зарплата: '))
    bonus = random.choice([True, False])

    if bonus == True:
        bonus_sum = bonus_random()
        total_salary = salary + bonus_sum
        print(f"Salary: {total_salary} р , Bonus: {bonus_sum} р")
    else:
        total_salary = salary
        print(f"Salary: {total_salary} р, Bonus: 0 р")

bonus_salary()