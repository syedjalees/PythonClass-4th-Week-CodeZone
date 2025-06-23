# transpiler -->  code ko aik language se doosri language mein convert karta hai
# compiler  --> poora ka poora code aik sath chalata hai  
# interpreter -->  line by line code chalata hai

# print("Hello Ahil!")
# print("Hello Ahil!")


# Variable == Container


# name = "Fatima"

# age = 14

# isStudent = True

# print(name)
# print(age)

# comment ==>  ctrl + ?  --> 

# concatination
# print('my name is ' + name + ' and my age is ' + str(age))

# print('my name is', name , 'and my age is', age)

# print(f'my name is {name} and age is {age} and I am a student {isStudent}')  # f-string


# sent = 12

# data = str(sent)
# check = type(data)

# print(check)  







# format --> f-string  / String literal

# print(f"my name is {name}")

# Data types
# 1. str ==  String  --> ABC,  "Word" / 'Word'  --> str   --> "Hello World!" , 'Hello World!'
# 2. int ==  Integer --> 123  123  --> int
# 4. bool  == Boolean --> True/False   ---> bool
# 3. Float --> 123.45  
# 5. List --> [1, 2, 3, 4, 5]
# 6. Tuple --> (1, 2, 3, 4, 5)
# 7. Dictionary --> {"name": "Nimarta", "age": 25}
# 8. Set   --> {1, 2, 3, 4, 5}  
# 9. None   --> NoneType 


# name = "Nimarta"
# age = 25
# is_student = False 

# print(f"my name is {name} and my age is {age} and I am a student {is_student}")

# # how to check data type 
# print(type(name))
# print(type(age))
# print(type(is_student))
# print("my name is : " + name + " and I am a student"+ is_student)  # concatenation  -->



# print(type(name))
# print(type(age))
# change = str(age)  # convert int to str
# print(type(change))







# num = 5   
# print(type(num))

# num2 = str(num)
# print(type(num2))

# num3 = int(num2)
# print(type(num3))


# sep / end

# print("Fatima", "Jalees", "Nimarta", sep="&&")

# print("14","5","2025", sep="/")

# print("I am a Web","Developer",sep="-")

# print("Sayyed" , end=" ")
# print("Jalees")

# print("Fatima", end=" ")
# print("Usman")

# round function --> round-off value of float 

# num: float = 5.5  
# print(round(num))





# name = input("Enter your name: ")  # Placeholder
# print(f"Your name is {name}")

# len function , length 

# \n new line 
# \t tab == ziada space 
# my_name = input("Enter your name: ")  # Placeholder

# result = len(my_name) 
# print(f"\nYour name is {my_name}")  
# print(f"\nLength of your name is \t{result} characters.")





# Operators

# 1. Arithmetic Operators
# + , - , x , / , % , // , ** 

# Used for mathematical operations like addition, subtraction, multiplication, and division.

# 1. Addition (+): Adds two numbers.
# 2. Subtraction (-): Subtracts the second number from the first.
# 3. Multiplication (*): Multiplies two numbers.
# 4. Division (/): Divides the first number by the second.
# 5. Modulus (%): Returns the remainder of the division.
# 6. Floor Division (//): Divides and returns the largest integer less than or equal to the result. 
# 7. Exponentiation (**): Raises the first number to the power of the second.



# Addition  
# a = 10  
# b = 5
# print(a + b)


# # Subtraction
# a = 10   
# b = 5 
# sub = a-b
# print(sub)

# # Multiplication
# a = 10         
# b = 5
# mul = a * b     
# print(mul)

# # Division
# a = 10         
# b = 5
# div = a / b     
# print(div)





# # Modulus % --> Reminder

# print(10 % 3)  # 1
# print(10 % 2)  # 0


# # Exponentiation ** --> Power 
# print(2 ** 3)


# Floor Division // --> Quotient
# x = 10
# y = 3

# print(x // y)  



# ASSIGNMENT:
# MAKE A CALCULATOR

# A = 14
# B = 50

# print(f"A + B = {A + B}")
# print(f"A - B = {A - B}")
# print(f"A * B = {A * B}")
# print(f"A / B = {A / B}")

# Input Method

# name = input("Enter your name: ")  #Placeholder
# age = input("Enter your age: ")
# print(f"Hello, my name is { name } and I am {age} years old.")


# first_number = input("Enter first number: ") 
# second_number = input("Enter second number: ")

# print(type(first_number))

# result = int(first_number) 

# print(f"Sum of {first_number} and {second_number} is {result}")
# print(type(first_number))


# string Methods 
# .lower()  --> Lowercase
# .upper()  --> Uppercase
# .title()  --> Titlecase
# .capitalize()  --> Capitalize first letter


# Sentence = "I am a Web Developer" 
# print("this is simple >>>>  ",Sentence)
# print("this is lowercase >>>>>  ",Sentence.lower())
# print("this is Uppercase >>>>>  ",Sentence.upper())
# print("this is Capitalize >>>>>  ",Sentence.capitalize())
# print("this is titleCase >>>>>  ",Sentence.title())









# Assignment Operators 

# Used to assign values to variables. 



    #  Name                   Symbol 
# 1. Assign                    =  
# 2. Add and Assign            +=
# 3. Subtract and Assign       -=
# 4. Multiply and Assign       *=
# 5. Divide and Assign         /=


# first = 10
# first = 15  # Reassigning value to first variable dynamically
# first += 5    # Add and assign  # first = first+5
# first -= 3    # Subtract and assign  # first = first-3
# first *= 2    # Multiply and assign  # first = first*2
# # first /= 4    # Divide and assign  # first = first/4
# first //= 4    # Floor and assign  # first = first/4
# first **= 2   # Exponentiation and assign  # first = first**2
# first %= 3    # Modulus and assign  # first = first%3

# round_off = round(first)
# print(f"Final value of first after operations: {round_off}")

# print(first)  















# name = "Jalees"
# age = 25




# a = int(input("Enter first number: "))  # Placeholder
# b = int(input("Enter second number: ") ) # Placeholder



# print(a + b)  # Addition
# print(a - b)  # Subtraction
# print(a * b)  # Multiplication
# print(a / b)  # Division
# print(a % b)  # Modulus
# print(a // b)  # Floor Division
# print(a ** b)  # Exponentiation








