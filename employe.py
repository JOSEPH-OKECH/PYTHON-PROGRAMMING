class Employee:
    num_of_emps = 0
    raise_amount = 1.04
    
    def __init__ (self, fname, lname, age, gender, pay):
        self.fname = fname
        self.lname = lname
        self.age = age
        self.gender = gender
        self.pay = pay
        self.email= fname + '.' + lname + '@mcc.com'
        
        Employee.num_of_emps += 1
        
    def apply_raise(self):
        self.pay = int(self.pay*self.raise_amount)
        
emp_1 = Employee('John','Baptist', 25, 'male', 5000)
emp_2 = Employee('Gilbert', 'Francis', 35, 'male', 15000)
emp_3 = Employee('Recheal', 'Rael', 24, 'Female', 8000)

print(Employee.num_of_emps)