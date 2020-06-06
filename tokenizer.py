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
#tokens_list=[]
s = time.time()

def Poch_ind(token):
    pass
def Country(token):
    return(True,index)
    
def Subject(token):
    pass
def City(token):
    pass
def Selo(token):
    pass
def Rn_type(token):
    pass
def Rn_name(token):
    pass
def Street_type(token):
    pass
def Street(token):
    pass

def Tabl_value(token, table):
    return(True,index)
    

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
    
    for token in temp_m:
        t_vector = [20] * n
        
        if token.type == 'INT' and len(token.value)==6:
            t_vector[0] = 1
            mas.append([0])
            Poch_ind(token.value)#обработка почтового индекса
        
        if token.type == 'RU':
            
            country(token.value)
            
            """
            t_vector[1].append(country(token.value))
            t_vector[1].append(subject(token.value))
            t_vector[1].append( city(token.value))
            t_vector[1].append(selo(token.value))
            t_vector[1].append( rn_type(token.value))
            t_vector[1].append( rn_name(token.value))
            t_vector[1].append( street_type(token.value))
            t_vector[1].append( street(token.value))
            """
            
            for elem in t_vector:
                if elem == 1:
            mas1
            
            mas.append(mas1)
        
        for mas in 
            #обл/респ/ано
            #город
            #гск?
            #поселок/деревня
            #улица
            #территория
            #СНТ
            #ПЕР
            #
            
            
        
    #tokens_list.append(temp_m)

print(time.time()-s)