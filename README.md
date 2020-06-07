# lp_case5_kai_core
Code for case 5 (Hackathon # 1) - KAI core

LEARNGOOD.ipynb - код с изучением файлов bad.csv и good.csv, включающий составление Bag of words и перекрёстный анализ.
tokenizer.py - токенизатор  
website - сайт для загрузки csv файла и получения результата обработки   
TABLNEW - предобработанные данные из  ФИАС с названиями адресообразующих элементов  
address_processing.ipynb - основной код нашего проекта. Первый блок исходного кода посвящён загрузке и предварительной обработке набора "плохих" адресов. Второй блок исходного кода посвящён токенизации полученных предобработанных адресов и осуществления их "тегирования". Тегирование осуществлено на основе таблиц, специально сформированных из базы ФИАС за время хакатона. На основе вычисленных тегов был произведён отбор токенов из сформированных строк адреса. 

Обработанные адреса записаны в файле result_Kazan Artificial Intelligence core.csv в столбце processed address. 
!!! В АРХИВЕ result_Kazan Artificial Intelligence core.rar НАХОДИТСЯ result_Kazan Artificial Intelligence core.csv

В папке result_without_ecran на всякий случай загружен result_Kazan Artificial Intelligence core.csv без экранов-кавычек (")
