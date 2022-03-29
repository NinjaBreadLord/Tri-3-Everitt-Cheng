global age1
global age2
def ageSwap(age1,age2):
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
  
