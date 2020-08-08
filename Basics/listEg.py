
# Question: Open the file "hello.txt" and read it line by line. For each line, split the line into a list of words using the split() method.
# The program should build a list of words. For each word on each line check to see if the word is already in the list and if not
# append it to the list. When the program completes, sort and print the resulting words in alphabetical order.

fh= open("hello.txt","r")
lst = list()
for line in fh:
    lst1=line.split()#this fn return o/p in list
    for x in lst1:
        if x not in lst:
            lst.append(x)
lst.sort()
print(lst)
fh.close()
