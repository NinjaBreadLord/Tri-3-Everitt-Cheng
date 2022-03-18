Creating the InfoDb and creating functions that print out the info and the tester to be put into the menu
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
  print_info(int(n))```
