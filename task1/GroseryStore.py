import os
import operator

class GroseryStore:
    def __init__(self):
        self.JSFileList = []
        self.CommonDictionary = {}
        self.WORKDIRR = os.getcwd()

    def static_vars(**kwargs):
        def decorate(func):
            for k in kwargs:
                setattr(func, k, kwargs[k])
            return func
        return decorate

    def SortGoods(self, dictionary, arg):
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
                raise NameError(self.SortGoods.__name__,"Wrong argument", arg,)
            except NameError:
                
                print("*** ERROR ***", self.SortGoods.__name__, "*** ERROR ***")
                raise
        return SortedDictionary

    def HighestValues(self, dictionary):
        KeyList = list(dictionary["Goods"].keys())
        if dictionary["Goods"][KeyList[0]]["Price"] > dictionary["Goods"][KeyList[-1]]["Price"]:
            for n in range(3):
                print(KeyList[n])
        else:
            for n in range(1,4):
                print(KeyList[-n])

    def GetGoodsDataList(self):
        for file in os.listdir(self.WORKDIRR):
            if file.endswith(".json"):
                self.JSFileList.append(file)

    def OpenJSON(file):
        try:
            f = open(file)
        except IOError:
            print("File",file,"does't exist")
        else:
            data = json.load(f)
            f.close()
        return data

    @static_vars(firstrun = True)
    def MergeData(self):
        for FileName in self.JSFileList:
            dictionary = self.open_task_json.OpenJSON(FileName)
            if firstrun:
                self.CommonDictionary.update(dictionary)
            else:
                self.CommonDictionary["Goods"] |= dictionary["Goods"]
