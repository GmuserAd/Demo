class Employee:
        def __init__(self, firstname, lastname):
            self.firstname = firstname
            self.lastname = lastname
            self.fullname = self.firstname +' '+ self.lastname
            self.email = self.firstname+'.'+self.lastname+'@company.com'
    
        


emp_1 = Employee("John", "Smith")
emp_2 = Employee("Mary",  "Sue")
emp_3 = Employee("Antony", "Walker")
