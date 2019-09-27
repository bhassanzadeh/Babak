# generate square numbers between (1000000 and 10000000)
# the square root of 10^6 is 1000
# the square root of 10^7 is 3162.3
# so we only check numbers between 1000 and 3163
for i in range(1000, 3163):
    number = i * i
    # check first letter and last letter, second letter with the 5th number
    # and so on
    str_number = str(number)
    if (str_number[0] == str_number[6] and
        str_number[1] == str_number[5] and
        str_number[2] == str_number[4]):
        print("%s is a palindrome" %str_number)
