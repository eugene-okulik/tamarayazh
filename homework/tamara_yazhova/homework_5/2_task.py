string_1 = "результат операции: 42"
string_2 = "результат операции: 514"
string_3 = "результат работы программы: 9"

result_string_1 = string_1[string_1.index(':') + 1:]
result_string_2 = string_2[string_2.index(':') + 1:]
result_string_3 = string_3[string_3.index(':') + 1:]

print(int(result_string_1) + 10)
print(int(result_string_2) + 10)
print(int(result_string_3) + 10)
