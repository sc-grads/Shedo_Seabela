import sqlite3

connection = sqlite3.connect('my_database.db')

cursor = connection.cursor()

sql = 'select * from employees'
cursor.execute(sql)

for row in cursor.fetchall():
    print(row)

connection.commit()

connection.close()