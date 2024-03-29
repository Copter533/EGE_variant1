# Источник: https://inf-ege.sdamgia.ru/test?id=13718138&nt=True&pub=False

# Задача:
# В магазине для упаковки подарков есть N кубических коробок. Самой интересной считается упаковка подарка по принципу
# матрёшки подарок упаковывается в одну из коробок та в свою очередь в другую коробку и т.д. Одну коробку можно
# поместить в другую если длина её стороны хотя бы на 3 единицы меньше длины стороны другой коробки. Определите
# наибольшее количество коробок которое можно использовать для упаковки одного подарка и максимально возможную длину
# стороны самой маленькой коробки где будет находиться подарок. Размер подарка позволяет поместить его в самую маленькую
# коробку. Входные данные. Задание 26 В первой строке входного файла находится число N количество коробок в магазине
# натуральное число не превышающее 10000. В следующих N строках находятся значения длин сторон коробок все числа
# натуральные не превышающие 10000 каждое в отдельной строке. Запишите в ответе два целых числа сначала наибольшее
# количество коробок которое можно использовать для упаковки одного подарка затем максимально возможную длину стороны
# самой маленькой коробки в таком наборе. Пример входного файла 5 43 40 32 40 30 Пример входного файла приведён для пяти
# коробок и случая когда минимальная допустимая разница между длинами сторон коробок подходящих для упаковки матрёшкой
# составляет 3 единицы. При таких исходных данных условию задачи удовлетворяют наборы коробок с длинами сторон 30 40 и
# 43 или 32 40 и 43 соответственно т.е. количество коробок равно 3 а длина стороны самой маленькой коробки равна 32.

data = tuple(map(int, open(r"../files/Задача номер 26/Задание 26.txt").readlines()))

count, lens = data[0], data[1:]

a = b = 0

for cut in range(5):
    s_lens = sorted(lens)[cut:]
    streak = [min(s_lens)]
    for i in s_lens:
        if i - streak[-1] < 3: continue
        streak.append(i)

    a = max(len(streak), a)
    b = max(streak[0], b)

print(a, b)