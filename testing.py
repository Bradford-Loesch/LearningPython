# print "Hello World"
#
# for i in range (1, 1000, 2):
#     print i
#
# for i in range (5, 1000000, 5):
#     print i

# a = [1, 2, 5, 10, 255, 3]
# sum = 0;
# for i in range (0, len(a), 1):
#     sum += a[i]
#     print sum
# avg = sum / len(a)
# print avg

# for i in range(1,2001,1):
#     print "Number is", i
#     if (i % 2 == 0):
#         print " This is an even number."
#     else:
#         print " This is an odd number."

# def multiply5(arr):
#     for i in range(0,len(arr),1):
#         arr[i] = arr[i] * 5
#     print arr
#     return arr
#
# multiply5([2,4,10,16])

# def grades():
#     print "Scores and Grades"
#     for i in range(0,10,1):
#         grade = input("Enter a grade between 60 and 100.")
#         while (grade > 100 or grade < 60):
#             grade = input("Your value was not between 60 and 100. Enter a grade between 60 and 100.")
#         if (grade >= 60 and grade < 70):
#             letGrade = "D"
#         elif (grade >= 70 and grade < 80):
#             letGrade = "C"
#         elif (grade >= 80 and grade < 90):
#             letGrade = "B"
#         elif (grade >= 70 and grade <= 100):
#             letGrade = "A"
#         print "Score:", grade, "; Your Grade is", letGrade
#     print "End of the program. Bye!"
#
# grades()

# def coinflip(flips):
#     import random
#     heads = 0
#     tails = 0
#     for i in range(0, flips, 1):
#         rand = round(random.random())
#         if (rand == 1):
#             side = "head"
#             heads+=1
#         elif(rand == 0):
#             side = "tail"
#             tails+=1
#         print "Attempt #",i,": Throwing a coin... it's a",side,"!... Got",heads,"head(s) so far and",tails,"tail(s) so far."
#
# coinflip(10)

# def drawstars(arr):
#     for i in range (0,len(arr),1):
#         stars = ""
#         if (isinstance(arr[i], basestring)):
#             for j in range (0,len(arr[i]),1):
#                 stars += arr[i][0].lower()
#         else:
#             for j in range (0,arr[i],1):
#                 stars += "*"
#         print stars
#
# testArray = [4, "Tom", 1, "Michael", 5, 7, "Jimmy Smith"]
# drawstars(testArray)

# def students(arr):
#     for i in range(0,len(arr),1):
#         print arr[i].get('first_name'), arr[i].get('last_name')
#
# testArray = [
#      {'first_name':  'Michael', 'last_name' : 'Jordan'},
#      {'first_name' : 'John', 'last_name' : 'Rosales'},
#      {'first_name' : 'Mark', 'last_name' : 'Guillen'},
#      {'first_name' : 'KB', 'last_name' : 'Tonel'}
# ]
# students(testArray)

def users(dic):
    students = dic.get('Students')
    instructors = dic.get('Instructors')
    for i in range(0,len(students),1):
        length = len(students[i].get('first_name')) + len(students[i].get('last_name'))
        print i+1, "-", students[i].get('first_name'), students[i].get('last_name'), "-", length
    for i in range(0,len(instructors),1):
        length = len(instructors[i].get('first_name')) + len(instructors[i].get('last_name'))
        print i+1, "-", instructors[i].get('first_name'), instructors[i].get('last_name'), "-", length

testDict = {
    'Students': [
         {'first_name':  'Michael', 'last_name' : 'Jordan'},
         {'first_name' : 'John', 'last_name' : 'Rosales'},
         {'first_name' : 'Mark', 'last_name' : 'Guillen'},
         {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ],
    'Instructors': [
         {'first_name' : 'Michael', 'last_name' : 'Choi'},
         {'first_name' : 'Martin', 'last_name' : 'Puryear'}
    ]
}

users(testDict)
