# AIM: Design a Python program to compute 
# the factorial of a given integer N.
# Coder: Qureshi Atif
# Date:30/1/26

print("--- Factorial Finder ---\n")

n = int(input("Enter Number: "))
factorial = 1

if n >= 0:
    for i in range(1, n + 1):
        factorial = factorial * i
    print(f"Factorial of {n} is {factorial}")
else:
    print(f"Factorial of {n} is Not Defined")
