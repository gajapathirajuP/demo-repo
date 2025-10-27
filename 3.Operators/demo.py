# Operators  ( operators are special symbols performs operations on variable and their values) manipulate data 

# There are diff type of operators  

# Arthimetic operators (+ - * /) Mathematical calculations
# // floor division (same as division but roudsoff the value)
# ** Exponentation (calculating the power)

#Interpolation : This technique replaces place holders with actual value dynamically using f-strings (formatted string literals) use F with print and {}
#as place holders
num1 = 10
num2 = 5

print("The sum of Two Numbers:",num1+num2)

print("-------")

print(f"The sum of {num1} and {num2} is {num1+num2}")

print("-------")

print(f"The difference of {num1} and {num2} is {num1-num2}")

print(f"The product of {num1} and {num2} is {num1*num2}")

print(f"The division of {num1} and {num2} is {num1/num2}")

print(f"The modulus of {num1} and {num2} is {num1%num2}")

print(f"The floor division of {num1} and {num2} is {num1//num2}")

print(f"exponentiation of {num1} and {num2} is {num1**num2}")


print("-------")

# compound assignement operators
# assignment operator is = used for assigning a value
# CAO combine artithmatic and assignment opeartor . used for concise code.

#x = 10
#x = x + 5 (long hand)
#x += 5 (short hand)

# increment / Decrement : ++  --  pyhton doesnt support this syntax , in python CAO are used.

# below is without CAO

num = 10
num = num + 5
print(num)

print("-------")

# below is with CAO

num = 10
num += 5
print(num)

num = 10
num *= 5
print(num)

print("-------")

# increment

count = 10
count += 1
print (count)

# decrement

count = 10
count -= 1
print (count)

print("-------")


# Comparision Operators 
# used for comparing values and results in boolean (True/False) especially used in conditionals
# == != < > <= >=

num1 = 10
num2 = 5
print(num1 == num2)
print (num1 != num2)
print(num1 < num2)
print(num1 > num2)

print("-------")

#Logical operators
# to perform logical operations and mainluy used to check multiple conditions and results in boolean(True/False)
# and : validates when both or multiple  conditions are true.
# or : If one of the conditions are true.  
# not : negates , If true then false and viseversa.

# x     y  x and y    x or y   not x  not y
# T     T     T         T        F      F
# T     F     F         T        F      T
# F     T     F         T        T      F
# F     F     F         F        T      T

print("-------")

num1 = 10
num2 = 5
num3 = 1
num4 = 2

print(num1 > num2) 
print(num3 > 4)
print(num1 > num2 and num3 > num4)
print(num1 > num2 and num3 < num4)
print(num1 > num2 or num3 > num4)
print(num1 < num2 or num3 > num4)
print(not num1 < num2)

print("-------")

# Membership operators : used for checking if an object is in sequence .
# in: Returns true , if object given is in sequence
# not in: Returns true , if object givenis not in sequence

data = "python is a programming language"

find_word = "java"

found = find_word in data

print(found)

print("-------")

data = "python is a programming language"

find_word = "python"

found = find_word in data

print(found)

print("-------")

data = "python is a programming language"

find_word = "java"

found = find_word not in data

print(found)


print("-------")

#Identity operators :used to check if both objects are same ( Technically they will check memory addresses)
# is : Returns true if objects are same 
# is not : returns true if objects are not same.

n1 = 10
n2 = 10
print(n1 is n2)

print("-------")

n1 = 10
n2 = 10
n3 = 1
print(n1 is n3)

print("-------")

m1 = [10,20]
m2 = [10,20]
print( m1 is m2)

print("-------")

# Bitwise operators : used in lo-level programming.(might not used often)(01010101100)
# & : if both the bits are 1 ,the result is 1
# | : if one of the bits is 1 then the result is 1
# etc : 

n1 = 5 #0000000000000101
n2 = 3 #0000000000000011
       #0000000000000001 & 
       #0000000000000111 |

print(n1 & n2)
print(n1 | n2)

print("-------")





















