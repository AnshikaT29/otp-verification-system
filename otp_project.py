import random
 
otp = random.randint(1000,9999)
print("Your OTP is:", otp)

attempts = 3

while attempts > 0:
    user_input= int(input("Enter the OTP:"))

   if user_input == otp:
     print("OTP Verified Successfully!")
    break
   else:
      attempts -= 1
      print("Invalid OTP! Attempts left:", attempts)

    if attempts == 0:
        print("Too many wrong attempts. Access Denied.")

