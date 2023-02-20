import sqlite3

connection = sqlite3.connect('my_database.db')

cursor = connection.cursor()
id = input('Id:')

sql = 'UPDATE employees SET department="Sales" where id=?;'
cursor.execute(sql, (id,))
connection.commit()
connection.close()