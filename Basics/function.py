#Functions in python

#Program 1
def sum(x,y):
 sum=x+y
 return sum
print("Ans is",sum(3,5))

#Program 2
def sum(a,b,c=None):
  if (c==None):
    return a+b
  else:
    return a+b+c
print("Third value given, sum is ", sum(11,12,13))
print("Third value not given, sum is ", sum(11,12))
