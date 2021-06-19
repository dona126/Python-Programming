# There is a large pile of socks that must be paired by color. Given an array of integers
# representing the color of each sock, determine how many pairs of socks with matching colors
# there are.

# Example
#arr = [1, 2, 1, 2, 1, 3, 2, 10, 10, 80, 80]
import math
def socksMatching(arr):
    # Write your code here
    dict1={}
    for x in arr:
        x=int(x)
        if x not in dict1:
            dict1[x]=1
        else:
            dict1[x]=dict1[x]+1
    values=dict1.values()
    count=0
    divide=0
    for x in values:
        if x==2:
            count=count+1
        if x>2:
            divide=math.floor(x/2)
            count=count+divide
    return(count) 

arr =input("Enter array elements as space separated numbers:")
arr=arr.split(" ")
result =socksMatching(arr)
print(result)
