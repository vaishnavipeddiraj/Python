#find in strings
course = "Python"
print(course.find("o"))
print(course.find("O")) #casesensitive returns -1
print(course.replace("Python", "Java" ))
print(course[1:-1])
print("Java" in course) #true or false
print(len(course)) #length of string
print(course.upper()) #uppercase
print(course.lower()) #lowercase
print(course.title()) #titlecase