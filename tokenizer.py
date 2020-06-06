import random
import codecs
import re

f = codecs.open("SBERDATA/SBERBANK/bad.csv", 'r', "utf_8_sig")

elementaddr = []
for line in f:
    elementaddr.append(line.strip("\n"))
    break
print(elementaddr)

fw = open("BADCLEAR.txt", 'w')

for line in f:
    s = line.strip("\n").split(';')[1]
    s = re.sub(r"[')№\\(,.`<>«»~!@#$%;}{^&*?\"|+=_:]",' ', str(s))
    s = s.lower()
    s = s.split()
    s = ' '.join(s)
    fw.write(s +"\n")
fw.close()
f.close()

import natasha as nat
from yargy.tagger import PassTagger
from natasha.tokenizer import TOKENIZER as tokenizer
tag = PassTagger()
import time

s = time.time()

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

def Tabl_value_1(token, table):

    f = open('C:/Users/Admin/Desktop/TABLNEW/TABLNEW/' + table, 'r')
    index = -1
    
    for line in f:
        index += 1
        chslov = line.strip("\n").split(' ')
        for i in chslov:
            if token == i:
                return(True, index, len(chslov))
    return(False, None, None)

def Tabl_value(token, table):
    f = tablesoperativ[tables.index(table)]
    index = -1
    for line in f:
        index += 1
        chslov = line.strip("\n").split(' ')
        for i in chslov:
            if token == i:
                return(True, index, len(chslov))
    
    return(False, None, None)

def In_value(token, table, column_num):
    f = tablesoperativ[tables.index(table)]
    index = -1
    for line in f:
        index += 1
        if index == column_num:
            if line.strip("\n").find(token)>=0:
                return(True, table, column_num)
            else:
                break
    
    return(False, table, column_num)


def Po4_ind(t, token):    
    if t.type == 'INT' and len(t.value)==6:
        return(True, None, None)
    else:
        return(False, None, None)

def Rim(t, token):
    if (t.type == 'EN' and ('m' in token or 'c' in token or 'd' in token or 'x' in token or 
                           'l' in token or 'i' in token or 'v' in token) and 
    ('a' not in token or 'b' not in token or 'e' not in token or 'f' not in token or 'g' not in token or 
     'h' not in token or 'j' not in token or 'k' not in token or 'n' not in token or 'o' not in token or 
     'p' not in token or 'q' not in token or 'r' not in token or 's' not in token or 't' not in token or 
     'u' not in token or 'w' not in token or 'y' not in token or 'z' not in token)):
        return(True, None, None)
    else:
        return(False, None, None)


tables = ['SUBJECT.txt','Settlements.txt','Elements_of_the_road_network.txt',
              'Municipalities.txt',
              'Elements_of_the_planning_structure.txt',
              'Administrative_units.txt', 'Other_items.txt']

tablesoperativ = []
for table in tables:
    f = open('C:/Users/Admin/Desktop/TABLNEW/TABLNEW/' + table, 'r')
    strings = []
    for line in f:
        strings.append(line.strip("\n"))
    f.close
    tablesoperativ.append(strings)


