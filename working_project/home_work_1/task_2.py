data = int(input("Введите количество секунд: "))
hour = data // 3600
data = data % 3600
min = data // 60
sec = data % 60
if hour < 10:
    hour = "0" + str(hour)
if min < 10:
    min = "0" + str(min)
if sec < 10:
    sec = "0" + str(sec)
print(f"{hour}:{min}:{sec}")
