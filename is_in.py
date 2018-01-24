def isIn(char, aStr):
    
    '''
    char: a single character
    aStr: an alphabetized string
    
    returns: True if char is in aStr; False otherwise
    '''
    # Your code here
    if len(aStr)>1:
        if char == aStr[round(len(aStr)/2)]:
            return True
        elif ord(char) < ord( aStr[round(len(aStr)/2)] ):
            return isIn(char, aStr[0:round(len(aStr)/2)])
        else:
            return isIn(char, aStr[round(len(aStr)/2):])        
    else:
        if char == aStr[0]:
            return True
        else:
            return False
print(isIn('f',  'abcdfhigklmn'))
