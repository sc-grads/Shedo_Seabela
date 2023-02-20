import sqlite3

connection = sqlite3.connect('my_database.db')

cursor = connection.cursor()


department = input('Department:')

sql = 'DELETE FROM employees where department = ?;'
cursor.execute(sql, (department,))


connection.commit()

connection.close()