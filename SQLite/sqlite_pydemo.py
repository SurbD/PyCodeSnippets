import sqlite3

from employee import Employee

conn = sqlite3.connect(':memory:')

c = conn.cursor()

c.execute("""CREATE TABLE employees (
          first text,
          last text,
          pay integer
    )""")

def insert_emp(emp):
    with conn:
        c.execute("INSERT INTO employees VALUES (:first, :last, :pay)", {'first': emp.first, 'last': emp.last, 'pay': emp.pay})

def get_emps_by_name(lastname):
    c.execute("SELECT * FROM employees WHERE last=:last", {'last': lastname})
    return c.fetchall()

def update_pay(emp, pay):
    with conn:
        c.execute("""UPDATE employees SET pay = :pay
                  WHERE first = :first AND last = :last""", 
                  {'first': emp.first, 'last': emp.last, 'pay': pay})

def remove_emp(emp):
    with conn:
        c.execute("""DELETE from employees WHERE first = :first AND last = :last""",
                  {'first': emp.first, 'last': emp.last})


emp_1 = Employee('Devyn', 'Conn', 120_000)
emp_2 = Employee('Renee', 'Conn', 120_000)

insert_emp(emp_1)
insert_emp(emp_2)

emps = get_emps_by_name('Conn')
print(emps)

update_pay(emp_2, 100_000)
remove_emp(emp_1)

emps = get_emps_by_name('Conn')
print(emps)

conn.close()