# Variables - named storage location in RAM which holds value or data.(Student_name/age/gpa is a variable) computer-> Memory-> Variable ( Syntax variable_name = value)
# = is assignment operator  and value is data what we store

# Variables
# Variables allows you to store data or assign data or retrieve data or manipulate data(If required)

#Assign Data (storing data)
Student_name = 'Raju' # String (datatype)
Student_age = 35 # Integer (datatype)
Student_gpa = 9.0 # Float (datatype)
Student_passed = True # boolean True/False (datatype)
student_unknown_data = None # represents no value

# Retrieve data -> print()
print (Student_name)
print (Student_age)
print (Student_gpa)
print (Student_passed)
print (student_unknown_data)



# How to combine variables with our statements 

# Retrieve data with statements -> Concatenation  can use both (+/,)  string to string // not with Int or float(numbers) use only coma(,)

#print ("Student_name:" Student_name ) Invalid syntax
print ("Student_name:" + Student_name) 
#print ("Student_age:" + Student_age) Invalid syntax
print ("Student_age:" , Student_age) 
#print ("Student_gpa:" + Student_gpa) Inavlid syntax
print ("Student_gpa:" , Student_gpa)
#print ("Student_passed:" + Student_passed) Invalid syntax
print ("Student_passed:" , Student_passed)
#print ("student_unknown_data:" + student_unknown_data) Invalid syntax
print ("student_unknown_data:" , student_unknown_data)


# How to know the memory address
# function does a task 
# Print is a function that prints standard output {print()}
# id is a function that show memory address {id()}
# type () : will display data type

# Get Identity / memory address
# print(id())

print ("===========")

print(id(Student_name))
print(id(Student_age))
print(id(Student_gpa))
print(id(Student_passed))
print(id(student_unknown_data))

print ("===========")

# Memory model of python  (If a value is already present pyhton will not craete a memory block instead it eill just use refernece.so memory is efficiently used.)(Reference below)

# Simple data type : holds "one value" in a variable . (Reference below)
# Example is int

# comple data type : holds "multiple values" in a single variable.
# Example is list

value_x = 10
value_y = 20
value_z =10

print(id(value_x))
print(id(value_y))
print(id(value_z))

print ("===========")


list_data_x = [10,20,30,40,50]
print(id(list_data_x))

list_data_z = [10,20,30,40,50]
print(id(list_data_z))

# In complex data type Data is same but diff memory address where as in simple data types same memoryy address will be seen.

#type () : will display data type

print ("===========")

print (type(Student_name))
print (type(Student_age))
print (type(Student_gpa))
print (type(Student_passed))
print (type(student_unknown_data))
print (type(list_data_z))

print ("===========")









 



