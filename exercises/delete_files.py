import os
import shutil

file = open(os.getcwd()+'/duplicate.txt', 'r')

for line in file:
    a = line.strip('\n')

    if os.path.exists(a):
        shutil.move(a, 'C:/Users/Priya/Desktop/duptest/delete/')
#        os.remove(a)
    else:
        print('File ' + a + ' does not exist')
