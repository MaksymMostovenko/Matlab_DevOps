
import json
from os import path

def OpenJSON(file):
    try:
        f = open(file)
    except IOError:
        print("File",file,"does't exist")
    else:
        data = json.load(f)
        f.close()
        return data
   
