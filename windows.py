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

#Окно выбора бд для изменения данных
def update_window(root, packs):
    def button_vacancy_clicked():
        update_window_query(root, packs, 'vacancy')
    
    def button_employer_clicked():
        update_window_query(root, packs, 'employer')
    
    def button_candidate_clicked():
        update_window_query(root, packs, 'candidate')


    clear_packs(packs)

    root.title('Обновление данных')
    root.geometry(f'400x270+{(root.winfo_screenwidth() - 400) // 2}+{(root.winfo_screenheight() - 270) // 2}')
    choose_db_label = Label(root, text='Выберите таблицу для обновления данных', font='Arial 12 bold', bg='#CCCCFF')
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

#Обновление данных
def update_window_query(root, packs, title):
    
    def button_back_update_clicked():
        update_window(root, packs)
    
    def update_vacancy_table(old_values):
        update_vacancy(root, packs, old_values)
    
    def update_employer_table(old_values):
        update_employer(root, packs, old_values)
    
    def update_candidate_table(old_values):
        update_candidate(root, packs, old_values)

    clear_packs(packs)

    root.title(f'Обновление данных в {title}')
    main_label = Label(root, text=f'Выбрана: {title}', font='Arial 12 bold', bg='#CCCCFF')
    main_label.pack(pady=10)
    packs.append(main_label)

    y_size = 120
    root.geometry(f'600x{y_size}+{(root.winfo_screenwidth() - 450) // 2}+{(root.winfo_screenheight() - y_size) // 2}')

    form_frame = Frame(root, bg='#CCCCFF')
    form_frame.pack(expand=True)
    packs.append(form_frame)

    if title == 'vacancy':
        length = 0
        columns = ('Title', 'Description', 'Status', 'Salary')
        table = ttk.Treeview(columns=columns, show='headings')
        table.pack()
        packs.append(table)

        style = ttk.Style()
        style.configure("Treeview", rowheight=50)

        table.tag_configure('data', background='#CCCCEF')
        table.heading('Title', text='Название')
        table.heading('Description', text='Описание')
        table.heading('Status', text='Статус')
        table.heading('Salary', text='Зарплата')

        table.column('#1', width=100)
        table.column('#2', width=200)
        table.column('#3', width=100)
        table.column('#4', width=100)

        query_select = "SELECT * FROM vacancy"
        result = session.execute(query_select)
        for row in result.all():
            y_size += 50
            length += 1

            title = row[4]
            description = row[1]
            status = row[3]
            salary = row[2]

            parsed_record = (title, description, status, salary)
            table.insert('', END, values=parsed_record, tags=('data',))
        table['height'] = length

        root.geometry(f'600x{y_size}+{(root.winfo_screenwidth() - 600) // 2}+{(root.winfo_screenheight() - y_size) // 2}')

        def item_selected(event):
            selected_string = ''
            for selected in table.selection():
                item = table.item(selected)
                string = item['values']
                old_values = string
                update_vacancy_table(old_values)
        table.bind("<<TreeviewSelect>>", item_selected)
    
    if title == 'employer':
        length = 0
        columns = ('Vacancy', 'Title', 'Description', 'Address')
        table = ttk.Treeview(columns=columns, show='headings')
        table.pack()
        packs.append(table)

        style = ttk.Style()
        style.configure("Treeview", rowheight=50)

        table.tag_configure('data', background='#CCCCEF')
        table.heading('Vacancy', text='Вакансия')
        table.heading('Title', text='Название')
        table.heading('Description', text='Описание')
        table.heading('Address', text='Адрес')

        table.column('#1', width=120)
        table.column('#2', width=100)
        table.column('#3', width=200)
        table.column('#4', width=100)

        query_select = "SELECT * FROM employer"
        result = session.execute(query_select)
        for row in result.all():
            y_size += 50
            length += 1

            query_vacancy = f"SELECT title FROM vacancy WHERE id={row[4]}"
            result_vacancy = session.execute(query_vacancy)
            title = [row_title[0] for row_title in result_vacancy.all()]
            
            vacancy = title[0]
            title = row[3]
            description = row[2]
            address = row[1]

            parsed_record = (vacancy, title, description, address)
            table.insert('', END, values=parsed_record, tags=('data',))
        table['height'] = length

        root.geometry(f'700x{y_size}+{(root.winfo_screenwidth() - 700) // 2}+{(root.winfo_screenheight() - y_size) // 2}')

        def item_selected(event):
            selected_string = ''
            for selected in table.selection():
                item = table.item(selected)
                string = item['values']
                old_values = string
                update_employer_table(old_values)
        table.bind("<<TreeviewSelect>>", item_selected)
    
    if title == 'candidate':
        length = 0
        columns = ('Vacancy', 'Name', 'Gender', 'DateOfBirth')
        table = ttk.Treeview(columns=columns, show='headings')
        table.pack()
        packs.append(table)

        style = ttk.Style()
        style.configure("Treeview", rowheight=50)

        table.tag_configure('data', background='#CCCCEF')
        table.heading('Vacancy', text='Вакансия')
        table.heading('Name', text='Имя')
        table.heading('Gender', text='Пол')
        table.heading('DateOfBirth', text='Дата рождения')

        table.column('#1', width=120)
        table.column('#2', width=100)
        table.column('#3', width=200)
        table.column('#4', width=100)

        query_select = "SELECT * FROM candidate"
        result = session.execute(query_select)
        for row in result.all():
            y_size += 50
            length += 1

            query_vacancy = f"SELECT title FROM vacancy WHERE id={row[4]}"
            result_vacancy = session.execute(query_vacancy)
            title = [row_title[0] for row_title in result_vacancy.all()]

            vacancy = title[0]
            name = row[3]
            gender = row[2]
            date_of_birth = row[1]

            parsed_record = (vacancy, name, gender, date_of_birth)
            table.insert('', END, values=parsed_record, tags=('data',))
        table['height'] = length

        root.geometry(f'700x{y_size}+{(root.winfo_screenwidth() - 700) // 2}+{(root.winfo_screenheight() - y_size) // 2}')

        def item_selected(event):
            selected_string = ''
            for selected in table.selection():
                item = table.item(selected)
                string = item['values']
                old_values = string
                update_candidate_table(old_values)
        table.bind("<<TreeviewSelect>>", item_selected)

    button_back_update = Button(root, text='Вернуться назад', command=button_back_update_clicked)
    button_back_update.pack(pady=10)
    button_back_update.config(font='Arial 12 bold', bg='#CCCCFF')
    packs.append(button_back_update)

