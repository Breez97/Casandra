from cassandra.cluster import Cluster
from tkinter import *
from tkinter import ttk
from tkinter.messagebox import showerror, showinfo


def clear_packs(packs):
    if len(packs) != 0:
        for i in range(0, len(packs) - 1):
            packs[i].pack_forget()
        packs.clear()

def update_window(root, packs):
    clear_packs(packs)
    
    root.title('Вставка данных')

def main_window(root, packs):

    def button_insert_clicked():
        update_window(root, packs)

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


def ui():
    root = Tk()
    root.resizable(False, False)
    root['bg'] = '#CCCCFF'

    packs = []

    main_window(root, packs)

    root.mainloop()


def main():
    ui()


if __name__ == '__main__':
    main()