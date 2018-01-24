aList = ["apple", "cat", "dog", "banana"]

def lessThan4(aList):
    less4 = []
    for i in aList:
        if len(i)<4:
            less4.append(i)

    return less4
print(lessThan4(aList))
