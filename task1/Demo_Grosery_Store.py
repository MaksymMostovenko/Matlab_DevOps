import GroseryStore

class Demo:
    def __init__(self,sort_type, goods_type):
        self._sort_type  = sort_type
        self._goods_type = goods_type

    def run_demo(self):
        print('\n','\t',"This demo for GROSERY_STORE sorter",'\n')
        new_store = GroseryStore.GroseryStore()
        print("Get data about goods from JSONS",'\n')
        new_store.MergeData()
        print("Sort goods by price",self._sort_type,'\n')
        new_store.SortGoods(self._sort_type)
        print("Print three most expencive goods from", self._goods_type, '\n')
        new_store.HighestValues(self._goods_type)

