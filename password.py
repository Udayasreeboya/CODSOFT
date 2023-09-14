import random
Alphabets_Lower="abcdefghijklmnopqrstuvwxyz"
Alphabets_Upper=Alphabets_Lower.upper()
digits="1234567890"
Special_Character="~`!@#$%^&*+-/|?"
password=Alphabets_Lower+Alphabets_Upper+Special_Character+digits
Length_of_password=int(input("Enter the size of password:"))
a="".join(random.sample(password,Length_of_password))
print(f"Your password is {a}")
