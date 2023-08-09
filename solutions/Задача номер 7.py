# Источник: https://inf-ege.sdamgia.ru/test?id=13718138&nt=True&pub=False

# Задача:
# Автоматическая фотокамера производит растровые изображения размером 1200 на 900 пикселей. При этом объём файла с
# изображением не может превышать 900 Кбайт, упаковка данных не производится. Какое максимальное количество цветов можно
# использовать в палитре?

from cmath import log


# Если ЧБ (только 2 цвета), то размер = 1200 * 900 * 1 = 1 080 000 бит
# что > чем 57 600 бит (900 Кбайт)
pxs = 1200 * 900
last_ok = 0
for x in range(0, 50_000):
    if not (pxs * x < 900 * 8 * 8): break
    last_ok = x

print('???')
# print(int(log(int(last_ok), 2).real))
