# Control Structures / Statements
    # Control structures helps you determine the flow of execution in a program, allowing you to make decisions and repeat tasks.

# Python has given three types of Control structures

    # Conditional Statements / Structures (Decision Making Statements)    
    # Looping Statements / Structures (Iteration Statements)
    # Branching Statements / Structures (Jumping Statements)

# Indentation 
    
    # Indentation in Python is a fundamental and mandatory aspect of its "syntax", used to define the structure and hierarchy of code blocks. 
    # Unlike many other programming languages that use curly braces or keywords to delineate blocks, Python relies entirely on consistent indentation.

# Using space correctly 

    # Python allows for any consistent number of spaces or a single tab(4 spaces) for indentation, the widely accepted and recommended standard.
    # At least one space but recommended is 4 space i.e tab 


# Indentation 

print("Hello")

# Conditional statements

    # Used to run a "block of code" based on a condition result

    # if 
    # runs a block of code, if the condition is True 
    # syntax
        # if condition:
            #statements 

if 5 > 2:
#print("Yes true")     
    print("Yes true") 
    print("I want the print this too")   

if 5 > 10:
    print("Yes true")

if 10 > 5:
  print(" Its correct")     


# if else

    # runs a block of code, if the condition is True and  runs another block of code, if the condition is False 

    # syntax
      # if condition:
        # statements 
      # else:   
        # statements

# NOTE : input() function reads input from a user.

# if condition


num = -10
if num > 0:
    print(f"Number {num} is positive")
if num < 0:
    print(f"Number {num} is negative")    


# if else condition  

num = 10
if num > 0:
    print(f"Number {num} is positive")
else:
    print(f"Number {num} is negative")  

# Voting eligibility

age = 12
if age >= 18:
    print("You can vote")
else:
    print("You can't vote")    

# input function 

name = input("Enter Name: ")
print(f"Welcome {name}")
session = input("Enter course name: ")
print(f"Your course name {session}")


num1 = input("Enter Number: ")
num2 = input("Enter Number: ")
sum = num1 + num2 #concatenation
print(sum)

num1 = int(input("Enter Number: "))
num2 = int(input("Enter Number: "))
sum = num1 + num2
print(sum)


age = int(input("Enter Your age: "))
if age >= 18:
    print("You can vote")
else:
    print("You can't vote")    




  
       