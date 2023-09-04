import logging

logging.basicConfig(filename='Logging/employee.log', level=logging.INFO, format='%(levelname)s:%(message)s')

class Employee:

    def __init__(self, first, last) -> None:
        self.first = first
        self.last = last

        logging.info(f"Created Employee: {self.fullname} - {self.email}")

    @property
    def fullname(self):
        return f'{self.first} {self.last}'
    
    @property
    def email(self):
        return f'{self.first}.{self.last}@email.com'
    

emp1 = Employee('Jred', 'Pint')
emp2 = Employee('Tristan', 'Platten')
emp3 = Employee('Ria', 'Nali')