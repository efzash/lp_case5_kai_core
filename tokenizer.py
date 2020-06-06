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


def Tabl_value(token, table):
    f = open(table + ".txt", 'r')
    index = -1
    for line in f:
        index += 1
        chslov = line.strip("\n").split(' ')
        for i in chslov:
            if token == i:
                return(True, index, len(chslov))
    
    return(False, None, None)
    

#for i in range(len(bad)):
for i in range(3484):
    #обработка каждой строки
    tokens = tag(tokenizer(bad[i])) 
    #генератор токенов
    temp_m = []
    for t in tokens:
        temp_m.append(t)
    
    mas = []#список списков тегов - список принадлежностей токена к опр категории (таблице фиас)
    mas_nums = []#список списков индексов в каждом теге - попробуем склеивать слова с одинаковыми тегами по этим индексам
    
    table = [t1,t2,t3,t4,t5,t6,t7,t8,t9]#таблицы названий фиас
    
    for token in temp_m:
        t_vector = [20] * n
        t_vector_i = [20] * n
        
        if token.type == 'INT' and len(token.value)==6:
            t_vector[0] = 1
            mas.append([0])
            Poch_ind(token.value)#обработка почтового индекса
        
        #if token.type == 'RU':
        
        for i, table in enumerate(tables): 
            t_vector[i],t_vector_i[i] = Tabl_value(token, table)

        t_mas = []
        t_mas_i = []
        for i, elem in enumerate(t_vector):
            if elem == True:
                t_mas.append(i)
                t_mas_i.append(t_vector_i[i])

        mas.append(t_mas)
        mas_nums.append(t_mas_i)
    
    for elem in mas:
        if 
        
            


print(time.time()-s)
