import random as r
lower_letters="abcdefghijklmnopqrstuvwxyz"
upper_letters="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers="1234567890"
symbols="!@#$%^&*{}[]<>"
all=lower_letters + upper_letters + numbers + symbols
length=int(input("Enter the length of the password:"))
password=r.sample(all,length)
print("".join(password))
