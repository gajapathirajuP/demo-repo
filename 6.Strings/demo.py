 # Strings 

        # Strings are one of the most widely used Datatype in any programming language

        # In Python, a string is a sequence of characters, used to represent text. 
            # Strings are a fundamental data type and are widely used for 
            # handling and manipulating textual information.

        # Strings are enclosed in double quotes ("") or single quotes('') or 
            # triple quotes(''' ''') or (""" """)

            # single line strings : use double quotes ("") or single quotes('')

            # multi line strings : use triple quotes(''' ''') or (""" """)

        # Rules When Defining Strings 

            # strings must be defined in  double quotes ("") or single quotes('') or 
            # triple quotes(''' ''') or (""" """)

            # When you use single quote in a string, enclose them in double quotes 
            # When you use double quote in a string, enclose them in single quotes 
            # When you use both single quote and double quote in a string, 
                # enclose them in triple quotes 

# Strings 

# define single line strings 
s1 = "hello"
print(s1)

s2 = 'hello'
print(s2)

s3 = '''hello''' # not recommended, as it's a single line string 
print(s3)

s4 = """hello""" # not recommended, as it's a single line string 
print(s4)  

# define multi line strings  
# define_python = "Python is a high-level, general-purpose programming language. 
#         Its design philosophy emphasizes code readability 
#         with the use of significant indentation."
# print(define_python) # SYntaxerror : unterminated string lateral.

define_python = """Python is a high-level, general-purpose programming language. 
        Its design philosophy emphasizes code readability 
        with the use of significant indentation."""
print(define_python)

define_python = '''Python is a high-level, general-purpose programming language. 
        Its design philosophy emphasizes code readability 
        with the use of significant indentation.'''
print(define_python)

# need a single quote in a string # double quotes 
question = "how are you ?"
# answer = 'i'm fine'
answer = "i'm fine"
print(answer)

# need a double quote in a string # single quotes 
question = "how are you ?"
# answer = "i"m fine"
answer = 'i"m fine'
print(answer)

# need both single & double quote in a string # triple quotes 
question = "how are you ?"
answer = '''i"m fine i'm fine'''
print(answer)



 # Accessing Strings

    # Indexing 

        # String indexing in Python allows access to individual characters within a string 
        # using their "position", known as the "index". 
        
        # Python uses zero-based indexing, meaning the first character is at index 0, 
            # the second at index 1, and so on.
        
        # Positive Indexing:
           # Starts from the beginning of the string.
           # The index of the first character is 0.
        
        # Negative Indexing:
            # Starts from the end of the string.
            # The index of the last character is -1.

        # text = "python"
            
            # 0  1  2  3  4  5   [Positive Indexing]
            # p  y  t  h  o  n
            #-6 -5 -4 -3 -2 -1  [Negative Indexing]

        # syntax

            # string[index]

            # NOTE : Accessing invalid index will raise error (IndexError)

# Accessing Strings 
text = "python"
print(text)

# Access characters using index 
# Positive Index
print(text[0])
print(text[1])

# Negative Index
print(text[-1])
print(text[-2])

# print(text[10]) # IndexError: string index out of range

# Access all characters 
print(text[0])
print(text[1])
print(text[2])
print(text[3])
print(text[4])
print(text[5])

# Access all characters 
text = "python"
for char in text:
    print(char)

# len() used to check the number of characters 
print("Length Of String: ",len(text))        

 # Slicing 

        # String slicing in Python is a method for extracting a portion (substring) 
        # from a larger string. It utilizes the slice operator [] with specific 
        # indices to define the desired segment.

        # syntax 

            # string[start:end:step]

                # start (optional): The index where the slice begins (inclusive). If omitted, it defaults to 0 (the beginning of the string).
                # end (optional): The index where the slice ends (exclusive). The character at this index is not included. If omitted, it defaults to the length of the string (the end of the string).
                # step (optional): The increment between each index during slicing. If omitted, it defaults to 1. A negative step value can be used to slice in reverse.

            # Earlier range()
                
               # range(start,end,step)