#for i in range(len(bad)):
for q in range(3484):
    #обработка каждой строки
    tokens = tag(tokenizer(bad[q])) 
    #генератор токенов
    temp_m = []
    temp_txt =[]
    for t in tokens:
        temp_m.append(t)
        temp_txt.append(t.value)
        
    #print(temp_txt)
    mas = []#список списков тегов - список принадлежностей токена к опр категории (таблице фиас)
    mas_nums = []#список списков индексов в каждом теге - попробуем склеивать слова с одинаковыми тегами по этим индексам
    mas_lengs = []

    
    for token in temp_m:
        t_vector = [0] * 9
        t_vector_i = [0] * 9
        t_vector_l = [0] * 9
            #mas.append([0])
            #Poch_ind(token.value)#обработка почтового индекса
        
        #t_vector[0], t_vector_i[0], t_vector_l[0] = Po4_ind(token, token.value)
        #t_vector[1], t_vector_i[1], t_vector_l[1] = Rim(token, token.value)
        '''   
        for i in range(2, len(tables)+2):
            #for i, table in enumerate(tables):
            t_vector[i], t_vector_i[i], t_vector_l[i] = Tabl_value(token.value, table)
        #print(t_vector, t_vector_i, t_vector_l)
        '''
        
        for i, table in enumerate(tables):
            if i==0:
                t_vector[i], t_vector_i[i], t_vector_l[i] = Po4_ind(token, token.value)
            elif i==1:
                t_vector[i], t_vector_i[i], t_vector_l[i] = Rim(token, token.value)
            else:
                t_vector[i], t_vector_i[i], t_vector_l[i] = Tabl_value(token.value, table)
            
        t_mas = []
        t_mas_i = []
        t_mas_l = []
        for i, elem in enumerate(t_vector):
            if elem == True:
                t_mas.append(i)
                t_mas_i.append(t_vector_i[i])
                t_mas_l.append(t_vector_l[i])

        mas.append(t_mas)#сформировали списки, в которые входят токены каждого адреса
        mas_nums.append(t_mas_i)#сформировали индексы, списоков в которые входят токены каждого адреса
        mas_lengs.append(t_mas_l)
    #print(temp_txt)
    #print(mas)
    #print(mas_nums)
    #print(mas_lengs)
    
    #склейка одинаковых тегов
    for i, tok in enumerate(mas): #рассматриваем токены строки - одного адрес
        if len(tok) == 1 and mas_lengs[i][0] is not None and mas_lengs[i][0] >1: #только токены с 1 тегом и только токены, найденные в строках длиной более 1
            #print(i)
            if i+1 < len(mas) and len(mas[i+1]) == 1:#проверка на края списка и длины тега соседа
                #print('es')
                if tok == mas[i+1] and mas_nums[i] == mas_nums[i+1]:#проверка на идентичные токены
                    #print(i,i+1,'ESS')
                    #print(temp_txt)
                    #print(mas)
                    #print(mas_nums)
                    temp_txt[i]= temp_txt[i]+' '+temp_txt[i+1]#склейка
                    temp_txt.pop(i+1)
                    mas.pop(i+1)
                    mas_nums.pop(i+1)
                    mas_lengs.pop(i+1)
                    
            elif i-1 >=0 and len(mas[i-1]) == 1:#проверка на края списка и длины тега соседа
                #print('qw')
                if tok == mas[i-1] and mas_nums[i] == mas_nums[i-1]:#проверка на идентичные токены
                    #print(i-1, i,'QWW')
                    temp_txt[i-1]= temp_txt[i-1]+' '+temp_txt[i]#склейка
                    temp_txt.pop(i)
                    mas.pop(i)
                    mas_nums.pop(i)
                    mas_lengs.pop(i)
            
            #попытка склейки тегированного сообщения и текста
            elif i+1 < len(mas) and len(mas[i+1]) == 1:#проверка на края списка и длины тега соседа
                
                rez = In_value(temp_txt[i+1], (mas[i]), mas_nums[i])#ф-я проверки соседа по индексам токена
                if Rez[1]==True:
                    #print(i,'ESS')
                    temp_txt[i]= temp_txt[i]+' '+temp_txt[i+1]
                    temp_txt.pop([i+1])
                    mas.pop(i+1)
                    mas_nums.pop(i+1)
                    mas_lengs.pop(i+1)
                    
            elif i-1 >=0 and len(mas[i-1]) == 1:#проверка на края списка и длины тега соседа
                rez = In_value(temp_txt[i-1], tables(mas[i]), mas_nums[i])#ф-я проверки соседа по индексам токена
                if Rez[1]==True:
                    #print(i,'QWW')
                    temp_txt[i-1]= temp_txt[i-1]+' '+temp_txt[i]
                    temp_txt.pop(i)
                    mas.pop(i)
                    mas_nums.pop(i)
                    mas_lengs.pop(i)
               
    out = ''
    for i, word in enumerate(temp_txt):
        if mas[i]: # какое условие проверки будет для вывода строки?
            out += ' ' +''.join(word)
            
    #print(temp_txt)
    #print(mas)
    #print(out.strip())
    print(ids[q]+";"+out.strip())
    #print()
    
    
print(time.time()-s)
