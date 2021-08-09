# Вывести чётные числа из заданного СПИСКА и останавливается, если встречаешь число 237.
import open_task_json

def IsEven(n):
    mod = n%2
    if mod == 0:
        return True
    else:
        return False

Dictionary = dict(open_task_json.OpenJSON('Task.json'))
STOP_NUM = 237

for key in Dictionary:
    if IsEven(Dictionary[key]):
        print(Dictionary[key])
    elif Dictionary[key] == STOP_NUM:
        break
    else:
        continue 

