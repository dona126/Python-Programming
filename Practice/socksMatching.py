#An array of integers representing the color of each sock is given. Find how many pairs of socks with matching colors are there.
# Example
#arr = [10, 10, 8, 8, 1, 1, 1, 1, 1, 5]
#Output: 4


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
