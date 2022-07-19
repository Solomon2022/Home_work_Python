month_number = int(input("Введите месяц, число от 1 до 12: "))
month_list = ["Январь", "Февраль", "Март", "Апрель", "Май", "Июнь", "Июль", "Август", "Сентябрь", "Октябрь", "Ноябрь",
              "Декабрь"]
my_dict = {"Зима": [12, 1, 2], "Весна": [3, 4, 5], "Лето": [6, 7, 8], "Осень": [9, 10, 11]}
if month_number in (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12):
    for el in my_dict:
        if month_number in my_dict.get(el):
            print(f"Месяц {month_list[month_number - 1]} это {el}")
            break
else:
    print("Данные введены некорректно! ")