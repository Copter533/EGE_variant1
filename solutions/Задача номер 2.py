# Источник: https://inf-ege.sdamgia.ru/test?id=13718138&nt=True&pub=False

# Задача: Логическая функция F задаётся выражением (x ∧ ¬y) ∨ (y ≡ z) ∨ ¬w. Дан частично заполненный фрагмент,
# содержащий неповторяющиеся строки таблицы истинности функции F. Определите, какому столбцу таблицы истинности
# соответствует каждая из переменных x, y, z, w. 

# В ответе напишите буквы x, y, z, w в том порядке, в котором идут
# соответствующие им столбцы (сначала — буква, соответствующая первому столбцу; затем — буква, соответствующая второму
# столбцу, и т. д.). Буквы в ответе пишите подряд, никаких разделителей между буквами ставить не нужно. Пример. Пусть
# задано выражение x → y, зависящее от двух переменных x и y, и фрагмент таблицы истинности: 

# Тогда первому столбцу
# соответствует переменная y, а второму столбцу соответствует переменная x. В ответе нужно написать: yx.

from itertools import permutations, product


table1 = """
0xx0
0101
x10x
""".replace('\n', '')
table2 = ''

for x, y, z, w in product([0, 1], repeat=4):
    val = (x and not y) or (y == z) or not w
    if val == 0: table2 += f'{x}{y}{z}{w}'


for p1 in permutations(range(len(table2) // 4)):
    for p2 in permutations(range(4)):
        for i, e in enumerate(table1):
            j = p2[i % 4] + p1[i // 4] * 4
            if not(e == 'x' or table2[j] == e): break
        else:
            print(''.join(['XYZW'[i] for i in p2]))
