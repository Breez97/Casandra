import uuid
from cassandra.cluster import Cluster
from tkinter.messagebox import showerror, showinfo

cluster = Cluster()
session = cluster.connect('jobs')

#Очищение окна
def clear_packs(packs):
    if len(packs) != 0:
        for i in range(0, len(packs)):
            packs[i].pack_forget()
        packs.clear()

#Выбрать вакансии для компаний
def choose_free_vacancies():
    free_vacancies = []
    query_vacancies_used = "SELECT vacancy_id FROM employer"
    try:
        result = session.execute(query_vacancies_used)
        vacancies_used = [row[0] for row in result.all()]
        for i in range(0, len(vacancies_used)):
            query_select_title = f"SELECT title FROM vacancy WHERE id={vacancies_used[i]}"
            try:
                result_title = session.execute(query_select_title)
                titles = [str(row[0]) for row in result_title.all()]
                free_vacancies.extend(titles)
            except Exception as error:
                showerror(title='Ошибка', message=f'{error}')
    except Exception as error:
        showerror(title='Ошибка', message=f'{error}')
    return free_vacancies

#Выбрать вакансии для кандидатов
def choose_vacancies():
    vacancies = []
    try:
        query_select = "SELECT title FROM vacancy"
        result_select = session.execute(query_select)
        vacancies = [row[0] for row in result_select]
    except Exception as error:
        showerror(title='Ошибка', message=f'{error}')
    return vacancies

#Обработка запроса на выборку
def query_processing(query):
    query = query.lower()

    query_result = ''
    try:
        result = session.execute(query)
        fields = result.one()._fields
        number = 1
        for row in result.all():
            query_result += '----------------------------------------------\n'
            query_result += f'Number : {number}\n'
            for i in range(0, len(row)):
                query_result += f'{fields[i]} : {row[i]}\n'
            number += 1
    except Exception as error:
        query_result += f'Ошибка: {error}'

    return query_result

#Добавление данных в 'Vacancy'
def insert_vacancy(vacancy_title, vacancy_description, vacancy_status, vacancy_salary):
    if vacancy_title == '' or vacancy_description == '' or vacancy_status == '' or vacancy_salary == '':
        showerror(title='Ошибка', message='Заполните все поля')
    else:
        try:
            query_index = "CREATE INDEX IF NOT EXISTS ON vacancy (title)"
            session.execute(query_index)
            try:
                query_vacancy_title = f"SELECT * FROM vacancy WHERE title='{vacancy_title}'"
                result_select_title = session.execute(fquery_vacancy_title)
                titles = [row[1] for row in result_select_title.all()]
                if len(titles) == 0:
                    try:
                        query_id = "SELECT id FROM vacancy"
                        result_select_id = session.execute(query_id)
                        ids = [row[0] for row in result_select_id.all()]
                        while True:
                            vacancy_id = uuid.uuid4()
                            if vacancy_id not in ids:
                                break
                        try:
                            query_insert = f"INSERT INTO vacancy(id, description, salary, status, title) VALUES({vacancy_id}, '{vacancy_description}', {int(vacancy_salary)}, {bool(vacancy_status)}, '{vacancy_title}')"
                            session.execute(query_insert)
                            showinfo(title='Инфо', message='Данные успешно добавлены')
                        except Exception as error:
                            showerror(title='Ошибка', message=f'{error}')
                    except Exception as error:
                        showerror(title='Ошибка', message=f'{error}')
                else:
                    showerror(title='Ошибка', message='Такая вакансия уже есть')
            except Exception as error:
                showerror(title='Ошибка', message=f'{error}')    
        except Exception as error:
            showerror(title='Ошибка', message=f'{error}')

#Добавление данных в 'Employer'
def insert_employer(employer_vacancy_title, employer_title, employer_description, employer_address):
    if employer_vacancy_title == '' or employer_title == '' or employer_description == '' or employer_address == '':
        showerror(title='Ошибка', message='Заполните все данные')
    else:
        try:
            query_id = "SELECT id FROM employer"
            result_select_id = session.execute(query_id)
            ids = [row[0] for row in result_select_id.all()]
            while True:
                employer_id = uuid.uuid4()
                if employer_id not in ids:
                    break
            try:
                query_vacancy_id = f"SELECT id FROM vacancy WHERE title='{employer_vacancy_title}'"
                result_vacancy_id = session.execute(query_vacancy_id)
                vacancy_id = [row[0] for row in result_vacancy_id.all()]
                try:
                    query_insert = f"INSERT INTO employer(id, address, description, title, vacancy_id) VALUES({employer_id}, '{employer_address}', '{employer_description}', '{employer_title}', {vacancy_id[0]})"
                    session.execute(query_insert)
                    showinfo(title='Инфо', message='Данные успешно добавлены')
                except Exception as error:
                    showerror(title='Ошибка', message=f'{error}')
            except Exception as error:
                showerror(title='Ошибка', message=f'{error}')
        except Exception as error:
            showerror(title='Ошибка', message=f'{error}')

#Добавление данных в 'Candidate'
def insert_candidate(candidate_vacancy_title, candidate_name, candidate_gender, candidate_date_of_birth):
    if candidate_vacancy_title == '' or candidate_name == '' or candidate_gender == '' or candidate_date_of_birth == '':
        showerror(title='Ошибка', message='Заполните все данные')
    else:
        try:
            query_index = "CREATE INDEX IF NOT EXISTS ON Candidate (name)"
            session.execute(query_index)
            try:
                query_select_name = f"SELECT * FROM candidate WHERE name='{candidate_name}'"
                result = session.execute(query_select_name)
                names = [row[0] for row in result.all()]
                if len(names) == 0:
                    try:
                        query_id = "SELECT id FROM candidate"
                        result_select_id = session.execute(query_id)
                        ids = [row[0] for row in result_select_id.all()]
                        while True:
                            candidate_id = uuid.uuid4()
                            if candidate_id not in ids:
                                break
                        try:
                            query_vacancy_id = f"SELECT id FROM vacancy WHERE title='{candidate_vacancy_title}'"
                            result_vacancy_id = session.execute(query_vacancy_id)
                            vacancy_id = [row[0] for row in result_vacancy_id.all()]
                            try:
                                query_insert = f"INSERT INTO candidate(id, dateofbirth, gender, name, vacancy_id) VALUES({candidate_id}, '{candidate_date_of_birth}', '{candidate_gender}', '{candidate_name}', {vacancy_id[0]})"
                                session.execute(query_insert)
                                showinfo(title='Инфо', message='Данные успешно добавлены')
                            except Exception as error:
                                showerror(title='Ошибка', message=f'{error}')
                        except Exception as error:
                            showerror(title='Ошибка', message=f'{error}')
                    except Exception as error:
                        showerror(title='Ошибка', message=f'{error}')
                else:
                    showerror(title='Ошибка', message='Такой кандидат уже есть')
            except Exception as error:
                showerror(title='Ошибка', message=f'{error}')
        except Exception as error:
            showerror(title='Ошибка', message=f'{error}')
