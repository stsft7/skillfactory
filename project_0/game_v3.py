import random

number = random.randint(1, 100) #инициируем случайный выбор числа в пределах от 1 до 100;
low = 1
high = 100
attempts = 0

print("Угадай число от 1 до 100. Попытайся угадать его за меньшее количество попыток!")

while True:
    guess = (low + high) // 2 #сокращаем диапазон поиска в два раза, сравнив середину числового диапазона с искомым числом;
    print(f"Мой вариант: {guess}")
    attempts += 1

    if guess < number:
        print("Загаданное число больше")
        low = guess + 1
    elif guess > number:
        print("Загаданное число меньше")
        high = guess - 1
    else:
        print(f"Поздравляю! Я угадал число {number} за {attempts} попыток.")
        break

if attempts >= 20:
    print(f"К сожалению, число {number} не было угадано за меньше чем 20 попыток.")
    
    
