dist_begin = float(input("Введите результат первого дня: "))
dist_end = float(input("Введите конечный результат: "))
i = 1
while dist_begin <= dist_end:
    print(f"{i} день: {dist_begin:.2f}")
    dist_begin += dist_begin / 100 * 10
    i += 1
print(f"{i} день: {dist_begin:.2f}")
print(f"На {i} день спортсмен достиг результата - не менее {dist_end}")
