from cassandra.cluster import Cluster
from fill_functions import *

cluster = Cluster()
session = cluster.connect('jobs')

session.execute("DROP TABLE vacancy")
session.execute("DROP TABLE candidate")
session.execute("DROP TABLE employer")

create_vacancy = "CREATE TABLE IF NOT EXISTS Vacancy(ID UUID PRIMARY KEY,Title varchar,Description text,Status boolean,Salary int)"
session.execute(create_vacancy)

vacancy_index_1 = "CREATE INDEX IF NOT EXISTS ON vacancy(description)"
session.execute(vacancy_index_1)
vacancy_index_2 = "CREATE INDEX IF NOT EXISTS ON vacancy(status)"
session.execute(vacancy_index_2)
vacancy_index_3 = "CREATE INDEX IF NOT EXISTS ON vacancy(salary)"
session.execute(vacancy_index_3)
vacancy_index_4 = "CREATE INDEX IF NOT EXISTS ON vacancy(title)"
session.execute(vacancy_index_4)

create_candidate = "CREATE TABLE IF NOT EXISTS Candidate(ID UUID PRIMARY KEY,Vacancy_id UUID,Name varchar,Gender varchar,DateOfBirth date)"
session.execute(create_candidate)

candidate_index_1 = "CREATE INDEX IF NOT EXISTS ON candidate(Vacancy_id)"
session.execute(candidate_index_1)
candidate_index_2 = "CREATE INDEX IF NOT EXISTS ON candidate(Name)"
session.execute(candidate_index_2)
candidate_index_3 = "CREATE INDEX IF NOT EXISTS ON candidate(Gender)"
session.execute(candidate_index_3)
candidate_index_4 = "CREATE INDEX IF NOT EXISTS ON candidate(DateOfBirth)"
session.execute(candidate_index_4)


create_employer = "CREATE TABLE IF NOT EXISTS Employer(ID UUID PRIMARY KEY,Vacancy_id UUID,Title varchar,Description text,Address varchar)"
session.execute(create_employer)

employer_index_1 = "CREATE INDEX IF NOT EXISTS ON employer(Vacancy_id)"
session.execute(employer_index_1)
employer_index_2 = "CREATE INDEX IF NOT EXISTS ON employer(Title)"
session.execute(employer_index_2)
employer_index_3 = "CREATE INDEX IF NOT EXISTS ON employer(Description)"
session.execute(employer_index_3)
employer_index_4 = "CREATE INDEX IF NOT EXISTS ON employer(Address)"
session.execute(employer_index_4)

def gen_vacancy():
    ids = []
    for i in range(0, 5):
        while True:
            vacancy_id = uuid.uuid4()
            if vacancy_id not in ids:
                ids.append(vacancy_id)
                break
        vacancy_description = genText(random.randint(15, 20))
        vacancy_salary = random.randint(1000, 2000)
        vacancy_status = genStatus()
        vacancy_title = genWord()

        query_insert = f"INSERT INTO vacancy(id, description, salary, status, title) VALUES({vacancy_id}, '{vacancy_description}', {int(vacancy_salary)}, {bool(vacancy_status)}, '{vacancy_title}')"
        session.execute(query_insert)

def gen_employer():
    query = "SELECT id FROM vacancy"
    result = session.execute(query)
    vacancy_ids = [row[0] for row in result.all()]
    ids = []
    for i in range(0, 5):
        while True:
            employer_id = uuid.uuid4()
            if employer_id not in ids:
                ids.append(employer_id)
                break
        employer_address = f"{genWord()} street {random.randint(1, 30)}"
        employer_description = genText(random.randint(15, 20))
        employer_title = genWord()
        emploer_vacancy_id = vacancy_ids[random.randint(0, len(vacancy_ids) - 1)]
        vacancy_ids.remove(emploer_vacancy_id)

        query_insert = f"INSERT INTO employer(id, address, description, title, vacancy_id) VALUES({employer_id}, '{employer_address}', '{employer_description}', '{employer_title}', {emploer_vacancy_id})"
        session.execute(query_insert)

def gen_candidate():
    query = "SELECT id FROM vacancy"
    result = session.execute(query)
    vacancy_ids = [row[0] for row in result.all()]
    ids = []
    for i in range(0, 13):
        while True:
            candidate_id = uuid.uuid4()
            if candidate_id not in ids:
                ids.append(candidate_id)
                break
        candidate_date = generateDate().strftime("%Y-%m-%d")
        gender = random.randint(1, 2)
        candidate_gender = genGender(gender)
        candidate_name = genNames(gender)
        candidate_vacancy_id = vacancy_ids[random.randint(0, len(vacancy_ids) - 1)]

        query_insert = f"INSERT INTO candidate(id, dateofbirth, gender, name, vacancy_id) VALUES({candidate_id}, '{candidate_date}', '{candidate_gender}', '{candidate_name}', {candidate_vacancy_id})"
        session.execute(query_insert)

gen_vacancy()
gen_employer()
gen_candidate()
