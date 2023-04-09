import tkinter as tk
import pymongo
import json

client = pymongo.MongoClient("mongodb+srv://user:12345@cluster0.yezzjjp.mongodb.net/?retryWrites=true&w=majority")
db = client.list


def find_subdivision():
    client = pymongo.MongoClient("mongodb+srv://user:12345@cluster0.yezzjjp.mongodb.net/?retryWrites=true&w=majority")
    db = client.list
    res_s = db.subdivision_list.find()
    l = list(res_s)
    with open("subdivision_list.json", "w", encoding= "utf-8") as outfile:
       json.dump(l, outfile, sort_keys=True, indent=4, ensure_ascii=False)
    return l
       
def find_workers():
    client = pymongo.MongoClient("mongodb+srv://user:12345@cluster0.yezzjjp.mongodb.net/?retryWrites=true&w=majority")
    db = client.list
    res_w = db.workers_list.find()
    l = list(res_w)
    with open("workers_list.json", "w", encoding= "utf-8") as outfile:
       json.dump(l, outfile, sort_keys=True, indent=4, ensure_ascii=False)
    return l

def calc_pos(root):
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    window_height = 600
    window_width = 900
    x_cordinate = int((screen_width/2) - (window_width/2))
    y_cordinate = int((screen_height/2) - (window_height/2))
    return window_width, window_height, x_cordinate, y_cordinate

def fetch_table(name):
    table = []
    if (True):
        
        if (name == 'workers'):  
            for w in find_workers():
                table.append((w['_id'], w["worker_name"], w["date_of_birth"], w["date_of_servece"], w["email"], w["adress"], w["telephone_number"], w["salary"]))
            return table
        elif( name == 'subdivisions'):            
            for s in find_subdivision():
                table.append(( s['_id'], s['organization_name'], s['subdivision_name'], s['number_of_workers']))
            return table
    


def load_frame1(root):
    #Закриваємо минуле вікно, якщо воно є
    if (root):
        root.destroy()
    root1 = tk.Tk()
    root1.title('Laboratory work one by 5th team')
    window_width, window_height, x_cordinate, y_cordinate = calc_pos(root1)
    #Розміщуємо вікно по центру екрану
    root1.geometry("{}x{}+{}+{}".format(window_width,
                   window_height, x_cordinate, y_cordinate))
    all_tables = [ 'workers', 'subdivisions'] 
    arr = []
    arr.append(fetch_table('workers'))
    arr.append(fetch_table('subdivisions'))
    frame1 = tk.Frame(root1, bg="#8a6284")
    frame1.pack(fill="both", expand=1)
    #Заголовок - постановка завдання
    
    tk.Label(frame1,
             text="Інформаційна система автоматизації регіональних представництв фірми відповідно до розташування підрозділів, відділів та працівників, включаючи підпорядкованість",
             bg="#8a6284",
             fg="white",
             font=("TkMenuFont", 20),
             wraplength=800
             ).pack()
    
    tk.Button(
        frame1,
        text="CLICK TO LOAD WORKERS TABLE", 
        font=("TkHeadingFont", 20),
        bg="#47273c",
        fg="white",
        cursor="hand2",
        activebackground="#83859a",
        activeforeground="black",
        command=lambda: load_frame2(all_tables[0], arr[0], root1)).pack(pady=20)
    
    tk.Button(
        frame1,
        text="CLICK TO LOAD SUBDIVISION TABLE",
        font=("TkHeadingFont", 20),
        bg="#47273c",
        fg="white",
        cursor="hand2",
        activebackground="#83859a",
        activeforeground="black",
        command=lambda: load_frame2(all_tables[1], arr[1], root1)).pack(pady=20)
    
    root1.mainloop()
    
def get_col_names(name):
    worker_col = ['worker_id', 'worker_name', 'date_of_birth', ' date_of_servece', 'email', 'adress', 'telephone_number', 'salary']
    subdivision_col = ['subdivision_id', 'organization_name', 'subdivision_name', 'number_of_workers']
    if (name=='workers'):
        return worker_col
    else:
        return subdivision_col 
    
