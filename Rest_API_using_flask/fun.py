def sum(a, b):
    return a+b

def avg(a, b):
    return ( a + b)/2

def arm(number):
    sum = 0
    order = len(str(number))
    copy_number = number
    while(number>0):
        digit = number % 10
        sum += digit ** order
        number = number // 10

    if (sum == copy_number):
        print(f"\nThis number is Armstrong number! {copy_number}\n")
        return True
    else:   
        print(f"\nThis number is not a Armstrong number! {copy_number}\n")
        return False
    
    