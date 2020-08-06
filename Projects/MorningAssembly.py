

#There are equal number of boys and girls in a classroom.
#You need to arrange all of them in a line for the morning assembly such that the students must be in order of
#non-decreasing height and also no two boys or two girls must not be adjacent to each other.
#You have been given the heights of the boys and the heights of the girls. Find out whether
#you can arrange them in an order which satisfies the given conditions.
#Print "YES" if it is possible, or "NO" if it is not.

test=int(input("Enter number of test cases:"))
i=1
l1=[]
l2=[]
while((i<test) or (i==test)):
    n=int(input("Enter number of boys/girls:"))
    j=1
    while((j<n) or (j==n)):
        h=int(input("Enter height of  boy:"))
        l1.append(h)
        l1.sort()
        j=j+1
    j=1
    while((j<n) or (j==n)):
        h=int(input("Enter height of  girl:"))
        l2.append(h)
        l2.sort()
        j=j+1

    l3=l1+l2
    l4=[]
    w=0
    m=len(l3)-1
    while((n<m) or (n==m)):
        if(l3[w]>l3[n]):
            person=l3[n]
            l4.append(person)
            n=n+1
            person=l3[w]
            l4.append(person)
            w=w+1
        elif(l3[w]<l3[n]):
            person=l3[w]
            l4.append(person)
            w=w+1
            person=l3[n]
            l4.append(person)
            n=n+1
    print("Possible arrangement: ",l4)

    if(len(l4)==len(l3)):
        print("YES")
    else:
        print("NO")
    l4.clear()
    l3.clear()
    l2.clear()
    l1.clear()
    i=i+1
