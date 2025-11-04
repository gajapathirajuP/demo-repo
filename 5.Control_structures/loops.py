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



    # for loop     
    # for loops are used to iterate over a sequence (like a list, tuple, string, or range) or other iterable objects.   
    # The loop executes a block of code once for each item in the sequence.
    # We use for generally, when we  know number of Iterations in advance
    # syntax
        # for var in sequence:
            # print(var)