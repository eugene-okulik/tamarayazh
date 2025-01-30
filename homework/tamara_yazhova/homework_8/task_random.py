import random

salary = int(input("Ваша зарплата: "))
bonus = random.choice([True, False])

if bonus:
    salary_with_bonus = salary + random.randint(50, 5000)
    print(f"{salary}, True - '${salary_with_bonus}'")
else:
    print(f"{salary}, False - '${salary}'")
