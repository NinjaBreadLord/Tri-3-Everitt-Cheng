from Week0 import ageswap
from Week0 import matrix
from Week0 import pattern
from Week0 import christmas
from Week1 import Info
from Week1 import fibonacci
from Week2 import factorial
from Week2 import imperativeprime
from Week2 import oopprime
from Week2 import palindrome
from Week3 import quiz

main_menu = [

]
#week 0 submenu
week0_list = [
    ["Swap", ageswap.swapTester],
    ["Matrix", matrix.matrixTester2],
    ["Pattern", pattern.cake],
    ["Tree", christmas.christmastester]
]
#week 1 submenu
week1_list = [
    ["Fibonacci", fibonacci.fibonacciTester],
    ["InfoDb(Just printing specific index)", Info.infoTester]
]

#week 2 submenu
week2_list = [
    ["Factorial Class", factorial.factorialTester],
    ["Prime Function Imperative", imperativeprime.primeTester],
    ["Prime Function OOP", oopprime.primeOOPTester],
    ["Palindrome Extra Credit", palindrome.palindromeTester]
]

# Second menu for iteration
iteration_list = [
    ["For Loop to print all of InfoDb", Info.forLoop],
    ["While Loop to print all of InfoDb", Info.whileLoop ],
    ["Recursive Loop to print all of InfoDb", Info.recursiveRun]
]

#week 3 AKA cross over submenu
week3_list = [
    ["Quiz", quiz.starter],
]

border = "=" * 25
banner = f"\n{border}\nPlease Select An Option\n{border}"


def menu():
    title = "Function Menu" + banner
    menu_list = main_menu.copy()
    menu_list.append(["Week 0",week0Menu])
    menu_list.append(["Week 1",week1Menu])
    menu_list.append(["Week 2",week2Menu])
    menu_list.append(["Week 3",week3Menu])
    buildMenu(title, menu_list)

def iterationMenu():
    title = "Iteration Menu" + banner
    buildMenu(title, iteration_list)

def week0Menu():
    title = "Week 0 Menu" + banner
    buildMenu(title, week0_list)

def week1Menu():
    title = "Week 1 Menu" + banner
    week1_list.append(["Iteration to print Info", iterationMenu],)
    buildMenu(title, week1_list)

def week2Menu():
    title = "Week 2 Menu" + banner
    buildMenu(title, week2_list)

def week3Menu():
    title = "Week 2 Menu" + banner
    buildMenu(title, week3_list)

def buildMenu(banner, options):

    print(banner)

    prompts = {0: ["Exit", None]}
    for op in options:
        index = len(prompts)
        prompts[index] = op

    for key, value in prompts.items():
        print(key, '->', value[0])


    choice = input("Type your choice> ")


    try:
        choice = int(choice)
        if choice == 0:
            # stop
            return
        try:
            action = prompts.get(choice)[1]
            action()
        except TypeError:
            try:
                exec(open(action).read())
            except FileNotFoundError:
                print(f"File not found!: {action}")

    except ValueError:
        print(f"Not a number: {choice}")
    except UnboundLocalError:
        print(f"Invalid choice: {choice}")


    buildMenu(banner, options)


if __name__ == "__main__":
    menu()