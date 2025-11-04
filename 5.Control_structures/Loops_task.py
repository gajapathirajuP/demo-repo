# Will use All Control Structures 

# Simulate ATM Pin Functionality (ATM/OTP/Passwords etc)

# The User will be prompted to enter Pin 

# The Pin should be 4 Digit only 

# Assume Correct OTP is stored in variable for comparison 

# If the OTP given is not 4 Digit Number Display Error Message

    # OTP Must be 4 Digit Number Only 

# If the OTP given is a 4 Digit Number and also correct OTP, Display 

    # Transaction Success 

# If the OTP given is incorrect, and is also not a 4 digit, then   

   # Transaction Failed 

# After 3 Attempts, Display

    # Maximum Attempts Reached, Try after 24 Hours # Simulate ATM Pin Functionality (ATM/OTP/Passwords etc)

actual_otp = 2345

# import random
# actual_otp = random.randint(1000,9999)
# print(f"OTP Generated sent to mobile {actual_otp}")

attempts = 3

# print(len(actual_otp))

while attempts > 0:
    print(f"You have {attempts} Attempts left")
    user_otp = int(input("Enter OTP: "))
    
    # check for 4 digit number
    if (len(str(user_otp))) != 4:
        print("OTP Must be 4 Digit")
        attempts -= 1
        continue
    
    if user_otp == actual_otp:
        print("Correct OTP - Transaction Success")
        break
    else:
        print("Incorrect OTP - Transaction Failed")
        attempts -= 1

else:
    print("Maximum Attempts Reached, Try After 24 Hours")