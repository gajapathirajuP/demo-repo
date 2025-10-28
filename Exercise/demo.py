Principal_loan_amount = float(input("Enter the loan amount(p): "))
annual_intrest_rate = float(input("Enter the annual interest rate (in %): "))
tenure_years = int(input("Enter the loan tenure (in years): "))

monthly_intrest_rate = annual_intrest_rate / (12 * 100)
tenure_months = tenure_years * 12

emi = (Principal_loan_amount * monthly_intrest_rate * (1 + monthly_intrest_rate)**tenure_months) / ((1 + monthly_intrest_rate)**tenure_months - 1)

print(f"Your Monthly EMI is: ₹{emi:.2f}")



# === Student Fee Calculation Program ===

# 1. Collect Student Name
Student_Name = input("Student Name: ").strip()

# 2. Collect and validate Student Grade
while True:
    try:
        Student_Grade = int(input("Student Grade (1-12): ").strip())
        if 1 <= Student_Grade <= 12:
            break
        else:
            print("Grade must be between 1 and 12.")
    except ValueError:
        print("Invalid input! Enter a number between 1 and 12.")

# 3. Collect Base Tuition Fee (default 30000)
Default_fee = 30000.0
user_input = input(f"Base Tuition Fee [default {Default_fee}]: ").strip()

if user_input:
    try:
        Base_Tuition_Fee = float(user_input)
    except ValueError:
        print("Invalid input! Using default fee.")
        Base_Tuition_Fee = Default_fee
else:
    Base_Tuition_Fee = Default_fee

# 4. Collect Academic Topper status
while True:
    Academic_Topper = input("Academic Topper (Yes or No): ").strip().lower()
    if Academic_Topper in ["yes", "no"]:
        break
    else:
        print("Invalid input! Enter 'Yes' or 'No'.")

# 5. Calculate Base Discount
discount_percent = 0

if 9 <= Student_Grade <= 12:
    if Academic_Topper == "yes":
        discount_percent = 20
    else:
        discount_percent = 10
elif 6 <= Student_Grade <= 8:
    discount_percent = 5
else:
    discount_percent = 0

# 6. Apply Additional Discounts
additional_discount = 0
if Student_Grade == 10:
    additional_discount = 3
elif Student_Grade == 12:
    additional_discount = 5

total_discount = discount_percent + additional_discount

# 7. Calculate discount amount and final fee
discount_amount = (total_discount / 100) * Base_Tuition_Fee
final_fee = Base_Tuition_Fee - discount_amount

# 8. Display summary
print("\n===== Student Fee Details =====")
print(f"Student Name       : {Student_Name}")
print(f"Student Grade      : {Student_Grade}")
print(f"Base Tuition Fee   : {Base_Tuition_Fee}")
print(f"Academic Topper    : {Academic_Topper.capitalize()}")
print(f"Base Discount      : {discount_percent}%")
print(f"Additional Discount: {additional_discount}%")
print(f"Total Discount     : {total_discount}% -> {discount_amount}")
print(f"Final Tuition Fee  : {final_fee}")
print("================================")
