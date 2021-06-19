# A hiker moves a step UP or a step DOWN. Start and end at sea level.
# Mountain- start with step UP and end with step DOWN.
# Valley- start with step DOWN and end with step UP.
# Find number of valleys walked through.

# Uses;
#  U for UP 
#  D for DOWN

#Input:
#path="U D D D U D U U"
#Output:1
#

def valleyCount(path):
    count=0
    result=0
    for x in path:
        if x=="D":
            count=count-1
            
        if x=="U":
            count=count+1
            if(count==0):
                result=result+1
        
    return(result) 


path=input("Enter all the steps taken ('U' or 'D')  as space separated:")
path=path.split(" ")
result=valleyCount(path)
print(result)
