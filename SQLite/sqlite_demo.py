import os
import sqlite3

from employee import Employee

# Setting DB path
basedir = os.path.abspath(os.path.dirname(__file__))
os.chdir(basedir)

# conn = sqlite3.connect('employee.db') # (':memory:') - for in memory database
conn = sqlite3.connect(':memory:') 

c = conn.cursor()

# SQLite database datatypes => null, integer, real, text, blob

c.execute("""CREATE TABLE employees (
          first text,
          last text,
          pay integer
    )""")

emp_1 = Employee('John', 'Doe', 80_000)
emp_2 = Employee('Jane', 'Doe', 90_000)

c.execute("INSERT INTO employees VALUES (?, ?, ?)", (emp_1.first, emp_1.last, emp_1.pay))
conn.commit()

c.execute("INSERT INTO employees VALUES (:first, :last, :pay)", {'first': emp_2.first, 'last': emp_2.last, 'pay': emp_2.pay})
conn.commit()

c.execute("INSERT INTO employees VALUES ('Kendra', 'Hansbros', 9000)")
conn.commit()

c.execute("SELECT * FROM employees")
print(c.fetchall())

c.execute("SELECT * FROM employees WHERE last=?", ("Hansbros",))
print(c.fetchall())

c.execute("SELECT * FROM employees WHERE last=:last", {'last': 'Doe'})
print(c.fetchall())

conn.commit()

conn.close()