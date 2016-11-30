#Function to calculate the number of trailing zeroes in a factorial number
def findZeros(n):
    numOfFives = 0
    for i in range(2, n+1):
        while i > 0:
            if i % 5 == 0:  #Check for remainder when divided by 5
                numOfFives += 1 
                i = i/5    
            else:
                break
    print (numOfFives) 

findZeros(10) #Change parameter n to test a different number          
    
    








