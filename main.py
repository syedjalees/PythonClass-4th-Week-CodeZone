# Comparison Operators    Compare karna is ka kaam hai
# Used to compare two values and return a boolean result (True or False).

#   symbols    names
# 1.   ==      Equal to
# 2.   !=      Not equal to
# 3.   >       Greater than
# 4.   <       Less than
# 5.   >=      Greater than or equal to
# 6.   <=      Less than or equal to




#  ==      Equal to
# a = 10
# b = 10
# print(a == b)  

# # !=      Not equal to 
# x = 10
# y = 10
# print(x == y)  
# print(x != y)



#   >   Greater than 
# a = 10
# b = 5
# print(a > b) 
# print(b > a) 
# # less than  
# print(a < b)
# print(b < a)


# >=      Greater than or equal to 


# a= 12
# b = 13

# print(a >= b) 


# <=      Less than or equal to 

# print(a <= b)  
# print(b <= a) 


# logical Opeators 
# Logical operators are used to combine conditional statements.

#   symbols      names
# 1.   and      Logical AND
# 2.   or       Logical OR
# 3.   not      Logical NOT

# and      Logical AND
# -> Return True if both the statements are true. or 100 true 0 false 
# a = 10
# b = 20
# print(a > 5 and b > 15)  # True
# print(a > 15 and b > 15)  # False 

# or       Logical OR 
# -> Return True if at least one of the statements is true.  1 true 99 false
# print(a > 5 or b > 15)  # True
# print(a > 15 or b < 15)

# not      Logical NOT 
# -> True becomes False and False becomes True. 

# print(not True)  # False
# print(not False)  # True

# print(not 10 > 5)  # False
# print(not 10 < 5)  # True



# Membership Operators 
# used to test if a value is found in a sequence (like a list, tuple, or string).
# 1. in 
# 2. not in 

# in -> returns True if the value is found in the sequence.
# print("a" in "apple")  # True
# print("b" in "apple")  # False

# print("a" in ["a","apple", "banana", "cherry"])  # True


# not in -> returns True if the value is not found in the sequence. 
# print("a" not in "apple")  # False
# print("b" not in "apple")  # True 
# print("a" not in ["a","apple", "banana", "cherry"])


# identity Operators 

# used to compare the memory location of two objects.

# 1. is 
# 2. is not

# is -> returns True if both variables point to the same object in memory.
# a = 10
# b = 10.0 
# print(id(a))  # Memory address of a
# print(id(b))  # Memory address of b
# print(a is b) 

# 2. is not -> returns True if both variables do not point to the same object in memory. 

# print(a is not b) 


# Conditional Statements
# Conditional statements are used to perform different actions based on different conditions.

# These are conditional statements used to make decisions in Python.
# They allow your program to execute certain blocks of code based on conditions.

# 1. if-else statement

# syntax 
# if condition:
#     # code to execute if condition is true
# else:
#     # code to execute if condition is false


# name = "Jalees"

# if name == "Jalees":
#     print("Welcome Jalees")
# else:
#     print("Bahir nikaalo")

# button = input("Press Button (on/off): ").lower()

# if button == "on":
#     print("Fan is ON")
# else:
#     print("Fan is OFF")



# 2. if-elif-else statement

# elif => elif block checks multiple conditions in one by one. 
#  stands for Else If --> elif

# syntax
# name = "Ahil"

# if name == "Jalees":
#     print("Welcome Jalees")
# elif name == "Ali":
#     print("Welcome Ali")
# elif name == "Ahmed":
#     print("Welcome Ahmed")
# else:
#     print("Bahir niklo bhai kon ho")


# marks = int(input("Enter your marks: "))
# if marks >= 90 and marks <= 100:
#     print("Grade A+")
# elif marks >= 80:
#     print("Grade A")
# elif marks >= 70:
#     print("Grade B")
# elif marks >= 60:
#     print("Grade C")
# elif marks >= 50:
#     print("Grade D")
# else:
#     print("Grade F")









