#okuma
try:
    with open('test.txt') as file:
        print(file.read())
except FileNotFoundError as e:
    print(e)

#yazma
with open('test2.txt','w') as file:
    file.write('this is a text')

#ekleme
with open('test2.txt','a') as file:
    file.write('\nappend')

#copy a file

import shutil
#shutil.copyfile('test2.txt','copy.txt')
#shutil.copy('test2.txt','/Users/doganaybalaban/Desktop/copy.txt')

#move a file
import os
src = "move.txt"
dest = "/Users/doganaybalaban/Desktop/move.txt"

try:
    if os.path.exists(dest):
        print("There is already a file here")
    else:
        os.replace(src,dest)
        print(src + " was moved")
except FileNotFoundError as e:
    print(e)