def calculateHandlen(hand):
    """ 
    Returns the length (number of letters) in the current hand.
    
    hand: dictionary (string int)
    returns: integer
    """
    # TO DO... <-- Remove this comment when you code this function
    count = 0
    for i in hand.keys():
        count +=1
    return count

print( calculateHandlen({'a': 1, 'c': 0, 'b': 1}) )
