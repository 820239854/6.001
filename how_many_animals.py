animals = { 'a': ['aardvark'], 'b': ['baboon'], 'c': ['coati']}

animals['d'] = ['donkey']
animals['d'].append('dog')
animals['d'].append('dingo')

def how_many(aDict):
    num = 0
    for k in aDict.values():
        num += len(k)
    return num

def biggest(aDict):
    max_len = 0
    len_k = 0
    for k in aDict:
        if len(aDict[k]) > max_len:
            max_len = len(aDict[k])
            len_k = k
    return len_k

print(biggest(animals))
