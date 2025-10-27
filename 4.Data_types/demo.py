# Data Types : DT are categories that define what kind of data a variable can hold.
# Python is dynamic typed language(assumes type based on value)
# 1. Numeric Type
# int : 1,2,3,4,0,-1,-2 etc.,
# float : 2.3,11.11,2.3 etc
# complex : a + ib (i si imaginary)   /   a + bj (in pyhton)

data = 11
print(type(data))

data = -11
print(type(data))

data = 11.5
print(type(data))

#data = 4 + i6
#print(type(data))

data = 4 + 6j
print(type(data))

# Text Type
# String : sequence of characters enclosed inside ('' or "")

data = "hi everyone"
print(type(data))

# Boolean Type : Represents True or False

data = True
print(type(data))

data = False
print(type(data))

# None Type : Represents nothing i.e., absence of value

data = None
print(type(data))

# Sequence Type

# String is also a sequnce type
# List is complext data type it holds multiple values,represented using [].Mutable (Can be changed)
# Tuple is complex data type holds multiple values represented using (). Imutable (Can't be changed)

data = [1,2,3,4,5]
print(type(data))

data = ["hi,hello,bye"]
print(type(data))

data = ["hi,hello,bye"]
print(data)

data = (1,2,3,4,5)
print(type(data))

# Set Type
# Set : complex data type holds multiple values ( unique data -> No duplicates) represented using {}.Mutable (Can be changed)
# frozenset : complex data type holds multiple values ( unique data -> No duplicates) represented using frozenset class. Imutable (Can't be changed)

data = (1,2,3,4,5,1)
print(type(data))
print(data)
print(len(data))

data = {1,2,3,4,5,1}
print(type(data))
print(data)
print(len(data))

data = frozenset({1,2,3,4,5,1})
print(type(data))
print(data)

# Map Type
# dictionary : complex data type holds multiple key & values represented using {}.Mutable (Can be changed)

data = {"name" :" raju","age" : 35,"gender" : "M"}
print(type(data))
print(data)

# Note : All the above datatypes are predefined in pyhton standard library.
# Note : Based on custom requirements we can create our own datatypes also.
# Syntax Class CustomDataType : Statements

class Employee:
    Employee_id = 111
    Employee_name = "Raju"
    Employee_grade = 1

data = Employee()
print(type(data))   

# Type casting
    # converting one datatype to another (based upon requirements) (Explicit)manually not by python.
    # generally not safe data loss may occur
    # we use some predefined functions
# Type Conversion   
    #  converting one datatype to another automatically by python (Implicit)
    #  safe and no data loss

# Type Conversion : Implicit automatically done

a1 = 10
a2 = 5.5
sum = a1 + a2
print(sum)    
print(type(sum))

# Type casting : Explicit manually done using some functions.

Final_price = 1234.5 # float
Final_price_int = int(Final_price)
print(Final_price)
print(type(Final_price))
print(Final_price_int)
print(type(Final_price_int))


rating ="3"
rating = int(rating)

if rating < 5:
    print('Customer not satisfied')
else:
    print('Customer satisfied')    

















