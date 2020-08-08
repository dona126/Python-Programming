#LIST(it's mutable)
myList=[1,2,3,"meera"]
myList.append(5)#To add value to end of list.
print(myList)
myList.append((5,0000))#To add value to end of list. #Tuple is added.
print(myList)
myList.extend((5,0000))#To add value to end of list #Value added and not the tuple.
print(myList)
myList.insert(0,"mother")#To add value to list by giving the index(index 0 is given here)
print(myList)

element=myList.pop(3)#To remove value at the index specified of the list.
print(element)
print(myList)

myList.remove(1)#To remove any particular element from  list.
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

for ele in [11,2,3,3]:
 print(ele)

 
 
#TUPLE(not mutable)
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



#DICTIONARY
#Dictionary holds key:value pair.
#Values in a dictionary can be of any datatype,but keys can’t be repeated and must be immutable.

# Creating a Dictionary with Integer Keys
Dict = {1: 'Priya', 2: 'Frenny', 3: 'Geena'}
print("\nDictionary using Integer Keys: ")
print(Dict)

# Creating a Dictionary with Mixed keys
Dict = {'Name': 'Priya', 1: [1, 2]}
print("\nDictionary using  Mixed Keys: ")
print(Dict)

# Creating an empty Dictionary
Dict = {}
print("\nEmpty Dictionary: ")
print(Dict)

# Creating a Nested Dictionary
Dict = {1: 'Good', 2: 'Night',
		3:{'A' : 'Welcome', 'B' : 'To', 'C' : 'the Show!'}}
print(Dict)

# Adding elements to a Dictionary
Dict = {}
Dict[0] = 'Python'
Dict[2] = 'Program'
Dict[3] = 1
Dict['Numbers'] = 2, 3, 4
Dict[5] = {'Nested' :{'1' : 'one', '2' : 'two'}}
print("\nDictionary after adding  elements: ")
print(Dict)

# Updating existing Key's Value
Dict[2] = 'Code'
print("\nDict after updation: ")
print(Dict)

# Accessing a element from a Dictionary
Dict = {1: 'Who', 'name': 'are', 3: 'you?'}
print("Accessing a element using key:")
print(Dict['name'])

Dict = {'Dict1': {1: 2}, 'Dict2': {3: 4}}
print(Dict['Dict1'])
print(Dict['Dict1'][1])
print(Dict['Dict2'][3])

#Program to count the number of times each name is found in list.
#Display the count and name in the form of a dictionary
print("")
print("")
names=["anna","susan","selin","anna","susan","selin","annas"'megha',"jenny"]
dict={}
for x in names:
    if x not in dict:
        dict[x]=1
    else:
        dict[x]=dict[x]+1
print(dict)
print(dict.keys())#returns a list of all keys
print(dict.values())#returns a list of all values
print(dict.items())#returns a list of tuples containing both keys and valuues

#Sorting Dictionary w.r.t value_set.
print(" ")
sortedList=[]
for k,v in dict.items():
    sortedList.append((v,k))
print("After appending in reverse order (ie, value then key order):",sortedList)
sortedList=sorted(sortedList, reverse=True)
print("After sorting w.r.t tO value",sortedList)


#SET
set1 = {1, 2, 3, 4, 4, 4}
print(set1)

set1.add(5)#for adding elements
print(set1)

#Operations possible: union(), intersection(), difference(), symmetric difference()
set2 = {3, 4, 5, 6}
print(set1.union(set2))
print(set1.intersection(set2))
print(set1.difference(set2))
print(set1.symmetric_difference(set2))

