temperatures = [
    20, 15, 32, 34, 21, 19, 25, 27, 30, 32, 34, 30,29, 25, 27,
    22, 22, 23, 25, 29, 29, 31, 33, 31, 30, 32, 30, 28, 24, 23
]

new_list = list(filter(lambda x: x > 28, temperatures))

print(new_list)
print("Максимальная температура: ", max(new_list))
print("Минимальная температура: ", min(new_list))
print("Средняя температура: ", round(sum(new_list) / len(new_list), 2))
