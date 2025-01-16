name = input("Введите ваше имя: ")
age = int(input("Введите ваш возраст: "))
print(f"Куку, {name}! вам {age} лет.")


num1 = float(input("Введите дробное число: "))
num2 = int(input("Введите целое число: "))

print(f"{num1} + {num2} = {num1 + num2}")
print(f"{num1} - {num2} = {num1 - num2}")
print(f"{num1} * {num2} = {num1 * num2}")
print(f"{num1} / {num2} = {num1 / num2}")
print(f"{num1} // {num2} = {num1 // num2}")
print(f"{num1} % {num2} = {num1 % num2}")
print(f"{num1} ** {num2} = {num1 ** num2}")


print("Вот небольшая история:")
balance = 500
print(f"У меня было {balance} монет.")

print("Я купил книгу за 120 монет.")
balance -= 120
print(f"Теперь у меня осталось {balance} монет.")

print("Я заработал 200 монет, выполнив проект.")
balance += 200
print(f"Теперь у меня {balance} монет.")

print("И я пожертвовал 150 монет на благотворительность.")
balance -= 150
print(f"В конце дня у меня осталось {balance} монет.")


celsius = float(input("Введите температуру в градусах Цельсия: "))
fahrenheit = (9/5) * celsius + 32
print(f"Температура в градусах Фаренгейта: {fahrenheit}")

# Оставший баланс :
print(f" Спасибо за использование этой программы, {name}!")
