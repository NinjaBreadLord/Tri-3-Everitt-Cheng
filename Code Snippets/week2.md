{% include navbar.html %}


Factorial Class 
```
class Factorial:
  def __init__(self):
    self.factorial = [1,1]
    
  def __call__ (self,num):
    if num <= 1:
      pass #goes to the end return statement
    else:
      self.factorial.append(num * self(num-1)) 
    return self.factorial[num]
```
Prime finder in range imperatively 

```
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
```
Prime Finder Class
```
class Prime:
  def __init__(self):
    self.prime = []
  def __call__(self, a, b):
    for i in range(a, b + 1):
        count = 0
        for g in range(2, (i // 2 + 1)):
          if (i % g == 0):
            count = count + 1
            break
        if (count == 0 and i != 1):
          self.prime.append(" %d" % i)
    return ' '.join(self.prime)
```
Prime Finder Class Output 
```
def primeOOPTester():
  a = 1
  b = 10
  g = Prime()
  print("From range",a,"to",b, "the prime numbers are",g(a,b))
```
Palindrome Class
```
class Palindrome:
  def __init__(self):
    self.palindrome = []
    
  def __call__(self,string):
    #Setting a different variable so I can print the original string later on
    actual = string

    #If there are no alphanumeric characters(A-Z) in the string, it removes them for all characters in the string that are alphanumeric
    if actual.isalpha() == False: 
      #Using join builtin method with no space in between to join all characters that are iterated throughout to see if it fills condition that isalpha is True
      actual = ''.join(g for g in actual if g.isalpha())
    #replaces all spaces with empty
    actual.replace(" ","")      
    #python builtin lowercase function
    actual = actual.lower()
    #Has the string spliced starting from the end and moving to index 0 with a step of -1 and sets this to the variable self.palindrome
    self.palindrome = actual[::-1]
    #if statement to see if the reverse is equal to string
    if self.palindrome == actual:
      return("The statement " + string + "(" + actual + ") is a palindrome")
    else:
      return("The statement " + string + " is not a palindrome, " + string + " is not the same as " + self.palindrome)
 ```
