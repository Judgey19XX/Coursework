#Adapted Binary Search Algorith to search for a value at a specific interval
def binarySearch(seq, target):
    lowerBound = 0
    upperBound = len(seq) - 1
    while True:
        if upperBound < lowerBound:
            return - 1
        midPoint = (lowerBound + upperBound) // 2
        if seq[midPoint] < target: #If the mid point is less than the target move up the seuquence
             lowerBound = midPoint + 1 
        elif seq[midPoint] > target: #If the mid point is greater than the target move down the squence
             upperBound = midPoint - 1 
        else:
             return midPoint

#Unsorted array to test the function
testList = [0,1,8,9,48,91,64,73,88,100]
print("Your number is at posistion: ", binarySearch(testList, 8))  
