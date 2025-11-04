# Looping Statements (Iteration Statements)
# Loops in Python are used to repeatedly execute a block of code.
# When you want to do a task multiple times, use loops
# Python offers two primary types of loops
    # "while" loops 
    # while loops execute a block of code repeatedly as long as a specified condition remains True.
    # We use while generally, when we don't know number of Iterations in advance.
    # syntax
        # while condition:
            #statements
# password authentication -> forgot password, you'll keep trying till password is matched 
# at what attempt password is matched ?? 

actual_password_db = "2345"
user_given_password = ""

while user_given_password != actual_password_db:
    user_given_password = input("Enter Password: ")

print("Password Matched, Login Success")

# while
count = 0
while count < 3:
    print(f"Count is: {count}")
    count += 1


    # for loop     
    # for loops are used to iterate over a sequence (like a list, tuple, string, or range) or other iterable objects.   
    # The loop executes a block of code once for each item in the sequence.
    # We use for generally, when we  know number of Iterations in advance
    # syntax
        # for var in sequence:
            # print(var)

# for loop for sequence
list_numbers = [10,20,30,40,50]
print(list_numbers)

for num in list_numbers:
    print(num)    

# result = 10 * 10    
# result = 10 * 20
# result = 10 * 30

for num in list_numbers:
    #print(f"{num} * {10}")
    print(num * 10)   

simple_number = 12345   #TypeError: 'int' object is not iterable

#for num in simple_number:
    #print(num) 

# How do i know, if an object is iterable ?

                # use dir() 
                # dir() function in Python is a built-in function used for introspection, allowing you to discover the attributes and methods of an object     

# print(dir(simple_number)) # no __iter__

# print(dir(list_numbers)) # __iter__   


# for - when we  know number of Iterations in advance 
print("Hi")

# Say Hi for 10 times
print("Hi")
print("Hi")
print("Hi")
print("Hi")
print("Hi")
print("Hi")
print("Hi")
print("Hi")
print("Hi")
print("Hi")


# range() 

                # The range() function in Python generates an immutable sequence of numbers. 
                # It is commonly used for iterating a specific number of times in for loops. 

                # range(start, stop, step): This form generates a sequence of numbers starting 
                # from start (inclusive) up to, but not including, the stop value, 
                # with an increment of step. The step can be positive or negative.

                    # range(start, stop, step)
                        # start default is 0 (included) (inclusive)
                        # stop at this value (excluded) (exclusive)
                        # step is increment (default step is 1)

# range() - generates an immutable sequence of numbers
for num in range(5):
    print(num)    

for num in range(10):
    print(num)       

for num in range(5,11):
    print(num)    

for num in range(2,11,1):
    print(num)

for num in range(2,11,2):
    print(num)    

for num in range(5,100,5):
    print(num)    

for num in range(10, 0, -1):
    print(num)    

# Say Hi for 10 times
for greet in range(10):
    print("Hi")


