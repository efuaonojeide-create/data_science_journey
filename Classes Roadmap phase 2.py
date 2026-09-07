#this serves well for just one employee, if a 2nd was introduced the existing variables wold be overwritten, atleast for this.

class Employee:

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay

    def email(self):
        return f"{self.first}.{self.last}@gmail.com"


first = input("What's your first name: ")
last = input("What's your last name: ")
pay = int(input("How much is your pay: "))

emp_1 = Employee(first, last, pay)

print(emp_1.email())


#Monday's Warm Up

class Student:
    def __init__(self, name, score):
        self.name = name
        self.score = score

student_1 = Student('James', 89)
student_2 = Student('Grace', 90)

print (student_1.name, student_1.score)
print (student_2.name, student_2.score)


#Monday's Core
#The error with this is that python reads it as if 70 >= self.score AND self.score <= 100, which is ideally impossible to attain.
# In summary the direction is scarrterred so it can't produce anything.
'''
    def get_grade(self):
        if 70 >= self.score <= 100:
            return ("A")
        elif 60 >= self.score <= 69:
            return ("B")
        elif 50 >= self.score <= 59:
            return ("C")
        elif 40 >= self.score <= 49:
            return ("D")
        else:
            return "F"
'''

class Student:
    def __init__(self, name, score):
        self.name = name
        self.score = score

#The direction is correctly set, hence the logic can flow.
    def get_grade(self):
        if 70 <= self.score <= 100:
            return ("A")
        elif 60 <= self.score <= 69:
            return ("B")
        elif 50 <= self.score <= 59:
            return ("C")
        elif 40 <= self.score <= 49:
            return ("D")
        else:
            return "F"
        
student_1 = Student('James', 89)
student_2 = Student('Grace', 90)

print (student_1.name, student_1.score, student_1.get_grade())
print (student_2.name, student_2.score, student_2.get_grade())


#Monday's challenge
class Student:
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def get_grade(self):
        if 70 <= self.score <= 100:
            return ("A")
        elif 60 <= self.score <= 69:
            return ("B")
        elif 50 <= self.score <= 59:
            return ("C")
        elif 40 <= self.score <= 49:
            return ("D")
        else:
            return "F"
        
student_1 = Student('James', 89)
student_2 = Student('Grace', 90)
student_3 = Student('Love', 69)
student_4 = Student('Joy', 58)
student_5 = Student('David', 49)

students = [student_1, student_2, student_3, student_4, student_5]

for student in students:
    print (student.name, student.get_grade())