number_1 = int(input("Введите первое число: "))
number_2 = int(input("Введите второе число: "))
calc = input("Выбирите действие: \n 1 - сумма; \n 2 - разность; \n 3 - умножение; \n 4 - деление; \n --> ")
if calc == "1":
    print("Сумма равна: ", number_1 + number_2)
elif calc == "2":
    print("Разность равна: ", number_1 - number_2)
elif calc == "3":
    print("Умножение равно: ", number_1 * number_2)
elif calc == "4":
    print(f"Деление равно: {number_1 / number_2:.2f}")
else:
    print("Введены некоректные данные!")
