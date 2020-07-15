class Person:
    def __init__(self,name, email):
        self.name = name
        self.email = email

    def __repr__(self):
        return repr((self.name,self.email))


class Student(Person):
    def __init__(self, name, email, college, cls):
        super().__init__(name,email)
        self.college = college
        self.cls = cls

    def __repr__(self):
        return repr((super().__repr__(), self.college,self.cls))

person = Person('Youssef','test@gmail.com')
print(person)

student = Student('Youssef','Test@gmail.com', 'Stanford', 'Algorithms' )
print(student)


# Person
# name, email
# Student
# college, class
# Employee
# title, employer