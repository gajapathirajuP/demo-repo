Principal_loan_amount = float(input("Enter the loan amount(p): "))
annual_intrest_rate = float(input("Enter the annual interest rate (in %): "))
tenure_years = int(input("Enter the loan tenure (in years): "))

monthly_intrest_rate = annual_intrest_rate / (12 * 100)
tenure_months = tenure_years * 12

emi = (Principal_loan_amount * monthly_intrest_rate * (1 + monthly_intrest_rate)**tenure_months) / ((1 + monthly_intrest_rate)**tenure_months - 1)

print(f"Your Monthly EMI is: ₹{emi:.2f}")