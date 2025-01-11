import random

secret_number = random.randint(1, 10)

attempts = 3

print("Гра 'Вгадай число'!")
print("Програма загадала число від 1 до 10. У вас є 3 спроби, щоб його вгадати.")

for i in range(attempts):
    guess = int(input(f"Спроба {i + 1}. Введіть ваше число: "))

    if guess == secret_number:
        print("Вітаємо! Ви вгадали число!")
        break
    elif guess > secret_number:
        print("Менше!")
    else:
        print("Більше!")
else:
    print(f"Ви програли! Загадане число було {secret_number}.")
