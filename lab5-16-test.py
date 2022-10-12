
import os

if not os.path.exists('students.txt'):
    print('False')

with open('students.txt') as fileobj:
    lines = fileobj.readlines()
    numoflines = len(lines)
    if numoflines != 6:
        print('False')


lastline = lines[numoflines-1].split()
if lastline[0] != 'Kurt' or lastline[1] != '90' or lastline[2] != '100':
    print('False')

print('True')

# with open('students.txt') as fileobj:
#     for r in fileobj:
#         print(r)


# with open('students.txt') as fileobj:
#     while True:
#         r = fileobj.readline()
#         if not r:
#             break
#         print(r.strip('\n'))
