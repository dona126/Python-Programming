# Given a String S, reverse the string without reversing its individual words. Words are separated by dots.

# Input:
# S = i.wake.up.early
# Output: early.up.wake.i

S=input("Enter String to be reversed:")
list1=S.split(".")
length_list1=len(list1)-1
output=""
for x in list1:
    output=output+list1[length_list1]+"."
    length_list1=length_list1-1

print(output[:-1],'\n')
