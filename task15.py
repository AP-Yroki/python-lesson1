n = int(input("Введите количество минут: "))

hours = (n //60) % 24
minutes = n % 60
print(hours, minutes)