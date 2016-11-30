#Function to randomise a list of integers
import random

orginalList = [5,3,8,6,1,9,2,7]

def pickFromHat():
    arrayLength = len(orginalList)
    arrayCounter = arrayLength-1  #To move the index down the list
    for i in range(arrayCounter, 0,-1):
        randomInt = random.randint(0,i) #Pick a random Integer from the list to shuffle
        if randomInt == i: #Stops when all numbers have been shuffled
            continue
        orginalList[i],orginalList[randomInt]=orginalList[randomInt],orginalList[i]
        print (orginalList)

pickFromHat()
#Fisher Yates Algorithm
#-- To shuffle an array a of n elements (indices 0..n-1):
#for i from n−1 downto 1 do
     #j ← random integer such that 0 ≤ j ≤ i
     #exchange a[j] and a[i]

