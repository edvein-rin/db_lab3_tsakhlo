import json
import psycopg2

from constants import username, password, database, host, port

OUTPUT = 'DB.json'

TABLES = [
    'ramen',
    'author',
    'review',
    'review_author',
    'review_ramen',
]

conn = psycopg2.connect(user=username, password=password, dbname=database, host=host, port=port)

data = {}
with conn:
    cur = conn.cursor()
    for table in TABLES:
        cur.execute('SELECT * FROM ' + table)
        rows = []
        fields = [x[0] for x in cur.description]
        for row in cur:
            rows.append(dict(zip(fields, row)))

        data[table] = rows


with open(OUTPUT, 'w') as f:
    json.dump(data, f, default=str)