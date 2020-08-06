#A classroom has several students, half of whom are boys and half of whom are girls.
#You need to arrange all of them in a line for the morning assembly such that the following conditions are satisfied:
  1.The students must be in order of non-decreasing height.
  2.Two boys or two girls must not be adjacent to each other.
#You have been given the heights of the boys in the array and the heights of the girls in the array . Find out whether you can arrange them in an order which satisfies
#the given conditions. Print "YES" if it is possible, or "NO" if it is not.

test=int(input("Enter number of test cases:"))
i=1
l1=[]
l2=[]
while((i<test) or (i==test)):
    n=int(input("Enter number of boys:(same as the number of girls)"))
    j=1
    while((j<n) or (j==n)):
        h=int(input())
        l1.append(h)
        l1.sort()
        j=j+1
    j=1
    while((j<n) or (j==n)):
        h=int(input())
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
    print(l4)

    if(len(l4)==len(l3)):
        print("YES")
    else:
        print("NO")
    l4.clear()
    l3.clear()
    l2.clear()
    l1.clear()
    i=i+1
