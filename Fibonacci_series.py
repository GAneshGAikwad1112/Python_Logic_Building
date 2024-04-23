import time

def fibSeries(n):
    previousNum = 0
    currentNum = 1
    for i in range( 1, n):
        previouspreviousNum = previousNum
        previousNum = currentNum
        currentNum = previousNum + previouspreviousNum
    return currentNum

def fibRecur(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibRecur (n-1) + fibRecur (n-2)
    
if __name__=="__main__":
    num = int (input("Enter a Number: "))
    init = time.time()
    print(f"Using recursion value of fib({num}) is {fibRecur(num)}")
    print(f"Using recursion value of fib({num}) is {fibSeries(num)}")
    print( f"It took {time.time() -init } seconds")