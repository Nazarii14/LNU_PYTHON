    # тип імплоі, від нього похідний викладач
    # тип предмет, від нього похідний викладач
    # тип викладач має кафедру і предмет

class Employee:
    def __init__(self, first, last):
        self.first = first
        self.last = last

    def __str__(self):
        return self.first + " " + self.last

    @property
    def email(self):
        return f'{self.first}.{self.last}@email.com'

    @property
    def fullname(self):
        return f'{self.first} {self.last}'

    @fullname.setter
    def fullname(self, name):
        self.first, self.last = name.split(' ')


class Subject:
    def __init__(self, name, department):
        self.name = name
        self.department = department

    def __str__(self):
        return self.name + " " + self.department

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def department(self):
        return self._department

    @department.setter
    def department(self, value):
        self._department = value

class Lecturer(Employee, Subject):

    def __init__(self, first, last, name, department, rank):
        Employee.__init__(self, first, last)
        Subject.__init__(self, name, department)
        self.rank = rank

    def __str__(self):
        return Employee.__str__(self) + " " + Subject.__str__(self) + " " + self.rank

    @property
    def department(self):
        return self._department

    @department.setter
    def department(self, value):
        self._department = value

    @property
    def subject(self):
        return self._subject

    @subject.setter
    def subject(self, value):
        self._subject = value

    @property
    def rank(self):
        return self._rank

    @rank.setter
    def rank(self, value):
        self._rank = value


Klakovych = Lecturer("Lesya", "Klakovych", "Programming C++", "AMI", "c")
Yaroshko = Lecturer("Sergiy", "Yaroshko", "Programming Python", "AMI", "a")

print(Klakovych)
print(Yaroshko)
