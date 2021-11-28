import psycopg2
import math
import matplotlib.pyplot as plt

from constants import username, password, database, host, port


query_1 = '''
select trim(author.name), count(review.id) 
from author inner join review on author.id = review.id
group by author.name
'''

query_2 = '''
select trim(review.name), count(ramen.id) from review inner join ramen
on review.id = ramen.id or review.id = ramen.id
group by review.name
'''

query_3 = '''
select trim(author.name), count(ramen.id) 
from author inner join ramen on author.id = ramen.id
group by author.name
'''

connection = psycopg2.connect(user=username, password=password, dbname=database, host=host, port=port)

with connection:
    cursor = connection.cursor()


    cursor.execute('drop view if exists AuthorTotalReviews')
    cursor.execute(query_1)
    cursor.execute('select * from AuthorTotalReviews')

    bar = {}
    for row in cursor:
        bar[row[0]] = row[1]
        print(row)

    plt.bar(list(map(lambda x: str(x), list(bar.keys()))), bar.values())
    plt.xticks(rotation=45)
    plt.title('Количество ревью автора')
    plt.xlabel('Автор')
    plt.ylabel('Количество ревью')
    plt.show()


    cursor.execute('drop view if exists RamenReviewCount')
    cursor.execute(query_2)
    cursor.execute('select * from RamenReviewCount')

    pie = {}
    for row in cursor:
        pie[row[0]] = row[1]
        print(row)

    fig, ax = plt.subplots()
    colors = ['#4F6272', '#B7C3F3', '#DD7596', '#8EB897','#B7C3F3']
    ax.pie(pie.values(), labels = pie.keys(), autopct='%1.1f%%', colors=colors)
    plt.title('Количество ревью у раменов')
    plt.show()


    cursor.execute('drop view if exists RamensWithACupStyle')
    cursor.execute(query_3)
    cursor.execute('select * from RamensWithACupStyle')

    ramens_with_a_cup = []
    ramens_quantity = []
    for row in cursor:
        ramens_with_a_cup.append(row[0])
        ramens_quantity.append(row[1])
        print(row)

    fig, ax = plt.subplots()
    ax.plot(ramens_with_a_cup, ramens_quantity, marker='o')
    plt.title('Отношение раментов в чашке ко всем')
    plt.xlabel('Рамены в чашке')
    plt.ylabel('Все рамены')
    plt.show()