def load_frame2(title, table, root):
    cols = get_col_names(title)
    if root:
        root.destroy()
    root2 = tk.Tk()
    root2.title(title)
    ancho, alto, x_cordinate, y_cordinate = calc_pos(root2)
    root2.geometry("{}x{}+{}+{}".format(ancho, alto, x_cordinate, y_cordinate))
    #Створюємо головний фрейм
    main_frame = tk.Frame(root2, width=ancho, height=alto)
    main_frame.place(x=0, y=0)
    #Створюємо полотно
    my_canvas = tk.Canvas(main_frame, width=ancho+5, height=alto, bg="#8a6284")
    my_canvas.place(x=0, y=0)
    #Додаємо полоси прокрутки
    my_scrollbar = tk.Scrollbar(
        main_frame, orient="vertical", command=my_canvas.yview)
    my_scrollbar.place(x=885, y=0, height=alto)
    my_scrollbar_h = tk.Scrollbar(
        main_frame, orient="horizontal", command=my_canvas.xview)
    my_scrollbar_h.place(x=0, y=585, width=ancho)

    my_canvas.configure(yscrollcommand=my_scrollbar.set)
    my_canvas.configure(xscrollcommand=my_scrollbar_h.set)
    my_canvas.bind('<Configure>', lambda e: my_canvas.configure(
        scrollregion=my_canvas.bbox("all")))
    #Прокручуємо при взаємодії з мишою
    def _on_mouse_wheel(event):
        my_canvas.yview_scroll(-1 * int((event.delta / 120)), "units")

    my_canvas.bind_all("<MouseWheel>", _on_mouse_wheel)
    #Додаємо основний фрейм до полотна
    frame2 = tk.Frame(my_canvas, bg="#8a6284")
    frame2.pack(fill="both", expand=1)
    my_canvas.create_window((0, 0), window=frame2, anchor="nw")
    
    row = 0
    #Виводимо назву таблиці
    tk.Label(frame2,
             text=title,
             bg="#8a6284",
             fg="white",
             font=("TkMenuFont", 16),
             wraplength=800
             ).grid(row=row, column=1)
    row = +1
    col = 0
    #Виводимо назви колонок
    for i in cols:
        tk.Label(frame2,
                 text=i,
                 bg="#8a6284",
                 fg="white",
                 font=("TkHeadingFont", 12),
                 wraplength=140,
                 padx=10
                 ).grid(row=row, column=col, padx=15)
        col += 1
    row += 1
    #Відобразаємо зміст таблиці
    for i in table:
        col = 0
        for j in i:
            tk.Label(frame2,
                     text=j,
                     bg="#8a6284",
                     fg="white",
                     font=("TkMenuFont", 10),
                     wraplength=100,
                     padx=10
                     ).grid(row=row, column=col)
            col += 1
        row += 1
    #Кнопка для переходу на минулу сторінку
    tk.Button(
        frame2,
        text="CLICK TO GET BACK",
        font=("TkHeadingFont", 20),
        bg="#47273c",
        fg="white",
        cursor="hand2",
        activebackground="#83859a",
        activeforeground="black",
        command=lambda: load_frame1(root2)
    ).grid(row=row, column=1)
    row += 1
    # Напис + поле + кнопка для видалення по айді
    tk.Label(frame2,
             text="id of item to delete",
             bg="#8a6284",
             fg="white",
             ).grid(row=row, column=3)
    entry_id = tk.Entry(frame2, width=20)
    entry_id.grid(row=row+1, column=3, pady=10)
    tk.Button(
        frame2,
        text="DELETE NOTE",
        font=("TkHeadingFont", 20),
        bg="#47273c",
        fg="white",
        cursor="hand2",
        activebackground="#83859a",
        activeforeground="black",
        command=lambda: submit_delete(root2, title, entry_id, cols, title)
    ).grid(row=row+2, column=3, pady=15)
    entries = []
    # Поля + кнопка для створення запису + кнопка для редагування
    for i in cols:
        tk.Label(frame2,
                 text=i,
                 bg="#8a6284",
                 fg="white",
                 ).grid(row=row, column=0)
        entry = tk.Entry(frame2, width=50)
        entry.grid(row=row, column=1, pady=10)
        entries.append(entry)
        row += 1

    tk.Button( 
        frame2,
        text="CREATE NOTE",
        font=("TkHeadingFont", 20),
        bg="#47273c",
        fg="white",
        cursor="hand2",
        activebackground="#83859a",
        activeforeground="black",
        command=lambda: submit_add(entries, title, cols, title, root2)
    ).grid(row=row, column=1, pady=15)
    row += 1
    tk.Button(
        frame2,
        text="EDIT NOTE",
        font=("TkHeadingFont", 20),
        bg="#47273c",
        fg="white",
        cursor="hand2",
        activebackground="#83859a",
        activeforeground="black",
        command=lambda: submit_edit(entries, title, cols, title, root2)
    ).grid(row=row, column=1, pady=15)
    root2.mainloop()

