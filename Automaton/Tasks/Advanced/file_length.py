import os

os.chdir('Filepath here')

myfile = open('fruits.txt')
content = myfile.read()
myfile.close()
content = content.splitlines()
for i in content:
    print(len(i))
    
file = open('fruits.txt')
c = file.readlines()
c = [line.strip() for line in c]
file.close()
for b in c:
    print(len())
