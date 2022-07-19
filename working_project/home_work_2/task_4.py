str_user = input("Введите строку: ")
i = 1
for el in str_user.split():
    print(f"{i}) {el[:10]}")
    i += 1
