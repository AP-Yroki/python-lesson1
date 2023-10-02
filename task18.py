v = int(input("Введите скорость (км/ч): "))
t = int(input("Введите время (часы): "))


position = (v * t) % 109


print(position)