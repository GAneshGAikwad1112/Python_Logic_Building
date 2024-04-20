# creating a password generator using python

import string
import random

if __name__ == "__main__":
    s1 = string.ascii_letters + string.digits + string.punctuation
    plen = int(input("Enter a password length: "))

    s =[]
    s.extend(list(s1))
    random.shuffle(s)
    print()
    print("Your password is:","".join(s[0:plen]))
    