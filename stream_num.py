# write a python program which will keep adding a stream of numbers inputted by the user. The adding stops as soon  user presses q key on the keyboard.

sum = 0
while(True):
    userInput = input("Enter the price ir press q to quit:  \n")
    if (userInput != 'q'):
        sum = sum + int(userInput)
        print(f"Ordet total so far: {sum}")
    else:
        print(f"Your Bill total is {sum}. Thanks for shopping with us")
        break

