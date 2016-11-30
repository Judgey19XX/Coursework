#Recursive function to remove vowels from a given string
#Extended slice syntax [Start:Stop:Step]
def deleteVowels(userString):
    if len(userString) == 0:
        return userString #If the string is empty just return the empty string
    else:
        newString = userString[1: len(userString) + 1] #Create a new string by moving up the length of the old string & adding to the new string
        firstLetter = userString[0] #The first letter in the old string is at position 0 
        if firstLetter in "aeiouAEIOU": 
            return deleteVowels(newString) #If the first letter is a vowel delete it & call the function again
        else:
            return firstLetter + deleteVowels(newString) #Put the first letter back at the start of the string

#Input must be a string i.e. "beautiful" not beautiful
      
