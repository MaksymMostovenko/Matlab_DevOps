import os
import json

class GroseryStore:
    def __init__(self):
        self.JSFileList = []
        self.CommonDictionary = {}
        self.SortedDictionary = {}
        self.WORKDIRR = os.getcwd()
        self.SORTKWORDS = ["ascending", " descending"]

    def SortGoods(self, arg):
        if len(arg) == 0:
            try:
                raise NameError(self.SortGoods.__name__,"There is no arguments")
            except NameError:
                print("*** ERROR ***", self.SortGoods.__name__, "*** ERROR ***")
                raise
        elif arg not in self.SORTKWORDS:
            try:
                raise NameError(self.SortGoods.__name__,"Wrong argument", arg,)
            except NameError:
                print("*** ERROR ***", self.SortGoods.__name__, "*** ERROR ***")
                raise

        SortedGoods = {}
        for ProductType in self.CommonDictionary:
            SortedGoods[ProductType] = {}
            SortedKeys = sorted(self.CommonDictionary[ProductType],
                                key=lambda x: (self.CommonDictionary[ProductType][x]["Price"]),
                                reverse=(arg=='descending'))
            for  Goods in SortedKeys:
                SortedGoods[ProductType][Goods] = self.CommonDictionary[ProductType][Goods]
        self.SortedDictionary = SortedGoods

    def HighestValues(self, product_type):
        goods_keys_list = list(self.SortedDictionary[product_type].keys())
        goods_vals_list = list(self.SortedDictionary[product_type].values())

        if product_type not in list(self.SortedDictionary.keys()):
            try:
                raise NameError(self.HighestValues.__name__,"There is no any product type:",
                                product_type)
            except NameError:
                print("*** ERROR ***", self.HighestValues.__name__, "*** ERROR ***")
                raise

        if goods_vals_list[0]["Price"] < goods_vals_list[-1]["Price"]:
            for i in range(1,4):
                print(goods_keys_list[-i], goods_vals_list[-i])
        else:
            for i in range(1,4):
                print(goods_keys_list[i], goods_vals_list[i])

    def GetGoodsDataList(self):
        for file in os.listdir(self.WORKDIRR):
            if file.endswith(".json"):
                self.JSFileList.append(file)

    def OpenJSON(self,file):
        try:
            f = open(file)
        except IOError:
            print("File",file,"does't exist")
        else:
            data = json.load(f)
            f.close()
            print(".json", file, "opened successfuly",'\n')
        return data

    def MergeData(self):
        self.GetGoodsDataList()
        for FileName in self.JSFileList:
            dictionary = self.OpenJSON(FileName)
            if not self.CommonDictionary:
                self.CommonDictionary.update(dictionary)
            else:
                for key in dictionary.keys():
                    if key in self.CommonDictionary:
                        self.CommonDictionary[key] |= dictionary[key]
                    else:
                        self.CommonDictionary[key] = dictionary[key]

