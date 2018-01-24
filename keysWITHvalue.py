aDict = {1:5, 2:6}
def keysWithValue(aDict, target):
    dic = []
    found = False
    for key in aDict:
        if aDict[key] == target:
            found = True
            dic.append(key)
    if found:
        return dic
    else:
        return []

print(keysWithValue({0: 3, 1: 2, 2: 4, 4: 0, 5: 2, 7: 3, 8: 1, 10: 2}, 2))
            
