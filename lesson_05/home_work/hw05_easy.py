# Задача-1:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.

import os

#Создание списка директорий
try:
    for el in range(9):
        dir_path = os.path.join(os.getcwd(),'dir_'+str(el+1))
        os.mkdir(dir_path)
except FileExistsError:
    print('Такая директория уже существует')

#Удаление списка директорий
try:
    for el in range(9):
        dir_path = os.path.join(os.getcwd(),'dir_'+str(el+1))
        os.rmdir(dir_path)
except FileExistsError:
    print('Такая директория не существует')

# Задача-2:
# Напишите скрипт, отображающий папки текущей директории.

dir_path = os.path.join(os.getcwd())
dir_list=os.listdir(dir_path)
for d in dir_list:
    dir_name=os.path.join(dir_path,d)
    if os.path.isdir(dir_name):
        print(d)


# Задача-3:
# Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.
import shutil
file_name=os.path.basename(__file__)
newfile=file_name+'.dupl'
shutil.copy(file_name,newfile)