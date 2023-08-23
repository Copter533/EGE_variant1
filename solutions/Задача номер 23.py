# Источник: https://inf-ege.sdamgia.ru/test?id=13718138&nt=True&pub=False

# Задача:
# Исполнитель Тренер преобразует число на экране. У исполнителя есть две команды, которым присвоены номера: 1. Прибавить
# 1 2. Прибавить 2 Первая команда увеличивает число на экране на 1, вторая увеличивает его на 2. Программа для
# исполнителя Тренер – это последовательность команд. Сколько существует программ, для которых при исходном числе 1
# результатом является число 11?

import sys
from itertools import product

co = 0
for l in range(2, 12):
    for alg in product([1, 2], repeat=l):
        num = 1
        for s in alg:
            num += s
            if num > 11:
                break
        else:
            if num == 11:
                co += 1

print(co)


def solve(prev):
    if prev == 11:
        return 1
    if prev > 11:
        return 0
    return solve(prev + 1) + solve(prev + 2)


if "checker" not in sys.argv:
    print(solve(1))
