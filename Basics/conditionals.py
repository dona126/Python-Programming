#Use of if,elif and else statements.
#Example 1
age=int(input("Enter age:")) 
if(age>18):
 print("Hey, i can vote!")
elif(age==0):
 print(":)") 
else:
 print("I can't vote.")
 
#Example 2 
score =float( input("Enter Score: "))
if score>=0.0 and score<=1.0:
    if( score >= 0.9):
        print("A Grade")
    elif( score >= 0.8):
        print("B Grade")
    elif( score >= 0.7):
        print("C Grade")
    elif( score >= 0.6):
        print("D Grade")
    else:
        print("F Grade")
else:
    print("Error!")
    
