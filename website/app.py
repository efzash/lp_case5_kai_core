from flask import Flask, request, jsonify, render_template, send_file
import os
import re

APP_ROOT = os.path.dirname(os.path.abspath(__file__))
app = Flask(__name__)


import natasha as nat
from yargy.tagger import PassTagger
from natasha.tokenizer import TOKENIZER as tokenizer

tag = PassTagger()


def roman_to_arab(txt):
    CONV_TABLE = ((1000, 'm'), (900, 'cm'), (500, 'd'), (400, 'cd'),
                  (100, 'c'), (90, 'xc'), (50, 'l'), (40, 'xl'),
                  (10, 'x'), (9, 'ix'), (5, 'v'), (4, 'iv'), (1, 'i'))
    ret = 0
    for arab, roman in CONV_TABLE:
        while txt.startswith(roman):
            ret += arab
            txt = txt[len(roman):]
    return ret


def Tabl_value(token, table):
    f = tablesoperativ[tables.index(table)]
    low = 0
    high = len(f) - 1
    while low <= high:
        mid = (low + high) // 2
        if token == sorted([token, f[mid]])[0]:
            high = mid - 1
            actual = low
            for i in f[mid].split(' '):
                if token == i:
                    return (True, actual, len(f[actual]))

        elif token == sorted([token, f[mid]])[1]:
            low = mid + 1
            actual = high
            for i in f[mid].strip("\n").split(' '):
                if token == i:
                    return (True, actual, len(f[actual]))
        else:
            for i in f[mid].strip("\n").split(' '):
                if token == i:
                    return (True, mid, len(f[mid]))

    for i in f[actual].strip("\n").split(' '):
        if token == i:
            return (True, actual, len(f[actual]))

    return (False, None, None)


def Po4_ind(t, token):
    if t.type == 'INT' and len(t.value) == 6:
        return (True, None, None)
    else:
        return (False, None, None)


def Rim(t, token):
    if (t.type == 'LATIN' and ('m' in token or 'c' in token or 'd' in token or 'x' in token or
                               'l' in token or 'i' in token or 'v' in token) and
            ('a' not in token or 'b' not in token or 'e' not in token or 'f' not in token or 'g' not in token or
             'h' not in token or 'j' not in token or 'k' not in token or 'n' not in token or 'o' not in token or
             'p' not in token or 'q' not in token or 'r' not in token or 's' not in token or 't' not in token or
             'u' not in token or 'w' not in token or 'y' not in token or 'z' not in token)):
        return (True, None, None)
    else:
        return (False, None, None)


tables = ['ADROBR.txt', 'SUBJECT.txt', 'Settlements.txt', 'Elements_of_the_road_network.txt',
          'Municipalities.txt',
          'Elements_of_the_planning_structure.txt',
          'Administrative_units.txt', 'Other_items.txt']

tablesoperativ = []
for table in tables:
    f = open('TABLNEW/' + table, 'r')
    strings = []
    for line in f:
        strings.append(line.strip("\n"))
    f.close
    tablesoperativ.append(strings)


def OBRSTR(s):
    s = re.sub(r"[')№\\(,.`<>«»~!@#$%;}{^&*?\"|+=_:]",' ', str(s))
    s = s.lower()
    s = s.split()
    s = ' '.join(s)
    # обработка каждой строки
    tokens = tag(tokenizer(s))
    # генератор токенов
    temp_m = []
    temp_txt = []
    for t in tokens:
        temp_m.append(t)
        temp_txt.append(t.value)

    mas = []  # список списков тегов - список принадлежностей токена к опр категории (таблице фиас)
    mas_nums = []  # список списков индексов в каждом теге - попробуем склеивать слова с одинаковыми тегами по этим индексам
    mas_lengs = []

    for tt, token in enumerate(temp_m):
        t_vector = [0] * 9
        t_vector_i = [0] * 9
        t_vector_l = [0] * 9

        for i, table in enumerate(tables):
            if i == 0:
                t_vector[i], t_vector_i[i], t_vector_l[i] = Po4_ind(token, token.value)  # почтовый инжекс
            elif i == 1:
                t_vector[i], t_vector_i[i], t_vector_l[i] = Rim(token, token.value)  # детекор римских цифр
                if t_vector[i] == True:
                    break
            else:
                t_vector[i], t_vector_i[i], t_vector_l[i] = Tabl_value(token.value, table)
                if t_vector[i] == True:
                    break

        if t_vector[1] == True:  # араб цифры
            temp_txt[tt] = roman_to_arab(temp_txt[tt])

        t_mas = []
        t_mas_i = []
        t_mas_l = []
        for i, elem in enumerate(t_vector):
            if elem == True:
                t_mas.append(i)
                t_mas_i.append(t_vector_i[i])
                t_mas_l.append(t_vector_l[i])

        mas.append(t_mas)  # сформировали списки, в которые входят токены каждого адреса
        mas_nums.append(t_mas_i)  # сформировали индексы, списоков в которые входят токены каждого адреса
        mas_lengs.append(t_mas_l)

    out = ''
    for i, word in enumerate(temp_txt):
        if mas[i]:  # какое условие проверки будет для вывода строки?
            out += ' ' + ''.join(str(word))

    return out.strip()

@app.route('/', methods=['GET'])
def index():
    return render_template("index.html")

@app.route('/result', methods=['POST'])
def csv_upload():
    text = request.form.get('text')
    result = OBRSTR(text)
    return render_template("result.html", result=result)

if __name__ == '__main__':
    app.run(debug=True)
