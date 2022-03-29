# Fibonacci function
def fibonacci(n):
    if n == 1 or n == 0:
        return 1
    return (fibonacci(n-1) + fibonacci(n-2))

#Tester
def fibonacciTester():
    n = int(input("Enter a number: "))
    try:
      print("Sequence of: ", n , " numbers is" )
      #For loop to print all the fibonacci values 0-n
      for i in range(0,n):
        print( "=" * 5, "\n", fibonacci(i))
    except:
      print("Invalid integer(Check if value is negative)")
      