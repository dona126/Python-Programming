
#FILE HANDLING
file=open("hello.txt","r")#opens a file, mode also given #“ r “, for reading.
                                                         #“ w “, for writing.
                                                         #“ a “, for appending.
                                                         #“ r+ “, for both reading and writing
                                                         
for each in file:
    #Prints each line in the file one by one
    print(each)
file.close()


#READ MODE
print("Example 1")
file=open("hello.txt","r")
data=file.read()#Reads the whole file as a single string.
print(data)
file.close()

print("Example 2")
file=open("hello.txt","r")
data=file.read(5)#Read the first five characters of stored data in file.
print(data)
file.close()


#WRITE MODE
#Python code to create a file
file = open('gk.txt','w')
file.write("I am write command \n")
file.write("I allows you to write.")
file.close()
file = open('gk.txt','r')
data=file.read()
print(data)
file.close()


#APPEND MODE
file = open('gk.txt','a')
file.write(" This will add this line")
file.close()
file = open('gk.txt','r')
data=file.read()
print(data)
file.close()

#split() in file handling
file = open('gk.txt','r')
data=file.read()
for each in data:
        word = each.split()
        print(word)
file.close()
