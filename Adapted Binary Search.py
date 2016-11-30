#Adapted Binary Search Algorith to search for a value at a specific interval
def isBetween (seq, target):
    lowInput = input("Please Enter a low input: ")
    highInput = input("Please Enter a high input: ")
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
        elif target > int(lowInput) and target < int(highInput): #If target is inbetween low and high inputs print true
            print ("True")
            break
        else: 
            print ("False")
            break


#Unsorted array to test the function
testList = [2,3,5,7,9,13]
print (isBetween(testList, 13))
