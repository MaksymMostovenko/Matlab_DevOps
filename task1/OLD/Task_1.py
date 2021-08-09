# Task 1
# Сортировка словаря с целыми числами по в порядке возрастания и убывания.
import open_task_json
import operator

Dictionary = dict(open_task_json.OpenJSON('Task.json'))

Sorted_up_down = sorted(Dictionary.items(), key=operator.itemgetter(1))
print(Sorted_up_down)
Sorted_down_up = sorted(Dictionary.items(), key=operator.itemgetter(1), reverse=True)
print(Sorted_down_up)