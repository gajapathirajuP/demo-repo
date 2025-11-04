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


# Terenary operator / conditional expression: it provides a concise way to write an if-else statement on a single line.
                      # It evaluates a condition and returns one of two values based on whether the condition is true or false.    

# Syntax : value_if_true if condition else value_if_false     

age = int(input("Enter Your age: "))

Status = "You can vote" if age >= 18 else "You can't vote" 

print(Status)

# elif ladder
# elif (elase if) : It is used in conditional statements to check for multiple conditions sequentially after an intial "if " statement.

#  -> syntax 
            #if condition:
                #statements
            #elif condition:
                #statements
            #elif condition:
                #statements
            # .    
            # .    
           #else:
                #statements

marks = int(input("Enter your marks: "))
if marks >= 90:
    print("A")
elif marks >= 75:
    print("B")
elif marks >= 60: 
    print("C") 
elif marks >= 50: 
    print("D")  
elif marks >= 35: 
    print("E")        
else:
    print("F")    

# match-case ( available only from python 3.X)    
# like elif we have match-case in pyhton for checking multiple conditions
# In other languages like java / c++ we had (switch case)
# Offers a more expressive and readable alternative to complex if-elif-else chains
#syntax
            #match expression:
                #case pattern1:
                    # Code block 1
                #case pattern2:
                    # Code block 2
                # ...
                #case _:  # Optional wildcard/default case
                    # Default code block

choice = int(input("Enter Your Choice: "))   
match choice:
    case 1:
        print("Option 1 selected")
    case 2:
        print("Option 2 selected")  
    case 3:
        print("Option 3 selected")  
    case 4:
        print("Option 4 selected")   
    case _:
        print("Default Option selected")     

 #Nested Conditionals 
 #Conditionals inside Conditionals                              

# Voting app with identity verification -> incorrect approach
age = int(input("Enter Your Age: "))
has_id = input("Do You Have ID (yes/no): ")
if age >=18 :
    print("You can vote")
elif has_id == "yes":
    print("You can vote as you have ID")
else:
    print("You cannot vote")

# Voting app with identity verification using nested conditionals 
age = int(input("Enter Your Age: "))
if age >=18 :
    has_id = input("Do You Have ID (yes/no): ")
    if has_id == "yes":
       print("You can vote")
    else:
        print("You need an ID to vote") 
else:
    print("You cannot vote")




    




  
       