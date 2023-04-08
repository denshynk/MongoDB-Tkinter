import tkinter as tk
import pymongo



def calc_pos(root):
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    window_height = 600
    window_width = 900
    x_cordinate = int((screen_width/2) - (window_width/2))
    y_cordinate = int((screen_height/2) - (window_height/2))
    return window_width, window_height, x_cordinate, y_cordinate

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
    all_tables = ['subdivisions', 'workers'] 
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
        text="CLICK TO LOAD WORKERS TABLE", #CLICK TO LOAD SUBDIVISION TABLE
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
    
    
load_frame1(False)


