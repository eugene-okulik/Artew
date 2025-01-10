result1 = "результат операции: 42"
result2 = "результат операции: 514"
result3 = "результат работы программы: 9"


result1 = result1[result1.index(':') + 2:]
result2 = result2[result2.index(':') + 2:]
result3 = result3[result3.index(':') + 2:]

print("результат операции:", int(result1) + 10)
print("результат операции:", int(result2) + 10)
print("результат работы программы:", int(result3) + 10)
