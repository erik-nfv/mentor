# !!!Все задания необходимо сделать с использованием генераторов-коллекций!!!:
# (Результатом каждого задания будет коллекция, какая больше подойдет, зависит от задачи)

# 1) Найти все числа от 1 до 1000, которые делятся на 7
lst1 = [x for x in range(1, 1001) if x % 7 == 0]
print(lst1)

# 2) Сгенерировать список на основе чисел от 1 до 1000.
# Если число делится на 3 - положить результат деления в коллецию без изменений,
# в противном случае положить число записанное дважды друг за другом
lst2 = [x if x % 3 == 0 else int(str(x) + str(x)) for x in range(1, 1001)]
print(lst2)

# 3) Посчитать кол-во пробелов в строке "  hel l o      world   "
lst3 = [x for x in "  hel l o      world   " if x == ' ']
print(len(lst3))
# или
_len = sum(1 for x in "  hel l o      world   " if x == ' ')
print(_len)

# 4) Сгенерировать список из слов строки
# “Yellow Yaks like yelling and yawning and yesturday they yodled while eating yuky yams”,
# которые начинаются на Y/y
lst4 = [
    x
    for x in "Yellow Yaks like yelling and yawning and yesturday they yodled while eating yuky yams".split()
    if x.lower().startswith('y')
]
print(lst4)

# 5) Для каждого элемента строки  "hi, 3.44, 535  "
# сгенерировать коллекцию кортежей вида (индекс, значение), (индекс, значение)
lst5 = [
    (x, y.strip())
    for x, y in enumerate("hi, 3.44, 535  ".split(','))
]
print(lst5)
# 6) Сгенерировать коллекцию с числами из строки
# "In 1984 there were 13 instances of a protest with over 1000 people attending"
lst6 = [
    int(x)
    for x in "In 1984 there were 13 instances of a protest with over 1000 people attending".split() if x.isdigit()
]
print(lst6)

# 7) Для чисел из промежутка [1, 20] сгенерировать коллекцию строк вида ("четное", "нечетное", "четное")
lst7 = ["четное" if x % 2 == 0 else "нечетное" for x in range(1, 21)]
print(lst7)

# 8) Найти все слова из строки, длина которых меньше 4 символов
# "The trickiest part of learning list comprehension for me was really understanding the syntax."
lst8 = [x for x in
        "The trickiest part of learning list comprehension for me was really understanding the syntax.".split() if
        len(x) < 4]
print(lst8)

# 9) Найти простые числа из промежутка [1, 50].
# Простым числом называется число, которое делится только на единицу и на себя же.
lst9 = [x for x in range(1, 51) if all(x % i != 0 for i in range(2, x)) and x > 1]
print(lst9)
