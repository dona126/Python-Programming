# Given a String S, reverse the string without reversing its individual words. Words are separated by dots.
#
# Example 1:
#
# Input:
# S = i.like.this.program.very.much
# Output: much.very.program.this.like.i
# Explanation: After reversing the whole
# string(not individual words), the input
# string becomes
# much.very.program.this.like.i
S=input("Enter String to be reversed:")
list1=S.split(".")
length_list1=len(list1)-1
output=""
for x in list1:
    output=output+list1[length_list1]+"."
    length_list1=length_list1-1

print(output[:-1],'\n')
