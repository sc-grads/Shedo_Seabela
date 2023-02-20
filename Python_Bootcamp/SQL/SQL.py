import sqlite3

connection = sqlite3.connect('my_database.db')

c = connection.cursor()




sql = """
INSERT INTO employees (id, name, department, phone, email) VALUES (1, "John Smith", "IT", "+123456789", "johns@mycompany.com");
INSERT INTO employees VALUES (2, "Anne Barker", "Accounting", "+155345789", "anne@mycompany.com");
INSERT INTO employees VALUES (3, "Antony Winter", "Sales", "0042345678911", "danw@mycompany.com");
"""


c.executescript(sql)

connection.commit()


connection.close()