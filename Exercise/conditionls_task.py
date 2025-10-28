Student_Name = (input("Student Name: "))

Student_Grade = int(input(f"Student Grade : "))
if Student_Grade < 1 or Student_Grade > 12 :
    print(f"Student Grade {Student_Grade} is not between 1-12 Grades")

Base_Tution_Fee = 30000.0
user_input = input(f"Base Tution Fee: {Base_Tution_Fee}")

Academic_Topper = (input("Academic Topper: "))
if Academic_Topper != "Yes" and Academic_Topper != "No":
    print(f"Academic_topper is entered as {Academic_Topper}. It should be either Yes or No")

Discount_percent  = 0
if Student_Grade >= 9 and Student_Grade <= 12:
    if Academic_Topper == "Yes":
        Discount_percent = 20
    else:
        Discount_percent = 10
elif Student_Grade >= 6 and Student_Grade <= 8:
    Discount_percent = 5
else:
    Discount_percent = 0 

Additional_discount = 0
if Student_Grade == 10:
   Discount_percent += 3
elif Student_Grade == 12:
     Discount_percent += 5    

discount_amount = (Discount_percent / 100) * Base_Tution_Fee
final_fee = Base_Tution_Fee - discount_amount    

print(f"Discount Applied: {Discount_percent}% -> {discount_amount}")
print(f"Final Tuition Fee: {final_fee}")





