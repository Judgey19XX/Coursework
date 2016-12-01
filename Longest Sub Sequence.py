def findLongestSeq(seq):
    longestSeq = []
    currentSeq = []

    for i in range (len(seq)):
        #Seq continues as long as previous ints are smaller than next ints
        if i < len(seq) -1 and seq[i] <= seq[i+1]:
            currentSeq.append(seq[i]) 
        #Else save the seq to current seq variable
        else:
            currentSeq.append(seq[i])
            #If the currentSeq is greater than the longestSeq
            if len(currentSeq) > len(longestSeq):
                longestSeq = currentSeq #current is now the longest

            currentSeq = [] #clear the currentSeq for garbage collection 

            print('The longest sequence is:', longestSeq)

findLongestSeq([1,2,3,4,1,5,1,6,7])







        
         
