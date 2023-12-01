from functions import *
from imports import *

#Окно добавления записи (INSERT)
def insert_window(root, packs):

    def button_back_clicked():
        main_window(root, packs)

    clear_packs(packs)
    
    root.title('Вставка данных')

    #Кнопка "Back"
    button_back = Button(root, text='Вернуться назад', command=button_back_clicked)
    button_back.pack(pady=10)
    button_back.config(font='Arial 12 bold', bg='#CCCCFF')
    packs.append(button_back)

#Главное окно
def main_window(root, packs):

    def button_insert_clicked():
        insert_window(root, packs)
    
    def button_quit_clicked():
        root.destroy()

    clear_packs(packs)

    root.title('Окно взаимодействия с базой данных')
    root.geometry('450x350+550+200')
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

    #Кнопка "QUIT"
    button_quit = Button(root, text='Выйти', command=button_quit_clicked)
    button_quit.pack(pady=10)
    button_quit.config(font='Arial 12 bold', bg='#CCCCFF')
    packs.append(button_quit)