import ageswap
import matrix
import pattern
import christmas
import Info
import fibonacci


main_menu = [
    ["Swap", ageswap.swapTester],
    ["Matrix", matrix.matrixTester2],
    ["Pattern", pattern.cake],
    ["Tree", christmas.christmastester],
    ["Fibonacci", fibonacci.fibonacciTester],
    ["InfoDb(Just printing specific index)", Info.infoTester],
    #["Menu Two", ]
]


iteration_list = [
  ["For Loop to print all of InfoDb", Info.forLoop],
  ["While Loop to print all of InfoDb", Info.whileLoop ],
  ["Recursive Loop to print all of InfoDb", Info.recurisveRun]
]


border = "=" * 25
banner = f"\n{border}\nPlease Select An Option\n{border}"


def menu():
    title = "Function Menu" + banner
    menu_list = main_menu.copy()
    menu_list.append(["Iteration to print Info", iterationMenu],)
    buildMenu(title, menu_list)
  
def iterationMenu():
    title = "Iteration Menu" + banner
    buildMenu(title, iteration_list)
  
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