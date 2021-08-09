# Преобразования полученных от пользователя последовательность чисел, разделенных запятой в список и кортеж с этими числами.

string = ''
li = []
string = input()
for i in string:
    if i==',':
        continue
    else:
        li.append(i)
print(li)
print(tuple(li))