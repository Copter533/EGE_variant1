# Источник: https://inf-ege.sdamgia.ru/test?id=13718138&nt=True&pub=False

# Задача:
# Каждый сотрудник предприятия получает электронный пропуск, на котором записаны личный код сотрудника, код
# подразделения и некоторая дополнительная информация. Личный код состоит из 19 символов, каждый из которых может быть
# одной из 14 допустимых заглавных букв или одной из 8 цифр (цифры 0 и 3 не используются). Для записи кода на пропуске
# отведено минимально возможное целое число байтов. При этом используют посимвольное кодирование, все символы кодируют
# одинаковым минимально возможным количеством битов. Код подразделения — натуральное число, не превышающее 1500, он
# записан на пропуске как двоичное число и занимает минимально возможное целое число байтов. Всего на пропуске хранится
# 36 байт данных. Сколько байтов выделено для хранения дополнительных сведений об одном сотруднике? В ответе запишите
# только целое число — количество байтов

from math import log

code_bit = round(log(22, 2).real + .5) * 19
code_byte = round(code_bit / 8 + .5)

place_bit = round(log(1500, 2).real + .5)
place_byte = round(place_bit / 8 + .5)

print(36 - code_byte - place_byte)
