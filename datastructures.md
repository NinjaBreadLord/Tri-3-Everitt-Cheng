{% include navbar.html %}



# Data Structures
## Project Idea
### [Link to Wireframe + Idea](https://ninjabreadlord.github.io/grup-grass/webProject) 
## Code Snippets


Menu - 
 ``` main_menu = [
    ["Swap", ageswap.swapTester],
    ["Matrix", matrix.matrixTester2],
    ["Pattern", pattern.cake],
    ["Tree", christmas.christmastester],
    ["InfoDb", Info.infoTester],
    #["Menu Two", ]
]
 ``` 

Ageswap Code with Tester - 
 ``` def ageSwap(age1,age2):
  # age1 = input("age 1 :")
  # age2 = input("age 2 :")
  if(age1 > age2):
    temp = age1
    age1 = age2
    age2 = temp
  return(age1,age2)
    
    
def swapTester():
  age1 = int(input("age 1 :"))
  age2 = int(input("age 2 :"))
  age1, age2 = ageSwap(age1, age2)
  print("age 1 = " + str(age1),"age 2 = " + str(age2))
  ```


Matrix Code and Tester - 
``` def matrix(list):
      for i in list:
         print(*i) 
    def matrixTester2():
     list = [[1,2,3],[4,5,6],[7,8,9],['*',0,'#']]
       print(matrix(list))    
 ```

Cake Pattern - 
```def cake_print(position):
    print(ANSI_HOME_CURSOR)
    print(CAKE_COLOR)
    ck = " " * position
    print(ck + "      )  (  )  (")
    print(ck + "     (^)(^)(^)(^)")
    print(ck + "     _i__i__i__i_")
    print(ck + "    (____________)")
    print(ck + "    |####|>o<|###|")
    print(ck + "    (____________)")
    print(RESET_COLOR)

  
def cake():

    # Animation Variables
    start = 0  # Start with no offset
    distance = 70  # Number of loops
    step = 1  # Step amount

    # Loop to move the computer to the right
    for position in range(start, distance, step):
        cake_print(position)  
        time.sleep(.1)
```


Christmas Tree and Tester - 
``` def christmastree():
  for i in range(6):
    for j in range(6-i):
      print(" ", end = " ")
    for k in range(2 * i + 1):
      print("*", end = " ")
    print()
  for i in range(2):
    print(" " * 11 + "***")
def christmastester():
  print(christmastree())
 ```


## Repl
{% include replinclude.html %}