# slicing # string[start:end:step]
text = "python"
print(text[:])
print(text[::])
print(text[0:3:1]) # pyt
print(text[1:3]) # yt
print(text[0:5:2]) # pto

        #     0  1  2  3  4  5   [Positive Indexing]
        #     p  y  t  h  o  n
        #    -6  -5 -4 -3 -2 -1  [Negative Indexing]

print(text[-4:-1:1]) # tho
print(text[-4:-1:-1]) # empty
print(text[-4:-6:-1]) # ty     


 # String Concatenation 

        # Joining the strings 

    # Formatted String Literals (f-strings)

        # Using Interpolation {} with f 

# String Concatenation 
s = "good"
m = "morning"
print(s+m)

age = 30
# print("My Age is: "+age) # TypeError: can only concatenate str (not "int") to str

# Formatted String Literals (f-strings)
print(f"My Age is: {age}")


    # String Repetition 

        # Repeat strings using "*" operator

# String Repetition 
laugh = "HaHaHa"
print(laugh)

hard_laugh = laugh * 10
print(hard_laugh)        

    # String Immutability 

        # Strings are Immutable in nature (immutable == cannot be changed)

# String Immutability 
greet = "hello" # -> Hello
print(greet)
print(greet[0])
# greet[0] = "H" # TypeError: 'str' object does not support item assignment
list_greet = ['h','e','l','l','o']
print(list_greet)
print(list_greet[0])
list_greet[0] = "H"
print(list_greet)
print(list_greet[0])


    # String Methods 

        # String methods in Python are built-in functions that operate on 
        # string objects, allowing for various manipulations, transformations, and checks. 
        # It is important to note that strings in Python are immutable, 
        # meaning these methods do not modify the original string but 
        # instead return a new string with the applied changes.

        # https://docs.python.org/3/library/stdtypes.html#string-methods

# string methods
print(dir(greet))

# String Methods / Operations 

# Simulate Gmail Functionality 
# RAvi2KRisHnA -> ravi2krishna@gmail.com 
email = input("Enter Your Email ID: ")
format_email = email.lower().strip()+"@gmail.com"
print("Original Email: "+email)
print("Formatted Email: "+format_email)

# Simulate PAN Functionality 
# https://www.pan.utiitsl.com/panonline_ipg/forms/csfPan.html/csfPreForm

pan = input("Enter PAN ID: ")
# print(pan.isalnum())
if pan.isalnum():
    format_pan = pan.upper()
    print("Given PAN: "+pan)
    print("Formatted PAN: "+format_pan)
else:
    print("Invalid PAN ID")
    
# Simulate Phone ISD Scenario 
# https://us1.discourse-cdn.com/flex016/uploads/weweb/original/2X/d/dbe25afb4aeb05640347e2f7c1b7ae532ebb28f2.png

mobile_number = input("Enter Phone Number With ISD Code: ")

if mobile_number.startswith("+91"):
    print("Calling India Number - Charged In Rupees")
elif mobile_number.startswith("+1"):
    print("Calling USA Number - Charged In Dollars")
elif mobile_number.startswith("+33"):
    print("Calling France Number - Charged In Euros")
else:
    print("Calling Support To Only - India, USA & France")

# Simulate Email Synchronization
source_email = input("Enter Source Email ID: ")   
destination_email = input("Enter Destination Email ID: ")   

if source_email.endswith("@gmail.com") and destination_email.endswith("@gmail.com"):
    print("Email Synchronization Started")
else:
    print("Email Synchronization Failed")
    
# Simulate CSV Data from a file and perform operations
# Name, Email, Age, City, Job_Role
emp_john_data = "John,john@gmail.com,25,hyderabad,developer"
print(emp_john_data)

# Req : Display Only Emp Name & Emp Job Role
print("Name: "+emp_john_data[0])
print("Job Role: "+emp_john_data[-1])

data_parts = emp_john_data.split(",")
print(data_parts)

print("Name: "+data_parts[0])
print("Job Role: "+data_parts[-1])

# Simulate Amazon Order Email Confirmation
order_template = "Hello, your order with {order_id} has been shipped"
order_ids = "AMZ-IN-8909,AMZ-IN-7530,AMZ-IN-2312"
order_print = order_ids.split(",")

for order_id in order_print:
    user_email = order_template.replace("{order_id}",order_id)
    print(user_email)