#Обновление вакансий
def update_vacancy(root, packs, old_values):
    def button_back_update_clicked():
        update_window_query(root, packs, 'vacancy')
    
    def button_update_vacancy_clicked():
        vacancy_old_title = old_values[0]
        vacancy_title = vacancy_title_entry.get()
        vacancy_description = vacancy_description_entry.get("1.0", "end-1c")
        vacancy_status = vacancy_combo_box_statuses.get()
        vacancy_salary = vacancy_salary_entry.get()

        update_vacancy_query(vacancy_old_title, vacancy_title, vacancy_description, vacancy_status, vacancy_salary)
        update_window_query(root, packs, 'vacancy')

    clear_packs(packs)

    root.title('Обновление вакансии')

    form_frame = Frame(root, bg='#CCCCFF')
    form_frame.pack(expand=True)
    packs.append(form_frame)

    root.geometry(f'450x375+{(root.winfo_screenwidth() - 450) // 2}+{(root.winfo_screenheight() - 375) // 2}')
    vacancy_title_label = Label(form_frame, text='Название вакансии : ', font='Arial 12 bold', bg='#CCCCFF')
    vacancy_title_label.grid(row=0, column=0, sticky='w')
    vacancy_title_var = StringVar()
    vacancy_title_entry = Entry(form_frame, textvariable=vacancy_title_var, font='Arial 12')
    vacancy_title_entry.grid(row=0, column=1, sticky='w', pady=10)
    vacancy_title_var.set(old_values[0])

    vacancy_description_label = Label(form_frame, text='Описание : ', font='Arial 12 bold', bg='#CCCCFF')
    vacancy_description_label.grid(row=1, column=0, sticky='w')
    vacancy_description_entry = Text(form_frame, font='Arial 12', width=20, height=3)
    vacancy_description_entry.grid(row=1, column=1, sticky='w', pady=10)
    vacancy_description_entry.insert("1.0", old_values[1])

    vacancy_status_label = Label(form_frame, text='Статус : ', font='Arial 12 bold', bg='#CCCCFF')
    vacancy_status_label.grid(row=2, column=0, sticky='w')
    statuses = ['True', 'False']
    status_var = StringVar(value=old_values[2])
    vacancy_combo_box_statuses = ttk.Combobox(form_frame, font='Arial 12', textvariable=status_var, values=statuses, state='readonly')
    vacancy_combo_box_statuses.grid(row=2, column=1, sticky='w', pady=10)

    vacancy_salary_label = Label(form_frame, text='Зарплата : ', font='Arial 12 bold', bg='#CCCCFF')
    vacancy_salary_label.grid(row=3, column=0, sticky='w')
    vacancy_salary_var = StringVar()
    vacancy_salary_entry = Entry(form_frame, textvariable=vacancy_salary_var, font='Arial 12')
    vacancy_salary_entry.grid(row=3, column=1, sticky='w', pady=10)
    vacancy_salary_var.set(old_values[3])

    button_update_vacancy = Button(root, text='Обновить', command=button_update_vacancy_clicked)
    button_update_vacancy.pack(pady=10)
    button_update_vacancy.config(font='Arial 12 bold', bg='#CCCCFF')
    packs.append(button_update_vacancy)

    button_back_update = Button(root, text='Вернуться назад', command=button_back_update_clicked)
    button_back_update.pack(pady=10)
    button_back_update.config(font='Arial 12 bold', bg='#CCCCFF')
    packs.append(button_back_update)

