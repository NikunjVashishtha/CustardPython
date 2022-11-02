# This function changes the key of the dictionay which is not allowed in python.
def alterKey(DictionaryName, OldKey, NewKey):
    mainDict = dict(DictionaryName)
    newDict = {}
    for dictKey in mainDict.keys():
        if mainDict[dictKey] == mainDict[OldKey]:
            newDict[NewKey] = mainDict[dictKey]
        else:
            newDict[dictKey] = mainDict[dictKey]
        print(dictKey)
    return newDict

# This function inserts an element before a certain element
def insertBefore(DictionaryName, PreviousKey, Key, Value):
    mainDict = dict(DictionaryName)
    newDict = {}
    for dictKey in mainDict.keys():
        if mainDict[dictKey] == mainDict[PreviousKey]:
            newDict[Key] = Value
        newDict[dictKey] = mainDict[dictKey]
    return newDict