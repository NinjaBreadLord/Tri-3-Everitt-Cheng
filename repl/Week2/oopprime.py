class Prime:
  def __init__(self):
    self.prime = []
  def __call__(self, a, b):
    for i in range(a, b + 1):
        count = 0
        for g in range(2, (i // 2 + 1)):
          if (i % g == 0):
            count = count + 1
            break
        if (count == 0 and i != 1):
          self.prime.append(" %d" % i)
    return ' '.join(self.prime)

def primeOOPTester():
  a = 1
  b = 10
  g = Prime()
  print("From range",a,"to",b, "the prime numbers are",g(a,b))