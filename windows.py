from functions import *
from imports import *

cluster = Cluster()
session = cluster.connect('jobs')

#Кнопка "Назад"
def button_back_on_main_window(root, packs):
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

#Окно выбора бд для добавления записей
def insert_window(root, packs):
    def button_vacancy_clicked():
        insert_window_query(root, packs, 'vacancy')
    
    def button_employer_clicked():
        insert_window_query(root, packs, 'employer')
    
    def button_candidate_clicked():
        insert_window_query(root, packs, 'candidate')


    clear_packs(packs)

    root.title('Добавление данных')
    root.geometry(f'400x270+{(root.winfo_screenwidth() - 400) // 2}+{(root.winfo_screenheight() - 270) // 2}')
    choose_db_label = Label(root, text='Выберите таблицу для добавления данных', font='Arial 12 bold', bg='#CCCCFF')
    choose_db_label.pack(pady=10)
    packs.append(choose_db_label)

    #Кнопка 'Vacancy'
    button_vacancy = Button(root, text='Vacancy', command=button_vacancy_clicked)
    button_vacancy.pack(pady=10)
    button_vacancy.config(font='Arial 12 bold', bg='#CCCCFF')
    packs.append(button_vacancy)

    #Кнопка 'Employer'
    button_employer = Button(root, text='Employer', command=button_employer_clicked)
    button_employer.pack(pady=10)
    button_employer.config(font='Arial 12 bold', bg='#CCCCFF')
    packs.append(button_employer)

    #Кнопка 'Candidate'
    button_candidate = Button(root, text='Candidate', command=button_candidate_clicked)
    button_candidate.pack(pady=10)
    button_candidate.config(font='Arial 12 bold', bg='#CCCCFF')
    packs.append(button_candidate)

    button_back_on_main_window(root, packs)

