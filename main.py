class Person( object ):

    def __init__(self, name, idnumber):
        self.name = name
        self.idnumber = idnumber
    def display(self):
            print(self.name)
            print(self.idnumber)

class Employee( Person ):
        def __init__(self, name, idnumber, salary, post):
                self.salary = salary
                self.post = post

                Person.__init__(self, name, idnumber)

a = Employee('Shivangi', 20210401, 15000, "Intern")
b = Employee('Rahul', 20210402, 25000, "Manager")
c = Employee('Ravi', 20210403, 35000, "CEO")

a.display()
b.display()
c.display()
