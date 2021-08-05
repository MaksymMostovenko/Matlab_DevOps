# Task 2
# Нахождение трёх ключей с самыми высокими значениями в словаре

import  open_task_json
import operator

Dictionary = dict(open_task_json.OpenJSON('Task.json'))
Sorted_down_up = dict(sorted(Dictionary.items(), key=operator.itemgetter(1), reverse=True))

print(list(Sorted_down_up.items())[:3])

