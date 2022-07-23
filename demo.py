import psycopg2
import dsn

connection = psycopg2.connect(dsn.DSN)

cursor = connection.cursor()

cursor.execute("DROP TABLE table2;")

sql1 = '''
   CREATE TABLE table2 (
       id INTEGER PRIMARY KEY,
       completed BOOLEAN NOT NULL DEFAULT False
   );
'''

cursor.execute(sql1)

sql2 = 'INSERT INTO table2 (id, completed) VALUES (1, True);'
cursor.execute(sql2)

sql3 = 'INSERT INTO table2 (id, completed) VALUES (%s, %s);'
cursor.execute(sql3, (2, False))

sql4 = 'INSERT INTO table2 (id, completed) VALUES (%(id)s, %(completed)s);'
cursor.execute(sql4, {
    "id": 3,
    "completed": True
})
cursor.execute("SELECT * FROM table2;")
results = cursor.fetchall()
for result in results:
    print(result)

connection.commit()

cursor.close()
connection.close()