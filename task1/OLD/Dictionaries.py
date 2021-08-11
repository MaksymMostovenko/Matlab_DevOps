# Merge several dictionaries into one, named as CommonDictionaryionary. 
# Software should be able to open files in bulk. Software should be able 
# to sort dictionaries "A-Z" and "Z-A". Software should print KEYS that 
# points to three highest values.

import open_task_json
import os
import operator

def SortDicionary(dictionary, arg):
    SortedDictionary = {"Goods":{}}
    SortedKeys = sorted(dictionary["Goods"], key=lambda x: (dictionary["Goods"][x]["Price"]))
    
    if arg == "Ascending":
        for K in SortedKeys:
            SortedDictionary["Goods"].update({K:dictionary["Goods"][K]})
    elif arg == "Descending":
        for K in reversed(SortedKeys):
            SortedDictionary["Goods"].update({K:dictionary["Goods"][K]})
    else:
        try:
            raise NameError(SortDicionary.__name__,"Wrong argument", arg,)
        except NameError:
            
            print("*** ERROR ***", SortDicionary.__name__, "*** ERROR ***")
            raise
    
    return SortedDictionary

def HighestValues(dictionary):
    KeyList = list(dictionary["Goods"].keys())
    if dictionary["Goods"][KeyList[0]]["Price"] > dictionary["Goods"][KeyList[-1]]["Price"]:
        for n in range(3):
            print(KeyList[n])
    else:
        for n in range(1,4):
            print(KeyList[-n])

WORKDIRR = os.getcwd()
# Configs

#Containers
JSFileList = []
CommonDictionary = {}

for file in os.listdir(WORKDIRR):
    if file.endswith(".json"):
        JSFileList.append(file)

for FileName in JSFileList:
    dictionary = open_task_json.OpenJSON(FileName)
    if not bool(CommonDictionary):
        CommonDictionary.update(dictionary)
    else:
        CommonDictionary["Goods"] |= dictionary["Goods"]

# Sort dictionary
CommonDictionary = SortDicionary(CommonDictionary, "Ascending")
HighestValues(CommonDictionary)