#Обновление компаний
def update_employer(root, packs, old_values):
    def button_back_update_clicked():
        update_window_query(root, packs, 'employer')
    
    def button_update_employer_clicked():
        employer_old_title = old_values[1]
        employer_vacancy = combo_box_titles.get()
        employer_title = employer_title_entry.get()
        employer_description = employer_description_entry.get("1.0", "end-1c")
        employer_address = employer_address_entry.get()

        update_employer_query(employer_old_title, employer_vacancy, employer_title, employer_description, employer_address)
        update_window_query(root, packs, 'employer')
    
    clear_packs(packs)

    root.title('Обновление компаний')

    form_frame = Frame(root, bg='#CCCCFF')
    form_frame.pack(expand=True)
    packs.append(form_frame)

    root.geometry(f'550x375+{(root.winfo_screenwidth() - 550) // 2}+{(root.winfo_screenheight() - 375) // 2}')

    vacancy_titles = choose_free_vacancies()

    vacancy_title_label = Label(form_frame, text='Выберите название вакансии : ', font='Arial 12 bold', bg='#CCCCFF')
    vacancy_title_label.grid(row=0, column=0, sticky='w')
    vacancy_var = StringVar(value=old_values[0])
    combo_box_titles = ttk.Combobox(form_frame, font='Arial 12', textvariable=vacancy_var, values=vacancy_titles, state='readonly')
    combo_box_titles.grid(row=0, column=1, sticky='w', pady=10)

    employer_title_label = Label(form_frame, text='Название компании :', font='Arial 12 bold', bg='#CCCCFF')
    employer_title_label.grid(row=1, column=0, sticky='w')
    employer_title_var = StringVar()
    employer_title_entry = Entry(form_frame, textvariable=employer_title_var, font='Arial 12')
    employer_title_entry.grid(row=1, column=1, sticky='w', pady=10)
    employer_title_var.set(old_values[1])

    employer_description_label = Label(form_frame, text='Описание :', font='Arial 12 bold', bg='#CCCCFF')
    employer_description_label.grid(row=2, column=0, sticky='w')
    employer_description_entry = Text(form_frame, font='Arial 12', width=20, height=3)
    employer_description_entry.grid(row=2, column=1, sticky='w', pady=10)
    employer_description_entry.insert("1.0", old_values[2])

    employer_address_label = Label(form_frame, text='Адрес :', font='Arial 12 bold', bg='#CCCCFF')
    employer_address_label.grid(row=3, column=0, sticky='w')
    employer_address_var = StringVar()
    employer_address_entry = Entry(form_frame, textvariable=employer_address_var, font='Arial 12')
    employer_address_entry.grid(row=3, column=1, sticky='w')
    employer_address_var.set(old_values[3])

    button_update_employer = Button(root, text='Обновить', command=button_update_employer_clicked)
    button_update_employer.pack(pady=10)
    button_update_employer.config(font='Arial 12 bold', bg='#CCCCFF')
    packs.append(button_update_employer)

    button_back_update = Button(root, text='Вернуться назад', command=button_back_update_clicked)
    button_back_update.pack(pady=10)
    button_back_update.config(font='Arial 12 bold', bg='#CCCCFF')
    packs.append(button_back_update)

