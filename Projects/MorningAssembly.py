
#There are equal number of boys and girls in a classroom.
#You need to arrange all of them in a line for the morning assembly such that the students must be in order of
#non-decreasing height and also no two boys or two girls must not be adjacent to each other.
#You have been given the heights of the boys in the array and the heights of the girls in the array. Find out whether
#you can arrange them in an order which satisfies the given conditions.
#Print "YES" if it is possible, or "NO" if it is not.

test=int(input("Enter number of test cases:"))
i=1
l1=[]
l2=[]
while((i<test) or (i==test)):
    n=int(input("Enter number of boys/girls:"))
    num=n

    hB=input("Enter height of all boys:")
    l1=hB.split(" ")
    z=0
    for x in l1:
        l1[z]=int(l1[z])
        z=z+1
    l1.sort()

    hG=input("Enter height of all girls:")
    l2=hG.split(" ")
    z=0
    for x in l2:
        l2[z]=int(l2[z])
        z=z+1
    l2.sort()

    l3=l1+l2
    z=0
    l4=[]
    w=0

    m=len(l3)-1
    while((n<m) or (n==m)):
        if(l3[w]>l3[n]):
            person=l3[n]
            l4.append(person)
            n=n+1
            if((l3[n]>l3[w]) and (n<len(l3))):
                break
            else:
                person=l3[w]
                l4.append(person)
                w=w+1
        elif(l3[w]<l3[n]):
            person=l3[w]
            l4.append(person)
            w=w+1
            if((l3[w]<l3[n]) and (w<num)):
                break
            else:
                person=l3[n]
                l4.append(person)
                n=n+1

    if(len(l4)==len(l3)):
        print("Possible arrangement: ",l4)
        print("YES")
    else:
        print("NO")
    l4.clear()
    l3.clear()
    l2.clear()
    l1.clear()
    i=i+1

