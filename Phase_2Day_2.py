#Exampe used to learn and practice
class Employee:

    raise_amount = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay

    def email(self):
        return f"{self.first}.{self.last}@gmail.com"

    def increase(self):
        return self.pay * self.raise_amount


emp_1 = Employee("Jacob", "Mary", 45000)
emp_2 = Employee("Sonia", "Precious", 11000)

print(emp_2.increase())

#Tuesday's Warm up

class Student:
    school_name = "LSU Secondary School"

    def __init__(self, name, score):
        self.name = name
        self.score = score

student_1 = Student('James', 89)
student_2 = Student('Grace', 90)

print (student_1.name, student_1.score, student_1.school_name)
print (student_2.name, student_2.score, student_2.school_name)

#Tueday's Core

class PartTimeStudent(Student):
    def __init__(self, name, score, hours_worked):
        super().__init__(name,score)
        self.hours_worked = hours_worked

    def average_hours(self):
        return self.hours_worked/2

student_1 = PartTimeStudent('James', 89, 30)
student_2 = PartTimeStudent('Grace', 90, 90)

print (student_1.name, student_1.score, student_1.school_name, student_1.average_hours())
print (student_2.name, student_2.score, student_2.school_name, student_2.hours_worked)

#Tuesday's Challenge
class PartTimeStudent(Student):
    def __init__(self, name, score, hours_worked):
        super().__init__(name,score)
        self.hours_worked = hours_worked

    def average_hours(self):
        return self.hours_worked/2
#the problem with this get_grade method was that it kept calling adding 10 whenever the student's grade was asked for which it's not meant to do
    
    def get_grade(self):
        if self.hours_worked > 20:
            self.score = self.score + 10
        if 70 <= self.score <= 100:
            return "A"
        elif 60 <= self.score <= 69:
            return "B"
        elif 50 <= self.score <= 59:
            return "C"
        elif 40 <= self.score <= 49:
            return "D"
        else:
            return "F"
    
    def get_grade(self):
        effective_score = self.score
        if effective_score > 20:
            effective_score = self.score + 10
        if 70 <= effective_score <= 100:
            return "A"
        elif 60 <= effective_score <= 69:
            return "B"
        elif 50 <= effective_score <= 59:
            return "C"
        elif 40 <= effective_score <= 49:
            return "D"
        else:
            return "F"

student_1 = PartTimeStudent('James', 40, 25)
student_2 = PartTimeStudent('Grace', 30, 26)

print (student_2.get_grade())
print (student_2.get_grade())
print (student_2.get_grade())