minutes = int(input("Введите количество минут: "))

hours = minutes // 60
result = minutes % 60
print(f"{minutes} мин - это {hours} час {result} минут.")