#Вставка данных
def insert_window_query(root, packs, title):
    def button_back_insert_clicked():
        insert_window(root, packs)
    
    def button_insert_query_clicked():
        if title == 'vacancy':
            vacancy_title = vacancy_title_entry.get()
            vacancy_description = vacancy_description_entry.get("1.0", "end-1c")
            vacancy_status = vacancy_combo_box_statuses.get()
            vacancy_salary = vacancy_salary_entry.get()

            insert_vacancy(vacancy_title, vacancy_description, vacancy_status, vacancy_salary)

        if title == 'employer':
            employer_vacancy_title = combo_box_titles.get()
            employer_title = employer_title_entry.get()
            employer_description = employer_description_entry.get("1.0", "end-1c")
            employer_address = employer_address_entry.get()

            insert_employer(employer_vacancy_title, employer_title, employer_description, employer_address)
        
        if title == 'candidate':
            candidate_vacancy_title = combo_box_titles.get()
            candidate_name = name_entry.get()
            candidate_gender = combo_box_genders.get()
            candidate_date_of_birth = date_of_birth_entry.get()

            insert_candidate(candidate_vacancy_title, candidate_name, candidate_gender, candidate_date_of_birth)

    clear_packs(packs)

    root.title(f'Добавление данных в {title}')
    root.geometry(f'450x350+{(root.winfo_screenwidth() - 450) // 2}+{(root.winfo_screenheight() - 350) // 2}')
    main_label = Label(root, text=f'Выбрана: {title}', font='Arial 12 bold', bg='#CCCCFF')
    main_label.pack(pady=10)
    packs.append(main_label)

    form_frame = Frame(root, bg='#CCCCFF')
    form_frame.pack(expand=True)
    packs.append(form_frame)

    if title == 'vacancy':
        root.geometry(f'450x375+{(root.winfo_screenwidth() - 450) // 2}+{(root.winfo_screenheight() - 375) // 2}')
        vacancy_title_label = Label(form_frame, text='Название вакансии : ', font='Arial 12 bold', bg='#CCCCFF')
        vacancy_title_label.grid(row=0, column=0, sticky='w')
        vacancy_title_entry = Entry(form_frame, font='Arial 12')
        vacancy_title_entry.grid(row=0, column=1, sticky='w', pady=10)

        vacancy_description_label = Label(form_frame, text='Описание : ', font='Arial 12 bold', bg='#CCCCFF')
        vacancy_description_label.grid(row=1, column=0, sticky='w')
        vacancy_description_entry = Text(form_frame, font='Arial 12', width=20, height=3)
        vacancy_description_entry.grid(row=1, column=1, sticky='w', pady=10)

        vacancy_status_label = Label(form_frame, text='Статус : ', font='Arial 12 bold', bg='#CCCCFF')
        vacancy_status_label.grid(row=2, column=0, sticky='w')
        statuses = ['True', 'False']
        status_var = StringVar(value=statuses[0])
        vacancy_combo_box_statuses = ttk.Combobox(form_frame, font='Arial 12', textvariable=status_var, values=statuses, state='readonly')
        vacancy_combo_box_statuses.grid(row=2, column=1, sticky='w', pady=10)

        vacancy_salary_label = Label(form_frame, text='Зарплата : ', font='Arial 12 bold', bg='#CCCCFF')
        vacancy_salary_label.grid(row=3, column=0, sticky='w')
        vacancy_salary_entry = Entry(form_frame, font='Arial 12')
        vacancy_salary_entry.grid(row=3, column=1, sticky='w', pady=10)
    
    if title == 'employer':
        root.geometry(f'550x375+{(root.winfo_screenwidth() - 550) // 2}+{(root.winfo_screenheight() - 375) // 2}')

        vacancy_titles = choose_free_vacancies()

        vacancy_title_label = Label(form_frame, text='Выберите название вакансии : ', font='Arial 12 bold', bg='#CCCCFF')
        vacancy_title_label.grid(row=0, column=0, sticky='w')
        vacancy_var = StringVar(value=vacancy_titles[0])
        combo_box_titles = ttk.Combobox(form_frame, font='Arial 12', textvariable=vacancy_var, values=vacancy_titles, state='readonly')
        combo_box_titles.grid(row=0, column=1, sticky='w', pady=10)

        employer_title_label = Label(form_frame, text='Название компании :', font='Arial 12 bold', bg='#CCCCFF')
        employer_title_label.grid(row=1, column=0, sticky='w')
        employer_title_entry = Entry(form_frame, font='Arial 12')
        employer_title_entry.grid(row=1, column=1, sticky='w', pady=10)

        employer_description_label = Label(form_frame, text='Описание :', font='Arial 12 bold', bg='#CCCCFF')
        employer_description_label.grid(row=2, column=0, sticky='w')
        employer_description_entry = Text(form_frame, font='Arial 12', width=20, height=3)
        employer_description_entry.grid(row=2, column=1, sticky='w', pady=10)

        employer_address_label = Label(form_frame, text='Адрес :', font='Arial 12 bold', bg='#CCCCFF')
        employer_address_label.grid(row=3, column=0, sticky='w')
        employer_address_entry = Entry(form_frame, font='Arial 12')
        employer_address_entry.grid(row=3, column=1, sticky='w')
    
    if title == 'candidate':
        root.geometry(f'550x375+{(root.winfo_screenwidth() - 550) // 2}+{(root.winfo_screenheight() - 375) // 2}')

        vacancy_titles = choose_vacancies()

        vacancy_title_label = Label(form_frame, text='Выберите название вакансии : ', font='Arial 12 bold', bg='#CCCCFF')
        vacancy_title_label.grid(row=0, column=0, sticky='w')
        vacancy_var = StringVar(value=vacancy_titles[0])
        combo_box_titles = ttk.Combobox(form_frame, font='Arial 12', textvariable=vacancy_var, values=vacancy_titles, state='readonly')
        combo_box_titles.grid(row=0, column=1, sticky='w', pady=10)

        name_label = Label(form_frame, text='Введите имя : ', font='Arial 12 bold', bg='#CCCCFF')
        name_label.grid(row=1, column=0, sticky='w')
        name_entry = Entry(form_frame, font='Arial 12')
        name_entry.grid(row=1, column=1, sticky='w')

        gender_label = Label(form_frame, text='Выберите пол : ', font='Arial 12 bold', bg='#CCCCFF')
        gender_label.grid(row=2, column=0, sticky='w')
        genders = ['Male', 'Female']
        gender_var = StringVar(value=genders[0])
        combo_box_genders = ttk.Combobox(form_frame, font='Arial 12', textvariable=gender_var, values=genders, state='readonly')
        combo_box_genders.grid(row=2, column=1, sticky='w', pady=10)

        date_of_birth_label = Label(form_frame, text='Введите дату рождения : ', font='Arial 12 bold', bg='#CCCCFF')
        date_of_birth_label.grid(row=3, column=0, sticky='w')
        date_of_birth_entry = Entry(form_frame, font='Arial 12')
        date_of_birth_entry.grid(row=3, column=1, sticky='w', pady=10)


    button_insert_query = Button(root, text='Добавить', command=button_insert_query_clicked)
    button_insert_query.pack(pady=10)
    button_insert_query.config(font='Arial 12 bold', bg='#CCCCFF')
    packs.append(button_insert_query)

    button_back_insert = Button(root, text='Вернуться назад', command=button_back_insert_clicked)
    button_back_insert.pack(pady=10)
    button_back_insert.config(font='Arial 12 bold', bg='#CCCCFF')
    packs.append(button_back_insert)

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

    button_back_on_main_window(root, packs)
