my_list = [2, 'text', 43.5, None, False, [1, 2]]
print("Мой список: ", my_list)
j = 1
for el in my_list:
    print(f"{j}) {el} - type: {type(el)}")
    j += 1
