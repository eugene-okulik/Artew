def srez_with_index(results):
    new_results = []
    for result in results:
        number_res = result[result.index(':') + 2:]
        number = int(number_res) + 10
        new_results.append(number)
    return new_results


results = [
    "результат операции: 42",
    "результат операции: 514",
    "результат работы программы: 9",
    "результат: 2"
]

new_results = srez_with_index(results)
for i in range(len(results)):
    print(f"{results[i].rsplit(':',1)[0]}: {new_results[i]}")
