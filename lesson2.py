# Запрашиваем и выводим имя
name = input("Enter your name: ")
surname = input("Enter your surname: ")
full_name = input("Enter your full name: ")
print(f"Hello {name} {surname} {full_name}!")

# TASK 1: Преобразование температуры из Цельсия в Фаренгейт
celsius = 7
fahrenheit = (9 / 5) * celsius + 32
print(f"{celsius} °C = {fahrenheit} °F")

# TASK 2: Вычисление площади круга
radius = 15
pi = 3.14
area = pi * radius**2
print(f"The area of a circle with radius {radius} is {area}")

# TASK 3: Арифметические операции с двумя числами
num1 = 10
num2 = 8

print(f"{num1} + {num2} = {num1 + num2}")
print(f"{num1} - {num2} = {num1 - num2}")
print(f"{num1} * {num2} = {num1 * num2}")
print(f"{num1} / {num2} = {num1 / num2}")
print(f"{num1} // {num2} = {num1 // num2}")
print(f"{num1} % {num2} = {num1 % num2}")
print(f"{num1} ** {num2} = {num1 ** num2}")
