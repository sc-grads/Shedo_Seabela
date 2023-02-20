import sqlite3

connection = sqlite3.connect('my_database.db')

cursor = connection.cursor()
id = input('Enter ID:')
sql = 'select * from employees where id = ?;'
cursor.execute(sql, (id,))

for row in cursor.fetchall():
    print(row)


record = (10, 'Leonardo Romano', 'Marketing', '+40122111', 'leo@x.com')

sql = 'insert into employees values (?,?,?,?,?);'
cursor.execute(sql, record)
connection.commit()

connection.close()