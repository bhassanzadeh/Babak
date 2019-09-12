import sys

# checks for correctness of argument
if len(sys.argv) != 2:
    print("Usage: python " + sys.argv[0] + " <first integer>")
    sys.exit()

n = int(sys.argv[1])

if n <= 0:
    print("argument should be a positive integer")
    sys.exit()

# set the first number to 0 and second to 1
first = 0
second = 1
if n == 1:
    print(first)
elif n == 2:
    print(second)
else:
    for i in range(n-1):
        current_number = first + second # add the last two numbers
        # update the numbers
        first = second
        second = current_number
    print(current_number)
