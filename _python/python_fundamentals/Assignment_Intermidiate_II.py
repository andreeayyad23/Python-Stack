#1

x = [ [5,2,3], [10,8,9] ]
students = [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'}
]
sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}
z = [ {'x': 10, 'y': 20} ]

x[1][0]=15
print(x)
students[0]['first_name']= 'Bryant'
print(students)
sports_directory['soccer'][0] = 'Andres'
print(sports_directory)


#2

def iterateDictionary(studentList):
    for studentDict in studentList:
        fullName =''
        for studentKey in studentDict:
            fullName += f"{studentKey} - {studentDict[studentKey]}, " 
        print(fullName[:-2])

students = [
         {'first_name':  'Michael', 'last_name' : 'Jordan'},
         {'first_name' : 'John', 'last_name' : 'Rosales'},
         {'first_name' : 'Mark', 'last_name' : 'Guillen'},
         {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]


iterateDictionary(students) 

#3

def iterateDictionary_2(keyName, studentList):
    
    if keyName == "first_name" or keyName == "last_name":
        for student in studentList:
            print(f"{student[keyName]}")
    else:
        print("Please provide a correct keyname ('first_name' or 'last_name') and student list")

iterateDictionary_2('first_name', students)
iterateDictionary_2('last_name', students)


#4

dojo = {
    'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
    'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}

def printInfo(dictionary):
    for key,value in dictionary.items():
        print(f"{len(dictionary[key]) } {key.upper()}")
        for element in dictionary[key]:
            print(element)
        print(" ")
printInfo(dojo)