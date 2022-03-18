Creating the InfoDb and creating functions that print out the info and the tester to be put into the menu -
```InfoDb = []
# List with dictionary records placed in a list  
InfoDb.append({  
               "FirstName": "Everitt",  
               "LastName": "Cheng",  
               "School ID": 1912363,  
               "School": "Del Norte",  
               "School Email": "everittc12363@stu.powayusd.com",  
               "Classes":["AP CSP","APUSH","AP English Language","AP Calculus AB", "Off Roll"]  
              })  
InfoDb.append({  
               "FirstName": "Jimmmy",  
               "LastName": "Fallon",  
               "School ID": 1809421,  
               "School": "Westview",  
               "School Email": "jimmyf09421@stu.powayusd.com",  
               "Classes":["AP CSP","Ethnic Studies","AP HUG","Off Roll", "Double Off Roll"]  
              })  
InfoDb.append({  
               "FirstName": "Joseph",  
               "LastName": "Biden",  
               "School ID": 2012363,  
               "School": "Mt. Carmel",  
               "School Email": "josephb12363@stu.powayusd.com",  
               "Classes":["AP CSP","Expos Lit","Child Development","Work Experience", "Marketing Economics 2"]  
              }) 
InfoDb.append({  
               "FirstName": "Gerald",  
               "LastName": "Ford",  
               "School ID": 1800000,  
               "School": "Abraxas",  
               "School Email": "geraldf00000@stu.powayusd.com",  
               "Classes":["AP CSP","World Lit","AP Psych","Off Roll", "Double Off Roll"]  
              })  

def print_info(n):
  print(InfoDb[n]["FirstName"], InfoDb[n]["LastName"])
  print("\t" + "ID: " + str(InfoDb[n]["School ID"]))
  print("\t" + "School Name: " + InfoDb[n]["School"])
  print("\t" + "School Email: " + InfoDb[n]["School Email"])
  print("Classes: ")
  #Loop to print all classes
  for i in (InfoDb[n]["Classes"]):
    print("\t" + i)

def infoTester():
  n = (input("List the index of the student you want: " ))
  print_info(int(n))
 ```
 Different loops(For,While, and Recursive) all printing out all the data of InfoDb - 
 ```
 def forLoop():
  print("For Loop: ")
  for i in range(len(InfoDb)):
    print_info(i)

def whileLoop():
  print("While Loop: ")
  g = 0
  while g < len(InfoDb):
    print_info(g)
    g += 1
    
def recursiveLoop(n):
  if n < len(InfoDb):
      print_info(n)
      recursiveLoop(n + 1)
  return 
  
def recursiveRun():
  print("Recursive Loop: ")
  recursiveLoop(0)
 ```
 Fibonacci Code and Tester/Outputter - 
 ```
 
def fibonacci(n):
    if n == 1 or n == 0:
        return 1
    return (fibonacci(n-1) + fibonacci(n-2))

def fibonacciTester():
    n = int(input("Enter a number: "))
    try:
      print("Sequence of: ", n , " numbers is" )
      for i in range(0,n):
        print( "=" * 5, "\n", fibonacci(i))
    except:
      print("Invalid integer(Check if value is negative)")
```
 