def submit_add(entries, title1, cols, title, root):
    client = pymongo.MongoClient("mongodb+srv://user:12345@cluster0.yezzjjp.mongodb.net/?retryWrites=true&w=majority")
    db = client.list
    flag = True
    for entry in entries:
        #Вивести попередження, якщо поле пусте або з помилкою
        if (not entry.get().strip() or entry.get() == "Заповніть поле!"):
            #Якщо хоч одне поле невалідне - підіймаємо флаг
            flag = False
            entry.delete(0, "end")
            entry.insert(0, "Заповніть поле!")
    #Якщо всі поля валідні
    if flag:
        if (title1=='workers'):
            db.workers_list.insert_one({"_id": int(entries[0].get()), 'worker_name': entries[1].get(), 'date_of_birth': entries[2].get(), 'date_of_servece': entries[3].get(), 'email': entries[4].get(),'adress': entries[5].get(), 'telephone_number': entries[6].get(), 'salary': int(entries[7].get())})
            table = fetch_table('workers')
        elif (title1=='subdivisions'):
            db.subdivision_list.insert_one({"_id": int(entries[0].get()), 'organization_name': entries[1].get(), 'subdivision_name': entries[2].get(), 'number_of_workers': int(entries[3].get())})
            table = fetch_table('subdivision')
        #Перезавантажити вікно, щоб відобразити нові дані
    load_frame2(title, table, root)

def submit_delete(root, title1, entry_id, cols, title):
    client = pymongo.MongoClient("mongodb+srv://user:12345@cluster0.yezzjjp.mongodb.net/?retryWrites=true&w=majority")
    db = client.list
    #Якщо поле айді не порожнє
    if (entry_id.get().strip()):
        if (title1=='workers'):
            db.workers_list.delete_one({"_id" : int(entry_id.get())})
            table = fetch_table('workers')
        elif (title1=='subdivisions'):
            db.subdivision_list.delete_one({"_id" : int(entry_id.get())})
            table = fetch_table('subdivisions')
        #Відкриваємо вікно з відображеними змінами
    #Якщо порожнє поле
    else:
        entry_id.delete(0, "end")
        entry_id.insert(0, "Заповніть поле!")
    load_frame2(title, table, root)

#Змінити запис таблиці
def submit_edit(entries, title1, cols, title, root):
    if entries[0].get():
        if (title1=='workers'):
            worker = {"_id": int(entries[0].get())}
            entries.pop(0)
            for e in range (len(entries)):
                #worker_name date_of_birth date_of_servece email adress telephone_number salary 
                if (entries[e].get()):
                    if (e == 0):
                        newvalue = {"$set": {"worker_name": f"{entries[e].get()}" }}
                        db.workers_list.update_one(worker, newvalue)
                    elif (e == 1):
                        newvalue = {"$set": {"date_of_birth": f"{entries[e].get()}" }}
                        db.workers_list.update_one(worker, newvalue)
                    elif (e == 2):
                        newvalue = {"$set": {"date_of_servece": f"{entries[e].get()}" }}
                        db.workers_list.update_one(worker, newvalue)
                    elif (e == 3):
                        newvalue =  {"$set": {"email": f'{entries[e].get()}' }}
                        db.workers_list.update_one(worker, newvalue)
                    elif (e == 4):
                        newvalue =  {"$set": {"adress": f'{entries[e].get()}' }}
                        db.workers_list.update_one(worker, newvalue)
                    elif (e == 5):
                        newvalue = {"$set": {"telephone_number": f'{entries[e].get()}' }}
                        db.workers_list.update_one(worker, newvalue)
                    elif (e == 6):
                        newvalue = {"$set": {"salary": int(entries[e].get()) }}
                        db.workers_list.update_one(worker, newvalue)
            table = fetch_table('workers')
            
        elif (title1=='subdivisions'):
            subdivision = {"_id": int(entries[0].get())}
            entries.pop(0)
            for e in range (len(entries)):
                #organization_name subdivision_name principal_id number_of_workers
                if (entries[e].get()):
                    if (e == 0):
                        newvalue = {"$set": {"organization_name": f"{entries[e].get()}" }}
                        db.subdivision_list.update_one(subdivision, newvalue)
                    elif (e == 1):
                        newvalue = {"$set": {"subdivision_name": f"{entries[e].get()}"}} 
                        db.subdivision_list.update_one(subdivision, newvalue)
                    elif (e == 2):
                        newvalue = {"$set": {"number_of_workers": int(entries[e].get()) }}
                        db.subdivision_list.update_one(subdivision, newvalue)
                
            table = fetch_table('subdivisions') 
    #Якщо поле з айді порожнє                                                   
    else:
        entries[0].delete(0, "end")
        entries[0].insert(0, "Заповніть обов'язкове поле!")

load_frame1(False)


