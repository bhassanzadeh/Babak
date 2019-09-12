# for every 3-digit number:
for n in range(100, 1000):
    sum = 0
    # find the sum of every divisor of n
    for i in range(1, n):
        # check if n can be divided by i
        if n % i == 0:
            sum = sum + i
    # check if it is a perfect number, if it is, print its divisors
    if n == sum:
        print ('1'),
        for i in range(2, n):
            # check if n can be divided by i
            if n % i == 0:
                print('+ %s' %i),
        print(' = %s' %n)