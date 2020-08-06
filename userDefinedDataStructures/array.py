#Array is like list but store data of one data type.

import array as arr
a = arr.array('i', [1, 2, 3])#i shows data type Integer

#Operations performed in an array
while(True):
    print('1. Print elements of array')
    print('2. Add element to array')
    print('3. Delete element from array')
    print('4. Exit')
    choic=input("Enter your choice: ")
    choice=int(choic)
    if(choice==1):
        print('Array elements are:')
        for number in a:
            print(number)
    elif(choice==2):
        val = int(input('Enter integer number:'))
        a.append(val);
    elif(choice==3):
        value = a.pop()
        print('Value deleted:', value)
    elif(choice==4):
        break
    else:
        print("Enter valid choice.")

