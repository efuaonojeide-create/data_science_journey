import pandas as pd
students = pd.read_csv("students.csv")
df = students.copy()
#print (students)

#Tuesday's Warm up
'''
students['department'] = students.department.str.lower()
print (students)
'''

#Tuesday's Core
'''
fish = pd.DataFrame(
    {'type' : ['Cat','Dog','Jelly', 'Electric', 'Ell'],
     'size': ['12cm','15cm','10cm','13cm','7cm'],
     'reviews': ['Good','Okay','Great','sweet','Delicious'],})

f = pd.concat([fish]*3, ignore_index = True)

print (f.duplicated())
print (f.drop_duplicates())
'''

#Tuesday's Challenge
Track = pd.read_csv("Tracker.csv")
#Amount is in correct numeric format

print (Track['Category'].unique())
Track['Category'] = Track.Category.str.upper()
#print (Track.drop_duplicates)