#Обновление кандидата
def update_candidate(root, packs, old_values):
    def button_back_update_clicked():
        update_window_query(root, packs, 'candidate')
    
    def button_update_candidate_clicked():
        candidate_old_name = old_values[1]
        candidate_vacancy = combo_box_titles.get()
        candidate_name = name_entry.get()
        candidate_gender = combo_box_genders.get()
        candidate_date = date_of_birth_entry.get()
        
        update_candidate_query(candidate_old_name, candidate_vacancy, candidate_name, candidate_gender, candidate_date)
        update_window_query(root, packs, 'candidate')

    clear_packs(packs)

    root.title('Обновление кандидатов')

    form_frame = Frame(root, bg='#CCCCFF')
    form_frame.pack(expand=True)
    packs.append(form_frame)

    root.geometry(f'550x375+{(root.winfo_screenwidth() - 550) // 2}+{(root.winfo_screenheight() - 375) // 2}')

    vacancy_titles = choose_vacancies()

    vacancy_title_label = Label(form_frame, text='Выберите название вакансии : ', font='Arial 12 bold', bg='#CCCCFF')
    vacancy_title_label.grid(row=0, column=0, sticky='w')
    vacancy_var = StringVar(value=old_values[0])
    combo_box_titles = ttk.Combobox(form_frame, font='Arial 12', textvariable=vacancy_var, values=vacancy_titles, state='readonly')
    combo_box_titles.grid(row=0, column=1, sticky='w', pady=10)

    name_label = Label(form_frame, text='Введите имя : ', font='Arial 12 bold', bg='#CCCCFF')
    name_label.grid(row=1, column=0, sticky='w')
    name_var = StringVar()
    name_entry = Entry(form_frame, textvariable=name_var, font='Arial 12')
    name_entry.grid(row=1, column=1, sticky='w')
    name_var.set(old_values[1])

    gender_label = Label(form_frame, text='Выберите пол : ', font='Arial 12 bold', bg='#CCCCFF')
    gender_label.grid(row=2, column=0, sticky='w')
    genders = ['Male', 'Female']
    gender_var = StringVar(value=old_values[2])
    combo_box_genders = ttk.Combobox(form_frame, font='Arial 12', textvariable=gender_var, values=genders, state='readonly')
    combo_box_genders.grid(row=2, column=1, sticky='w', pady=10)

    date_of_birth_label = Label(form_frame, text='Введите дату рождения : ', font='Arial 12 bold', bg='#CCCCFF')
    date_of_birth_label.grid(row=3, column=0, sticky='w')
    date_of_birth_var = StringVar()
    date_of_birth_entry = Entry(form_frame, textvariable=date_of_birth_var, font='Arial 12')
    date_of_birth_entry.grid(row=3, column=1, sticky='w', pady=10)
    date_of_birth_var.set(old_values[3])

    button_update_candidate= Button(root, text='Обновить', command=button_update_candidate_clicked)
    button_update_candidate.pack(pady=10)
    button_update_candidate.config(font='Arial 12 bold', bg='#CCCCFF')
    packs.append(button_update_candidate)

    button_back_update = Button(root, text='Вернуться назад', command=button_back_update_clicked)
    button_back_update.pack(pady=10)
    button_back_update.config(font='Arial 12 bold', bg='#CCCCFF')
    packs.append(button_back_update)

