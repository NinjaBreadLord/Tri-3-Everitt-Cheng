{% include navbar.html %}

## Crossover Code Snippets

Imperative Prime
```
def findprimes(a, b):
dne = True
for i in range(a, b + 1):
    count = 0
    for g in range(2, (i // 2 + 1)):
        if (i % g == 0):
            count = count + 1
            break
    if (count == 0 and i != 1):
        dne = False
        # changes dne to False if there is a prime number is found
        print(" %d" %i, end=' ')
if dne:
    print("There are no prime numbers within this interval")
    # prints if dne is True, meaning that there was no prime numbers found
else:
    print()
```
