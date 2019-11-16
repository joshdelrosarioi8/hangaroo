import string

def isWordGuessed(secretWord, wordguessed):
    for x in wordguessed:
        if wordguessed==secretWord:
            guesss = True
            break       
        elif x in secretWord:
            guesss = True
            print('Correct! ',wordguessed,'is in the mystery word!')
        else:
            print("Wrong!")
            guesss = False
                    
    return guesss

def getGuessedWord(secretWord, lettersGuessed):
    guessedlist = list(lettersGuessed)
    getguessedWord = ''
    
    for indx in secretWord:
        if lettersGuessed==secretWord:
            getguessedWord = lettersGuessed
            break
        elif indx in guessedlist:
            getguessedWord = getguessedWord + indx
        else:getguessedWord = getguessedWord + '_'
    
    return getguessedWord


def getAvailableletters(lettersGuessed):
    l = list(string.ascii_lowercase)
    availableletters = ''
    
    for indx3 in l:
        if indx3 not in lettersGuessed:availableletters+=indx3
    
    return availableletters

def Hangaroo(secretWord):

    tries = 5
    lettersGuessed = []
    availletters = string.ascii_lowercase
    guessedWord = ''
    
    print("Let's play Hangaroo!")
    while tries>0:

        casesensitive_guessed = input("Enter a letter(press 0 to quit) ") 
        guessed = casesensitive_guessed.lower()
        
        if guessed =='0':break
        
        if guessed in lettersGuessed:
            print('You have already entered that')
            print(guessedWord)
            continue
        
        lettersGuessed.append(guessed)
        
        availableletters = getAvailableletters(lettersGuessed)

        rightletter = isWordGuessed(secretWord,guessed)            
        if rightletter == False: 
            tries -= 1
            if tries ==0: 
                print("Oh no! You did not guess the word. The correct answer is ",secretWord)
                break
            print("You only have",tries," tries left.")
            
        guessedWord = getGuessedWord(secretWord,lettersGuessed)
        print(guessedWord) 


        if guessedWord == secretWord:
            print("Correct! You've guesses the right word!!") 
            break
    
    return
            
        
    
                    
                
                    
                
            

