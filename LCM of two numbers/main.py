# LCM (least common multiple)

a = int(input("Enter a First Number: "))
b = int(input("Enter a Second Number: "))
maxNum = max(a, b)
while(True):
    if(maxNum % a == 0 and maxNum % b ==0):
        break
    maxNum = maxNum + 1  

print(f"The LCM of {a} and {b} is {maxNum}")