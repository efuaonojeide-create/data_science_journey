#Monday's Excercises
#1 Warm_up
'''
fav_food = ["Beans", "Plantain", "Garri", "Rice", "Juice"]
for _ in fav_food:
    print(_) 
'''
#2 Core
'''
numbers = [5,2,3,4,100,6,7,8,9,10]

smallest = numbers[0]
largest = numbers[0]

for _ in numbers:
    if _ < smallest:
        smallest = _
    if _> largest:
        largest =_

print ("The smallest number is:", smallest)
print ("The largest number is:", largest)
'''
#3 Challenge
'''
import statistics
exam_scores = [30, 70, 80, 88, 100]
mean = statistics.mean(exam_scores)

count = 0

for i in exam_scores:
    if i > mean:
       count = count+1
       
print (f"There are {count} scores greater than average")
'''

#Tuesday's Excercises
#1 Warm up
'''
School = {"Name:":"Wisdom", "Age:":"20", "Dept:":"Computer Engr"}
for key, value in School.items():
    print (key, value)
'''
#2Core
'''
Contact_book = {"John": {"phone" : "555-444-090", "Email" : "John@gmail.com"}, }

User = input("Enter a name: ")

if User in Contact_book:
    print (Contact_book[User]["phone"])
'''
#3Challenge
'''
sentence = input("Enter a setence: ")

words = sentence.split()

word_count = {}

for word in words:
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1

print (word_count)
'''
#Wednesday Excericises
#1warm Up
'''
sentence = input("enter a sentence: ")
words = sentence.split()
words.reverse()
print (sentence.upper())
print (sentence.lower())
print (" ".join(words))
'''
#2Core
'''
fruits = ["apple", "banana", "apple", "orange", "banana", "grape"]

unique_list = list(set(fruits))

print(unique_list)
'''
#3Challenge

#This doesn't clear punctuations
'''
paragraph = input("Type a paragraph: ")

words = paragraph.split()

unique_words = set(words)

count = len(unique_words)

print ("The number of words =", count)
'''
#This does clear punctuations
'''
import string

paragraph = input("Type a paragraph: ")

# Remove punctuation
clean_paragraph = ""
for char in paragraph:
    if char not in string.punctuation:
        clean_paragraph += char

# Convert everything to lowercase
clean_paragraph = clean_paragraph.lower()

# Split into words
words = clean_paragraph.split()

# Remove duplicates
unique_words = set(words)

# Count unique words
count = len(unique_words)

print("The number of unique words =", count)
print("Unique words:", unique_words)
'''

#Thursday's Excercises
#Warm up
'''
file = open("line.txt", "w")

for i in range(5):
    text = input("Type something:")
    file.write(f"{text}\n")

file.close()

file = open("line.txt", "r")
for line in file:   
    print (line, end="")

file.close()
'''
#core
'''
import csv

item = input("What's the Item: ")
amount = input("How much does it cost: ")

file = open("expense.csv", "a", newline="")
writer = csv.writer(file)
writer.writerow([item, amount])
'''

