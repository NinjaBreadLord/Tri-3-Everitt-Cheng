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
      
def palindromeTester():
  print("=" * 5)
  palo = Palindrome()
  string = "hello"
  print("Word: " + string)
  print(palo(string))
  print("=" * 5)
  string2 = "taco cat"
  print(palo(string2))
  print("=" * 5)
  string3 = "A man, a plan, a canal -- Panama!"
  print("Statement: " + string3)
  print(palo(string3))
  
    
    
    
  
    