#Окно выбора бд для удаления данных
def delete_window(root, packs):
    def button_vacancy_clicked():
        delete_window_query(root, packs, 'vacancy')
    
    def button_employer_clicked():
        delete_window_query(root, packs, 'employer')
    
    def button_candidate_clicked():
        delete_window_query(root, packs, 'candidate')


    clear_packs(packs)

    root.title('Удаление данных')
    root.geometry(f'400x270+{(root.winfo_screenwidth() - 400) // 2}+{(root.winfo_screenheight() - 270) // 2}')
    choose_db_label = Label(root, text='Выберите таблицу для обновления данных', font='Arial 12 bold', bg='#CCCCFF')
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

#Окно удаления данных
def delete_window_query(root, packs, title):
    def button_back_delete_clicked():
        delete_window(root, packs)
    
    def delete_vacancy_table(old_values):
        delete_vacancy_query(old_values[0])
        delete_window_query(root, packs, 'vacancy')
    
    def delete_employer_table(old_values):
        delete_employer_query(old_values[1])
        delete_window_query(root, packs, 'employer')
    
    def delete_candidate_table(old_values):
        delete_candidate_query(old_values[1])
        delete_window_query(root, packs, 'candidate')

    clear_packs(packs)

    root.title(f'Удаление данных в {title}')
    main_label = Label(root, text=f'Выбрана: {title}', font='Arial 12 bold', bg='#CCCCFF')
    main_label.pack(pady=10)
    packs.append(main_label)

    y_size = 120
    root.geometry(f'600x{y_size}+{(root.winfo_screenwidth() - 450) // 2}+{(root.winfo_screenheight() - y_size) // 2}')

    form_frame = Frame(root, bg='#CCCCFF')
    form_frame.pack(expand=True)
    packs.append(form_frame)

    clear_packs(packs)

    root.title(f'Обновление данных в {title}')
    main_label = Label(root, text=f'Выбрана: {title}', font='Arial 12 bold', bg='#CCCCFF')
    main_label.pack(pady=10)
    packs.append(main_label)

    y_size = 120
    root.geometry(f'600x{y_size}+{(root.winfo_screenwidth() - 450) // 2}+{(root.winfo_screenheight() - y_size) // 2}')

    form_frame = Frame(root, bg='#CCCCFF')
    form_frame.pack(expand=True)
    packs.append(form_frame)

    if title == 'vacancy':
        length = 0
        columns = ('Title', 'Description', 'Status', 'Salary')
        table = ttk.Treeview(columns=columns, show='headings')
        table.pack()
        packs.append(table)

        style = ttk.Style()
        style.configure("Treeview", rowheight=50)

        table.tag_configure('data', background='#CCCCEF')
        table.heading('Title', text='Название')
        table.heading('Description', text='Описание')
        table.heading('Status', text='Статус')
        table.heading('Salary', text='Зарплата')

        table.column('#1', width=100)
        table.column('#2', width=200)
        table.column('#3', width=100)
        table.column('#4', width=100)

        query_select = "SELECT * FROM vacancy"
        result = session.execute(query_select)
        for row in result.all():
            y_size += 50
            length += 1

            title = row[4]
            description = row[1]
            status = row[3]
            salary = row[2]

            parsed_record = (title, description, status, salary)
            table.insert('', END, values=parsed_record, tags=('data',))
        table['height'] = length

        root.geometry(f'600x{y_size}+{(root.winfo_screenwidth() - 600) // 2}+{(root.winfo_screenheight() - y_size) // 2}')

        def item_selected(event):
            selected_string = ''
            for selected in table.selection():
                item = table.item(selected)
                string = item['values']
                old_values = string
                delete_vacancy_table(old_values)
        table.bind("<<TreeviewSelect>>", item_selected)
    
    if title == 'employer':
        length = 0
        columns = ('Vacancy', 'Title', 'Description', 'Address')
        table = ttk.Treeview(columns=columns, show='headings')
        table.pack()
        packs.append(table)

        style = ttk.Style()
        style.configure("Treeview", rowheight=50)

        table.tag_configure('data', background='#CCCCEF')
        table.heading('Vacancy', text='Вакансия')
        table.heading('Title', text='Название')
        table.heading('Description', text='Описание')
        table.heading('Address', text='Адрес')

        table.column('#1', width=120)
        table.column('#2', width=100)
        table.column('#3', width=200)
        table.column('#4', width=100)

        query_select = "SELECT * FROM employer"
        result = session.execute(query_select)
        for row in result.all():
            y_size += 50
            length += 1

            query_vacancy = f"SELECT title FROM vacancy WHERE id={row[4]}"
            result_vacancy = session.execute(query_vacancy)
            title = [row_title[0] for row_title in result_vacancy.all()]
            
            vacancy = title[0]
            title = row[3]
            description = row[2]
            address = row[1]

            parsed_record = (vacancy, title, description, address)
            table.insert('', END, values=parsed_record, tags=('data',))
        table['height'] = length

        root.geometry(f'700x{y_size}+{(root.winfo_screenwidth() - 700) // 2}+{(root.winfo_screenheight() - y_size) // 2}')

        def item_selected(event):
            selected_string = ''
            for selected in table.selection():
                item = table.item(selected)
                string = item['values']
                old_values = string
                delete_employer_table(old_values)
        table.bind("<<TreeviewSelect>>", item_selected)
    
    if title == 'candidate':
        length = 0
        columns = ('Vacancy', 'Name', 'Gender', 'DateOfBirth')
        table = ttk.Treeview(columns=columns, show='headings')
        table.pack()
        packs.append(table)

        style = ttk.Style()
        style.configure("Treeview", rowheight=50)

        table.tag_configure('data', background='#CCCCEF')
        table.heading('Vacancy', text='Вакансия')
        table.heading('Name', text='Имя')
        table.heading('Gender', text='Пол')
        table.heading('DateOfBirth', text='Дата рождения')

        table.column('#1', width=120)
        table.column('#2', width=100)
        table.column('#3', width=200)
        table.column('#4', width=100)

        query_select = "SELECT * FROM candidate"
        result = session.execute(query_select)
        for row in result.all():
            y_size += 50
            length += 1

            query_vacancy = f"SELECT title FROM vacancy WHERE id={row[4]}"
            result_vacancy = session.execute(query_vacancy)
            title = [row_title[0] for row_title in result_vacancy.all()]

            vacancy = title[0]
            name = row[3]
            gender = row[2]
            date_of_birth = row[1]

            parsed_record = (vacancy, name, gender, date_of_birth)
            table.insert('', END, values=parsed_record, tags=('data',))
        table['height'] = length

        root.geometry(f'700x{y_size}+{(root.winfo_screenwidth() - 700) // 2}+{(root.winfo_screenheight() - y_size) // 2}')

        def item_selected(event):
            selected_string = ''
            for selected in table.selection():
                item = table.item(selected)
                string = item['values']
                old_values = string
                delete_candidate_table(old_values)
        table.bind("<<TreeviewSelect>>", item_selected)

    button_back_delete = Button(root, text='Вернуться назад', command=button_back_delete_clicked)
    button_back_delete.pack(pady=10)
    button_back_delete.config(font='Arial 12 bold', bg='#CCCCFF')
    packs.append(button_back_delete)

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
