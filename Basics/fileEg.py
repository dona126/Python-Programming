
#Code to count number of lines in a file.
file=open("hello.txt","r")
count=0
for each in file:
    count=count+1
print("Line count:",count)
file.close()


#Searching through a file using startswith().
print("\n")
file=open("hello.txt","r")
for each in file:
    if each.startswith("hello"):
        print(each)
file.close()


#Creating a file, where file name is given from user.
print("\n")
name=input("Give file name:")
file1=open(name,"w")
file1.write("I created this file.")
file1.close()
file1=open(name,"r")
data=file1.read()
print(data)
file1.close()


#Code to open a file and read through the file and search for lines that starts with "0."
#Count these lines and extract the floating point values from each of the lines and compute the average of those values.
fh = open("file2.txt","r")
count=0
ans=0
for line in fh:
    if not line.startswith("0.") :
        continue
    count=count+1
    pos=line.find("0.")
    data=line[pos:6]
    ans=ans+float(data)

print("Average: ",ans/count)
