from cassandra.cluster import Cluster
cluster = Cluster()
session = cluster.connect('jobs')

#Очищение окна
def clear_packs(packs):
    if len(packs) != 0:
        for i in range(0, len(packs)):
            packs[i].pack_forget()
        packs.clear()

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