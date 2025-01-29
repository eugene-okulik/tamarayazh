number = 6

while True:
    user_input = int(input("Напишите цифру: "))
    if user_input == number:
        print("Поздравляю! Вы угадали!")
        break
    else:
        print("Попробуйте снова")
