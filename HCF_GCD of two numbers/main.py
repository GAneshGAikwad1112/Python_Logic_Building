# HCF or GCD of the two numbers using python.....
# greatest common divisor (GCD) or highest common factor (HCF)

num1 = int(input("Enter First Number:\n"))
num2 = int(input("Enter Second Number:\n"))

if num2 > num1:
    mx = num1
else:
    mx = num2

for i in range(1, mx+1):
    if num1 % i == 0 and num2 % i == 0 :
        hcf = i


print(f"The HCF/GCD of these two numbers is {hcf}")
