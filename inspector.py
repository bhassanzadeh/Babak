import sys

# first, we check that the argument is OK with 2 checks
#  length of sys.argv should be 2 (for 1 argument)
if len(sys.argv) != 2:
    print('Error: The input should be a single argument')
    sys.exit()

n = int(sys.argv[1])

#  n should be positive
if n < 0:
    print('The argument should be positive')
    sys.exit()

# *******************************************
# check if the number is odd
def isOdd(x):
    if x % 2 == 0:
        print("The number %s is not odd." %x)
    else:
        print("The number %s is odd." %x)

isOdd(n)

# *******************************************
# check if the number is square
def isSquare(x):
    for i in range(int(x/2) + 2):
        if i * i == x:
            print("The number %s is square." % x)
            return

    print("The number %s is not square." % x)

# call the function
isSquare(n)
# *******************************************
# check if the number is increasing
def isIncreasing(x):
    st_x = str(x)
    for i in range(len(st_x) - 1):
        if st_x[i] > st_x[i + 1]:
            print("The number %s is not increasing." % x)
            return
    print("The number %s is increasing." % x)


isIncreasing(n)

# *******************************************
# check if the number is palindrome
def isPalindrome(x):
    str_x = str(x)
    # str_x[::-1] reverses the digits
    if str_x == str_x[::-1]:
        print("The number %s is a palindrome." % x)
    else:
        print("The number %s is not a palindrome." % x)

isPalindrome(n)

# *******************************************
# check if the number is factorial
def isFactorial(x):
    result = 1
    for i in range(1, x + 1): # for all numbers from 1 to x
        result = result * i
        if result == x:
            print("The number %s is a factorial." % x)
            return

    print("The number %s is not a factorial." % x)

isFactorial(n)
