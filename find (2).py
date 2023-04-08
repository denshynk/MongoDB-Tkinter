import pymongo
import json
import os

client = pymongo.MongoClient("mongodb+srv://user:12345@cluster0.yezzjjp.mongodb.net/?retryWrites=true&w=majority")
db = client.list

def find_subdivision():
    res_s = db.subdivision_list.find()
    l = list(res_s)
    with open("subdivision_list.json", "w", encoding= "utf-8") as outfile:
       json.dump(l, outfile, sort_keys=True, indent=4, ensure_ascii=False)
       
def find_workers():   
    res_w = db.workers_list.find()
    l = list(res_w)
    with open("workers_list.json", "w", encoding= "utf-8") as outfile:
       json.dump(l, outfile, sort_keys=True, indent=4, ensure_ascii=False)

find_workers()
find_subdivision()