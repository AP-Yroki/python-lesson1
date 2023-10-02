nums = int(input("Введите положительное трехзначное число: "))

digit1 = nums // 100
digit2 = (nums //10) % 10
digit3 = nums %10

digit_sum = digit1 + digit2 + digit3
digit_mult = digit1 * digit2 * digit3

print(f"Сумма цифр = {digit_sum}\nПроизведение цифр = {digit_mult}")