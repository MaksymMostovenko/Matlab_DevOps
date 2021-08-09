# Merge several dictionaries into one, named as CommonDictionary. Software
# should be able to open files  in bulk. Software # should be able to sort 
# dictionaries "A-Z" and "Z-A". Software should # print KEY that points to 
# three highest values.

import open_task_json
import os

WORKDIRR = os.getcwd()
JSFileList = []
Commondict = {}

for file in os.listdir(WORKDIRR):
    if file.endswith(".json"):
        JSFileList.append(file)

for FileName in JSFileList:
    dictionary = dict(open_task_json.OpenJSON(FileName))
    if not bool(Commondict):
        Commondict.update(dictionary)
    else:
        Commondict["Goods"] |= dictionary["Goods"]

# get data fom goods item
for goods, g_info, in Commondict.items():
    for key in g_info:
        print(g_info[key]["Price"])
