temperatures = [20, 15, 32, 34, 21, 19, 25, 27, 30, 32, 34, 30,
                29, 25, 27, 22, 22, 23, 25, 29, 29, 31, 33, 31,
                30, 32, 30, 28, 24, 23]

new_temperatures = list(filter(lambda x: x > 28, temperatures))
print(list(new_temperatures))

high_temp = max(new_temperatures)
low_temp = min(new_temperatures)
avg_temp = sum(new_temperatures) / len(new_temperatures)

print(f"Самая высокая температура: {high_temp}")
print(f"Самая низкая температура: {low_temp}")
print(f"Средняя температура: {avg_temp:.2f}")