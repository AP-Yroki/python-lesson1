n = int(input("Введите целое положительное число, не превышающее 1000: "))

next_even = n + 2 - n % 2
print(next_even)