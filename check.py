import os
import re
import subprocess
import multiprocessing
from time import time

import requests
from bs4 import BeautifulSoup

site = "https://inf-ege.sdamgia.ru"
url = "https://inf-ege.sdamgia.ru/test?id=13718138&nt=True&pub=False"  # Url пробника
solutions = "solutions"
answers = "answers.html"


def generate_html_table(table, wrongs):
    table_html = "<html>\n<head>\n<meta charset='UTF-8'>\n{}\n</head>\n<body style='background-color: #2b2b2b;'>\n" \
    .format(
        """<style>
            table { background-color: #f0f0f0; border-color: black; border: black; }
            h1 {
                background-color: #3c3f41;
                color: white;

                padding: 30px;
                border-radius: 10px;
            }
            .hidden {
                background-color: black;
                white-space: pre;
            }
            .hidden:hover {
                background-color: black;
                color: white;
            }
            </style>""")

    # Заголовок
    table_html += "<h1 align='center'>Правильность ответов:</h1>\n"

    # Начало таблицы
    table_html += "<table border='1' cellpadding='10' align='center'>\n"

    # Заголовок таблицы
    table_html += "<tr style='background-color: black; color: white; font-weight: bold;'>\n"
    for item in table[0]:
        table_html += f"<th>{item}</th>\n"
    table_html += "</tr>\n"

    # Остальные строки таблицы
    spacesM = max([len(i[-1]) for i in table[1:]])
    counter = [0, 0, 0]

    for j in range(1, 26 + 1):
        possible_row = [i for i in table if i[0] == f'#{j}']
        row = possible_row[0] if possible_row else [f'#{j}', '', '💫', '❔']
        if not isinstance(row[2], bool):
            table_html += "<tr style='background-color: #f0f0ff'>\n"
        else:
            if row[1] == '???':
                table_html += "<tr style='background-color: #c0ffc0'>\n"
                row[1] = '❔❔❔'
            else:
                table_html += "<tr>\n" if row[2] else "<tr style='background-color: #fff0f0'>\n"

        for i, item in enumerate(row):
            item_s = f"<td align='center'>{item}</td>\n"
            if i == 3:
                sp = ' ' * (spacesM - len(item))
                item_s = f"<td align='center'><span class='hidden'>{sp}{item}{sp}</span></td>\n"
            elif i == 2:
                if not isinstance(item, bool):
                    item_s = f"<td align='center'>{item}</td>\n"
                    counter[2] += 1
                elif not item:
                    paste = '✖'
                    answer, correct = row[1], row[3]
                    answers, corrects = len(answer.split()), len(correct.split())
                    if answers != corrects:
                        paste += ' ' + ['МАЛО', 'МНОГО'][answers > corrects]
                    item_s = f"<td align='center' style='color: red'>{paste}</td>\n"
                    counter[1] += 1
                else:
                    item_s = f"<td align='center' style='color: green'>✔</td>\n"
                    counter[0] += 1
            table_html += '\t' + item_s
        table_html += "</tr>\n"

    # Закрываем таблицу
    table_html += "</table>\n"

    # Создаём таблицу с результатами
    wrong_style = "align='center' style='color: red'"
    table_html += f"""\
<h1 align='center'>Результаты:</h1>
<table border='1' cellpadding='10' align='center'>
    <tr>
        <td align='center' style='color: green'>✔</td>
        <td align='center' style='color: red'>✖</td>
        <td align='center' style='color: blue'>⚪</td>
        <td align='center' colspan="{len(wrongs)}">Исправить</td>
    </tr>
    <tr>
        <td align='center'>{counter[0]}</td>
        <td align='center'>{counter[1]}</td>
        <td align='center'>{counter[2]}</td>
        <td {wrong_style}>{f'</td><td {wrong_style}>'.join(wrongs)}</td>
    </tr>
</table>"""

    # Окончание
    table_html += "</body>\n</html>"

    return table_html


def check_task(filename, link, answer=None):
    os.chdir(solutions)
    if answer is None:
        answer = subprocess.run(["python", filename], capture_output=True, text=True).stdout.lower().strip(' \n')
    os.chdir('../')

    response = requests.get(link)
    soup = BeautifulSoup(response.text, 'html.parser')

    datablob = soup.find("div", id=lambda v: v and re.fullmatch(r'sol\d+', v)).text
    le = datablob.rfind("Ответ: ") + 6
    ri = datablob.find(".", le)

    correct = datablob.split()[-1].strip('\n. ') if le == 5 else datablob[le:ri].strip()
    correct = correct.replace(' ', '')
    return filename, answer, correct


def main():
    print("Вывод осуществляется в", answers)

    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    prob_list = soup.find("div", class_="prob_list")
    assert prob_list, ValueError("ОЙ! Укажите ссылку на СПИСОК задач, а не на одну задачу")

    tasks = {}
    table = ['Номер Ответ Правильность ДА'.split()]
    with multiprocessing.Pool() as pool:
        for filename in os.listdir(solutions):

            # if '2' not in filename: continue

            problem_number = [i for i in filename[:filename.find('.')].split(' ') if i.isnumeric()][-1]
            filepath = os.path.join(solutions, filename)

            prob_item = prob_list.find("div", class_="prob_num", string=problem_number)
            assert prob_item, ValueError("ОЙ! Задачи с таким номером нет на сайте!")

            nums = prob_item.find_next().find("span", class_="prob_nums")
            assert nums, ValueError("ОЙ! Ссылка на ответ не найдена!")

            link = site + nums.find('a')["href"]

            if filename.endswith(".txt"):
                with open(filepath, 'r', encoding="utf-8") as f:
                    s = f.read()
                    le = s.find("Ответ: ") + 6
                    ri = s.find('\n', le)
                    answer = s[le:ri].strip()

                    tasks[problem_number] = pool.apply_async(check_task, (filename, link, answer))
            else:
                tasks[problem_number] = pool.apply_async(check_task, (filename, link))

        wrongs = []
        finished = []
        print("Running...")

        st = time()
        while (time() - st < 4) and not all([i.ready() for i in tasks.values()]): pass
        print('Finished!')

        unfinished = [k for k, v in tasks.items() if not v.ready()]
        pool.terminate()  # Принудительно завершаем все незавершенные задачи

        for k, task in tasks.items():
            if not task.ready(): continue

            problem_number = '#' + k
            filename, raw_answer, correct = task.get()

            if raw_answer != correct: wrongs.append(problem_number)
            answer = raw_answer.replace('\n', '↷') if raw_answer else '✖'
            state = answer == correct
            finished.append(problem_number[1:])

            table.append([problem_number, answer, state, correct])

        for k in unfinished:
            table.append(['#' + k, 'TIMEOUT', '⏰', '❔'])
            wrongs.append('#' + k)

        html_table = generate_html_table(table, wrongs)
        with open(answers, 'w', encoding='utf-8') as f:
            f.write(html_table)


if __name__ == '__main__':
    main()
