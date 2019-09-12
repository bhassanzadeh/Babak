# for any number between 0 to 300 in steps of 20 (0, 20, 40, ....)
for f in range(0, 301, 20):
    # formula to find celc to fer
    c = (f - 32.0) * 5.0 / 9.0
    print('%s F = %.2f C' %(f, c))