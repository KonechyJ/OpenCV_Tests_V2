import datetime

class Employee:

    num_of_employees = 0
    raise_amount = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + "@company.com"

        Employee.num_of_employees += 1
    def fullname(self):
        return "{} {} ".format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

    @classmethod
    def set_raise_amount(cls, amount):
        cls.raise_amount = amount

    @classmethod
    def from_string(cls, employee_str):
        first, last, pay = employee_str.split('-')
        return cls(first, last, pay)

    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True



class Developer(Employee):
    raise_amount = 1.10

    def __init__(self, first, last, pay, programming_Language):
        super().__init__(first, last, pay)
        self.programming_Language = programming_Language

class Manager(Employee):
    def __init__(self, first, last, pay, employees=None):
        super().__init__(first, last, pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees
    def add_employee(self, employee):
        if employee not in self.employees:
            self.employees.append(Employee)
    def remove_employee(self, employee):
        if employee  in self.employees:
            self.employees.remove(Employee)
    def print_employee(self):
        for emp in self.employees:
            print('-->',emp.fullname())


emp_1 = Employee("Josh", "Konechy", 50000)
emp_2 = Employee("John", "Smith", 60000)

print(emp_1)
print(emp_2)
print(emp_1.fullname())
print(Employee.num_of_employees)

Employee.set_raise_amount(1.05)

print(Employee.raise_amount)
print(emp_1.raise_amount)
print(emp_2.raise_amount)

emp_str_1 = "Jane-Doe-70000"

new_emp_1 = Employee.from_string(emp_str_1)

print(new_emp_1.email)
print(new_emp_1.fullname())

my_date = datetime.date(2016, 7, 11)
print(Employee.is_workday(my_date))


dev_1 = Developer("Jurgen", "smoke", 65000, "Python")
dev_2 = Developer("Jorgen", "Scorpio", 70000, "C++")

manager_1 = Manager("Sue", "Smith", 90000, [dev_1])
print(dev_1.pay)
dev_1.apply_raise()
print(dev_1.pay)

print(dev_1.programming_Language)
print(dev_2.programming_Language)

print(manager_1.email)
manager_1.print_employee()

