{% include navbar.html %}



# College Board 

## [Quiz 1 Corrections](https://ninjabreadlord.github.io/Tri-3-Everitt-Cheng/tests/quiz1)
## [Quiz 2 Corrections](https://ninjabreadlord.github.io/Tri-3-Everitt-Cheng/tests/quiz2)


## Create Task Writeup

3ai. The overall purpose of this program is to work as a guessing game for the user, which inputs a value and guesses until he gets the number in the defined range. 

3aii. The user enters the function with input parameters, inputs a low value and then a high value. Then they guess the random value until they get it with hints on whether the guessed value is too high or too low. THen after guessing correctly the game shows his guesses and then asks if wants to replay with the same predefined amount.

3aiii. Input a value for the parameters of function guessGame(), which these variables are user input. After inputting the function outputs your range and asks you to guess. It will keep giving hints on whether the guessed value is too high or too low, after guessing it outputs the guesses of the user and if they want to play again, in which the user can input y/n. 

3bi. Empty list created with the data inside being appended later on in the code.

```
guesses = []
```

3bii. Appends the incorrect guesses by user to the list every time the user gets it wrong. 

```
  while guess != answer:
        if(guess > answer and guess <= b):
          print("Too high")
          guesses.append(guess)
          guess = int(input("Guess a number in range " + str(a) + "," + str(b) + ": "))
          count += 1
        elif(guess < answer and guess >= a):
          print("Too Low")
          guesses.append(guess)
          guess = int(input("Guess a number in range " + str(a) + "," + str(b) + ": "))
          count += 1
```

3biii. List name is guesses, the list type is an array.

3biv. An array with all the previous guesses of the user. At the end of the game it will display what your previous number guesses were. 

3bv. This array contains the numerical values of previous guesses of the user. It would be written differently by instead of having a list, you could just having a string value with the guesses being appended into the string rather than a list, however this would be a bit worse and less organized. 

3ci. guessGame procedure with parameter/input, this is a majority of the code

```
def guessGame(a,b):
    guesses = []
    on = True
    while on == True:
      #While loop so the game continuously runs unless the user says so
      answer = random.randint(a, b)
      count = 1
      guess = int(input("Guess a number in range " + str(a) + "," + str(b) + ": "))
      while guess != answer:
        #While the user is guessing wrong, the loop will continue with input
        if(guess > answer and guess <= b):
          #If guess is in the defined range and above the answer it will give the user a hint
          print("Too high")
          guesses.append(guess)
          guess = int(input("Guess a number in range " + str(a) + "," + str(b) + ": "))
          count += 1
        elif(guess < answer and guess >= a):
          #If guess is in range and too low it will give the user a hint
          print("Too Low")
          guesses.append(guess)
          guess = int(input("Guess a number in range " + str(a) + "," + str(b) + ": "))
          count += 1

        else:
          #if it is outside the range of a or b then it will tell the suer
          print("Number outside predefined range")
          guess = int(input("Guess a number in range " + str(a) + "," + str(b) + ": "))      
      print("Nice, that is the answer")
      print("Number of Guesses: ", count)
      print("Previous Guesses: ", *guesses)
      cont = input("Continue with this range('yes' to continue 'no' to define a new range that is not (1,100)?: ")
      guesses = []
      if (cont == "No" or cont == "no" or cont == "n"):
          on = False
          a = int(input("Choose lowest number for range: "))
          b = int(input("Highest number: "))
          guessGame(a,b)
```

3cii. Function called within main, already with parameters set from (0,100). The procedure will call itself after the end of the first game after a conditional statement asking the user if they want to change the base numbers. 
     

```
guessGame(1,100)
```

3ciii. The procedure is the majority of the code for the create task, without calling it I wouldn't have the game, and only random values not used.

3civ. First a while loop is created that keeps on running the game, unless a certain boolean 'on' is set to False after the game is finish. After the while loop is created for the game, the answer is set to a random value using the random.randint python method, and asks the user to guess. Another while loop is created for when the user is wrong, and will give hints using if statements depending if the guessed answer is higher or lower than the actual answer. After the answer is guessed correctly, the while loop ends and the code displays the guesses and amount of guesses, as well as asking whether the user wants to continue or not. Depending on the answer, the boolean 'on' will be set to True or False. 

3di.
Called with first parameters 
```
guessGame(1,100)
```
Second call is set with user input within the function, depending if the user wants to change the parameters of the guessGame()
```
if (cont == "No" or cont == "no" or cont == "n"):
     on = False
     a = int(input("Choose lowest number for range: "))
     b = int(input("Highest number: "))
     guessGame(a,b)
```

3dii. 
The first call has no condition, but the second call is only there if the user wants to changed the predetermined values of the first call.

3diii.

First call runs the game with range (1,100), the user has the option to continue the game after with the same parameters. For the second call it runs the game on the user input parameters, and can theoretically be called an infinite amount of times until the code is stopped. 


## Create Task
Idea: Create a list of numbers incrementing by 1 with the length based on user input. Randomly choose a number in this list and have the user guess until he gets the number. If the user guesses higher it prints that it is too high, and if it is too low it prints it is too low. Eventually the user should reach the number and then it should out put number of guesses afterwards. 

## Runtime
<iframe frameborder="0" width="100%" height="500px" src="https://replit.com/@EverittC/Create-Task?embed=True"></iframe>
