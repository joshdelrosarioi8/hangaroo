import string

def getAvailableletters(lettersGuessed3):
    l = list(string.ascii_lowercase)
    availableletters = ''
    
    for indx2 in l:
        if indx2 not in lettersGuessed3:  availableletters+=indx2
    
    return availableletters