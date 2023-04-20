# function.py
# define sentence_analyzer
# it should take in a line of text and output a dictionary 
# key will be each letter 
# value will be frequency of letter

def sentence_analyzer(text):
    myLetters = dict()  # empty dictionary
    # i need to iterate over the string 
    for letter in text :
        #print(letter) testing
        # check if letter is already in the dictionary
        # if it is increment the value otherwise add it to the dictionary and set value to 1
        if letter in myLetters:
            myLetters[letter] = myLetters[letter] + 1   # this performs a lookup and adds an value to count
        else:
            myLetters[letter] = 1
    return myLetters
