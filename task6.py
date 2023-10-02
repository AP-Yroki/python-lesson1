monitor = int(input("Введие стоимость монитора: "))
system_unit = int(input("Введите стоимость системного блока: "))
keyboard = int(input("Введите стоимость клавиатуры: "))
mouse = int(input("Ввыедите стоимость мыши: "))

price = (monitor + system_unit + keyboard + mouse) * 3
print(price)