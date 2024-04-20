# How to find Factorial and no of Trailing zeros in a factorial of a number in python

def factorial(number):
    if number == 0 or number == 1:
        return 1
    else:
        return number * factorial(number - 1)

def factTrailingZero(number):
    # fac = factorial(number)
    # print(fac)
    # while (number % 10 == 0):
    #     count = count + 1
    #     number = number / 10
    # return count
    i = 5
    count = 0
    while(number // i != 0):
        count += int(number/i)
        i = i * 5
    return count

if __name__ == '__main__':

    number = int(input("Enter a number: "))

    # fac = factorial(number)
    # factTraiZero = factTrailingZero(number)

    # print(f"The factorial is {fac}")
    print(factTrailingZero(number))