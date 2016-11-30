#Recursive Function to check if 'n' is a prime number
def isPrime(n):
   def NumChecker(n, j):
      if j == 1: #Presume 1 is a prime number even though it is not
         return True
      else:
          return n % j != 0 and NumChecker(n, j - 1) #Base Case that breaks the recursion
   return NumChecker(n, n -1)
