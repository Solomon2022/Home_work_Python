rank_list = [7, 5, 3, 3, 2]
print("Текущий рейтинг: ", rank_list)
number = int(input("Введите балл: "))
if number > rank_list[0]:
    rank_list.insert(0, number)
else:
    i = len(rank_list) - 1
    while True:
        if number <= rank_list[i]:
            rank_list.insert(i + 1, number)
            break
        else:
            i -= 1;
print("Рейтинг изменен: ", rank_list)
