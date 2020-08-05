#List(it's mutable)
myList=[1,2,3,"meera"]
myList.append(5)#To add value to end of list.
print(myList)
myList.append((5,0000))#To add value to end of list. #Tuple is added.
print(myList)
myList.extend((5,0000))#To add value to end of list #Value added and not the tuple.
print(myList)
myList.insert(0,"mother")#To add value to list by giving the index(index 0 is given here)
print(myList)

element=myList.pop()#To remove value at end of list.
print(element)
print(myList)

myList7=[1,2,3,99,6]
myList7.sort()
print(myList7)
myList7=[1,2,3,99,6]
print("max: ",max(myList7))
print("min: ",min(myList7))
print("len: ",len(myList7))

print("new list",[1,2]+[55,67])#Concatenation
print("new..new list",[1,2]*3)

myList.remove(1)#To remove any particular element from  list.
print(myList)

for ele in [11,2,3,3]:
 print(ele)

#Tuple(not mutable)
num=(1,2,3,4,5,6,7,8,"manu")
print(num)
print(num[0])
print(num[8])

num7=(1,2,3,4,5,6,7,8)
print("max: ",max(num7))
print("min: ",min(num7))
print("len: ",len(num7))

for elem in (11,2,3,3):
 print(elem)

print((1,2,3)+(4,5,6))#Concatenation

#Dictionary
#Set
