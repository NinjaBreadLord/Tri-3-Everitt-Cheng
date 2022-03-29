import time

# terminal print commands
ANSI_CLEAR_SCREEN = u"\u001B[2J"
ANSI_HOME_CURSOR = u"\u001B[0;0H\u001B[2"
OCEAN_COLOR = u"\u001B[44m\u001B[2D"
RESET_COLOR = u"\u001B[0m\u001B[2D"

CAKE_COLOR = u"\u001B[36m\u001B[2D"

def cake_print(position):
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
    distance = 60  # Number of loops
    step = 1  # Step amount

    for position in range(start, distance, step):
        cake_print(position)  
        time.sleep(.1)
