def findprimes(a, b):
    for i in range(a, b + 1):
        count = 0
        for g in range(2, (i // 2 + 1)):
            if (i % g == 0):
                count = count + 1
                break
        if (count == 0 and i != 1):
            print(" %d" %i, end=' ')
    print()

def primeTester():
    a = int(input("Enter the Minimum: "))
    b = int(input("Enter the Maximum: "))
    findprimes(a, b)