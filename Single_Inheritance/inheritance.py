class Person:
    def __init__(self, name,age,job):
        self._name = name
        self._age = age
        self._job = job

    @property
    def name(self):
        return self._name
    
    @property
    def age(self):
        return self._age
    
    @property
    def job(self):
        return self._job

    def get_details(self):
        return f"Name: {self.name}, Age: {self.age}, Job: {self.job}"
    

class Student(Person):

    def __init__(self, name, age, job, grade):
        super().__init__(name, age, job)
        self._grade = grade

    @property
    def grade(self):
        return self._grade
    
    def get_details(self):
        result = super().get_details()
        return f'{result}, Grade: {self.grade}'
    
class Professor(Person):

    def __init__(self, name, age, job, courses):
        super().__init__(name, age, job)
        self._courses = courses

    @property
    def courses(self):
        return self._courses
    
    def get_details(self):
        return f'{super().get_details()}, Courses: {self.courses}' 


class Employee(Person):

    def __init__(self, name, age, job, department):
        super().__init__(name, age, job)
        self._department = department

    @property
    def department(self):
        return self._department
    
    def get_details(self):
        return f'{super().get_details()}, Department: {self.department}' 

class StudentProfessor(Student, Professor):

    def __init__(self, name, age, job, courses, grade):
        Person.__init__(self,name, age, job)
        self._courses = courses
        self._grade = grade

    @property
    def grade(self):
        return self._grade

    @property
    def courses(self):
        return self._courses

    def get_details(self):
        return f'{Person.get_details(self)}, Courses: {self.courses}, Grade: {self.grade}'

class Location:
    
    __slots__ = ['_name', '_longitude', '_latitude']
    
    def __init__(self, name,longitude, latitude ):
        self._name = name
        self._longitude = longitude
        self._latitude = latitude

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        self._name = name
    
    @property
    def longitude(self):
        return self._longitude
    
    @property
    def latitude(self):
        return self._latitude
    
    def get_coordinates(self):
        return (self.longitude,self.latitude)

