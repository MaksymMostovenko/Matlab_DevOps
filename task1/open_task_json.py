
import json

def OpenJSON(file):

    f = open(file)
    data = json.load(f)
    f.close()
    return data
   
