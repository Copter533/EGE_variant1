# Источник: https://inf-ege.sdamgia.ru/test?id=13718138&nt=True&pub=False

# Задача:
# Назовём маской числа последовательность цифр, в которой также могут встречаться следующие символы: —
# символ «?» означает ровно одну произвольную цифру; — символ «*» означает любую последовательность цифр
# произвольной длины; в том числе «*» может задавать и пустую последовательность. Например, маске 123*4?5
# соответствуют числа 123405 и 12300405. Среди натуральных чисел, не превышающих 10^8, найдите все числа,
# соответствующие маске 12??36*1, делящиеся на 273 без остатка. В ответе запишите в первом столбце
# таблицы все найденные числа в порядке возрастания, а во втором столбце — соответствующие им
# результаты деления этих чисел на 273. Количество строк в таблице для ответа избыточно.

ans = []
for a in "0123456789":
    for b in "0123456789":
        for c in range(-1, 1000):
            num = int(f"12{a}{b}36{c}1".replace("-1", ''))
            if num > 10 ** 8: continue
            if num % 273 != 0: continue
            ans.append(num)

for i in sorted(ans):
    print(i, i // 273)

# ­
# ­
# ­
# ­
# ­
# ­
# ­
# ­
# ­
# ­
# ­
# ­
# ­
# ­
# ­
# ­
# ­
# ­
# ­
# ­
# ­
# ­
# ­
# ­
# ­
# ­
# ­
# ­
# ­
# ­
# ­
# ­
# ­
# ­
# ­
# ­
# ­
# ­
# ­
# ­
# ­
# ­
# ­
# ­
# ­
# ­
# ­
# ­
# ­
# ­
# ­
# ­
# ­
# ­
# ­
# ­
# ­
# ­
# ­
# ­
# ­
# ­
# ­
# ­
# ­
# ­
# ­
# ­
# ­
# ­
# ­
# ­
# ­
# ­
# ­
# ­
# ­
# ­
# ­
# ­
# ­
# ­
# ­
# ­
# ­
# ­
# ­
# ­
# ­
# ­
# ­
# ­
# ­
# ­
# ­
# ­
# ­
# ­
# ­
# ­
# ­
# ­
# ­ А почему бы и нет?
