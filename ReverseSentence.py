#Function to reverse sentences e.g. 'This is awesome' becomes 'awesome is This'
def reverseSentence():
    userInput = input("Enter your sentence to be reversed: ")
    y = userInput.split()
    result = [] #Buffer to store result
    for word in y:
        result.insert(0, word) #insert words at index 0 for all words
    return "".join(result)  #Join results into empty string


