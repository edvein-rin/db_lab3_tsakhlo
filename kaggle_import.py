import csv
import decimal
import psycopg2

from constants import username, password, database, host, port

INPUT = 'ramen.csv'

query_0 = '''
CREATE TABLE IF NOT EXISTS public.ramen_copy
(
    id integer NOT NULL DEFAULT nextval('"Ramen_id_seq"'::regclass),
    name character(50) COLLATE pg_catalog."default" NOT NULL,
    style character(50) COLLATE pg_catalog."default" NOT NULL,
    CONSTRAINT "Ramen_pkey" PRIMARY KEY (id)
)
'''

query_1 = '''
DELETE FROM ramen_copy
'''

query_2 = '''
INSERT INTO ramen_copy (id, name, style) VALUES (%s, %s, %s)
'''

connection = psycopg2.connect(user=username, password=password, dbname=database)

with connection:

    cur = connection.cursor()
    cur.execute('drop table if exists ramen_copy')
    cur.execute(query_0)
    cur.execute(query_1)

    with open(INPUT, 'r') as inf:
        reader = csv.DictReader(inf)

        for idx, row in enumerate(reader):
            values = (row['Ramen_Id'], row['Ramen_Name'], row['Ramen_Style'])
            cur.execute(query_2, values)

    connection.commit()