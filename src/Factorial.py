Num1 = int(input("enter the Number1:"))
factorial = 1

for i in range(1,Num1+1):
    factorial = factorial * i
    
print(f"The factorial of {Num1} is {factorial}")