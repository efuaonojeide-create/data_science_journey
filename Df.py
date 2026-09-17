import pandas as pd
students = pd.read_csv("students.csv")
departments = pd.read_csv("departments (1).csv")
'''
print(students.head()) #Printing out the first five rows

print (students.shape) #getting the dimensions of the dataframe

combine = students.query("department == 'Computer Engineering'") #I queried

merged = pd.merge(combine, departments) #having quieried I merged

print (merged) #I printed the merge
'''
#p2w2_Monday's Warm up
'''
merge = pd.merge(students, departments, left_on = 'department', right_on = 'department_name')

print (merge)
'''
#p2w2 Monday's Core
#print (students.name.isnull().sum())

#p2w2 Monday's Challenge
print (students.dropna(inplace = True))
