# Определение расширения файла по его полному пути.

# В идеале тут можно использовать перемнную среды (enviroment variable), но я не разобрался
# как это заставить взлететь на виндовс. В линуксе мне проще.
# Поэтому для демонстарции используем просто строку.
file_path = r'C:/Users/mostomak/Google Drive/Matlab_DevOps/Tasks.txt'

get_file_name = file_path.rsplit('/', 1)
get_file_type = get_file_name.pop().rsplit('.', 1)
get_file_type = get_file_type.pop()


if get_file_type == 'exe':
    print('Its executable file')
elif get_file_type == 'txt':
    print ('Its text file')
else:
    print ('Everything is a string if you brave enough')
