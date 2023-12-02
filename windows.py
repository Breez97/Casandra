from functions import *
from imports import *

#Кнопка "Назад"
def button_back_on_window(root, packs):
    def button_back_clicked():
        main_window(root, packs)
    
    button_back = Button(root, text='Вернуться назад', command=button_back_clicked)
    button_back.pack(pady=10)
    button_back.config(font='Arial 12 bold', bg='#CCCCFF')
    packs.append(button_back)

#Главное окно
def main_window(root, packs):

    def button_insert_clicked():
        insert_window(root, packs)
    
    def button_select_clicked():
        select_window(root, packs)
    
    def button_update_clicked():
        update_window(root, packs)
    
    def button_delete_clicked():
        delete_window(root, packs)
    
    def button_quit_clicked():
        root.destroy()    

    clear_packs(packs)

    root.title('Окно взаимодействия с базой данных')
    root.geometry(f'450x350+{(root.winfo_screenwidth() - 450) // 2}+{(root.winfo_screenheight() - 350) // 2}')
    connection_label = Label(root, text='Выполнено подключение\n к базе данных JOBS', font='Arial 15 bold', bg='#CCCCFF')
    connection_label.pack(pady=10)
    packs.append(connection_label)

    #Кнопка "INSERT"
    button_insert = Button(root, text='Вставить запись (INSERT)', command=button_insert_clicked)
    button_insert.pack(pady=10)
    button_insert.config(font='Arial 12 bold', bg='#CCCCFF')
    packs.append(button_insert)

    #Кнопка "SELECT"
    button_select = Button(root, text='Выборка данных (SELECT)', command=button_select_clicked)
    button_select.pack(pady=10)
    button_select.config(font='Arial 12 bold', bg='#CCCCFF')
    packs.append(button_select)

    #Кнопка "UPDATE"
    button_update = Button(root, text='Обновить данные (UPDATE)', command=button_update_clicked)
    button_update.pack(pady=10)
    button_update.config(font='Arial 12 bold', bg='#CCCCFF')
    packs.append(button_update)

    #Кнопка "DELETE"
    button_delete = Button(root, text='Удалить данные (DELETE)', command=button_delete_clicked)
    button_delete.pack(pady=10)
    button_delete.config(font='Arial 12 bold', bg='#CCCCFF')
    packs.append(button_delete)

    #Кнопка "QUIT"
    button_quit = Button(root, text='Выйти', command=button_quit_clicked)
    button_quit.pack(pady=10)
    button_quit.config(font='Arial 12 bold', bg='#CCCCFF')
    packs.append(button_quit)

#Окно выборки данных
def select_window(root, packs):

    def button_make_select_clicked():
        result_list.configure(state='normal')
        result_list.delete(1.0, END)
        
        query = select_entry.get()
        query_result = query_processing(query)

        result_list.insert(END, query_result)
        result_list.yview(END)
        result_list.configure(state='disabled')


    clear_packs(packs)

    root.title('Выборка данных')
    root.geometry(f'650x415+{(root.winfo_screenwidth() - 650) // 2}+{(root.winfo_screenheight() - 415) // 2}')

    main_label = Label(root, text='Выполнить выборку данных (SELECT)', font='Arial 12 bold', bg='#CCCCFF')
    main_label.pack(pady=10)
    packs.append(main_label)

    select_label = Label(root, text='Введите запрос на выборку', font='Arial 12 bold', bg='#CCCCFF')
    select_label.pack(pady=10)
    packs.append(select_label)

    select_entry = Entry(root, font='Arial 12', width=35)
    select_entry.pack(pady=10)
    packs.append(select_entry)

    button_make_select = Button(root, text='SELECT', command=button_make_select_clicked)
    button_make_select.pack(pady=10)
    button_make_select.config(font='Arial 12 bold', bg='#CCCCFF')
    packs.append(button_make_select)

    result_list = scrolledtext.ScrolledText(root, width=70, height=10)
    result_list.pack()
    packs.append(result_list)

    button_back_on_window(root, packs)
