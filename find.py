import pymongo
import json

# Файл створенно тільки для отримання вмісту двох таблиць в JSON форматі 

client = pymongo.MongoClient("mongodb+srv://user:12345@cluster0.yezzjjp.mongodb.net/?retryWrites=true&w=majority") # Підкючаємося до кластеру 
db = client.list # Оглошуємо базу данних


def find_subdivision(): # Функція пошуку підпорядкованості 
    l = list(db.subdivision_list.find()) # Оголошуємо елемент та присвоюємо йому список отприманий методом pymondo .find
    with open("subdivision_list.json", "w", encoding= "utf-8") as outfile:
       json.dump(l, outfile, sort_keys=True, indent=4, ensure_ascii=False)
       
def find_workers(): # Функція пошуку 
    l = list(db.workers_list.find()) # Оголошуємо елемент та присвоюємо йому список отприманий методом pymondo .find
    with open("workers_list.json", "w", encoding= "utf-8") as outfile: 
       json.dump(l, outfile, sort_keys=True, indent=4, ensure_ascii=False) 

find_workers()
find_subdivision()