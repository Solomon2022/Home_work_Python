products_list = []
i = 1
while i <= 3:
    name = input("Введите название: ")
    price = int(input("Введите цену: "))
    quantity = int(input("Введите количество: "))
    measure = input("Введите единицу измерения: ")
    products_list.append((i, {"название": name, "ценa": price, "количество": quantity, "ед": measure}))
    i += 1
    for el in products_list:
        print(el)
name_list = set()
price_list = []
quantity_list = []
measure_list = set()
for el in products_list:
    name_list.add(el[1].get("название"))
    price_list.append(el[1].get("ценa"))
    quantity_list.append(el[1].get("количество"))
    measure_list.add(el[1].get("ед"))
analytics_dict = [{"название": name_list, "ценa": price_list, "количество": quantity_list, "ед": measure_list}]
print()
print(analytics_dict)



