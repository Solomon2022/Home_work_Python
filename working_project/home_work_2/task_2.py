my_list = input("Введите список через пробел: ").split()
print("Ваш список:", my_list)
j = 0
while len(my_list) > j:
    if len(my_list) == 1:
        break
    a = my_list[j]
    my_list[j] = my_list[j + 1]
    my_list[j + 1] = a
    j += 2
    if len(my_list) % 2 != 0 and j == len(my_list) - 1:
        break
print("Изменённый список:", my_list)
