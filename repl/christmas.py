def christmastree():
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
