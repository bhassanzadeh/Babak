# for each x between 0 and 100, check multiples of 5, 7 and 13
for i in range(1, 101):
    # check for multiples of all three (5, 7, 13)
    if i % 5 == 0 and i % 7 == 0 and i % 13 == 0:
        print('%s is a multiple of 5 and 7 and 13!' %i)
    # check for multiples of any two (5, 7), (5, 13), (7, 13)
    elif i % 5 == 0 and i % 7 == 0:
        print('%s is a multiple of 5 and 7!'%i)
    elif i % 5 == 0 and i % 13 == 0:
        print('%s is a multiple of 5 and 13!'%i)
    elif i % 7 == 0 and i % 13 == 0:
        print('%s is a multiple of 7 and 13!'%i)
    # check for multiples of only one (5 or 7 or 13)
    elif i % 5 == 0:
        print('%s is a multiple of 5!'%i)
    elif i % 7 == 0:
        print('%s is a multiple of 7!'%i)
    elif i % 13 == 0:
        print('%s is a multiple of 13!'%i)
