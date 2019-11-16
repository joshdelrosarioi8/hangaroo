def getGuessedWord(secretWord2, lettersGuessed2):
    guessedword = ''
    for indx in secretWord2:
        if indx in lettersGuessed2:
            guessedword =+ indx
        else: guessedword = guessedword + '_'
    
    return guessedword 