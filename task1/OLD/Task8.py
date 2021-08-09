# С помощью анонимной функции извлечь из списка числа, делимые на 15.

import open_task_json

Dictionary = dict(open_task_json.OpenJSON('Task.json'))

ValueList = []
mod = lambda a: a%5

for key in Dictionary:
    ValueList.append(Dictionary[key])

for val in ValueList:
    if mod(val) == 0:
        print(val)
