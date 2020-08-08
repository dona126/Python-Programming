
#String(not mutable)
str1="hello"
a=len(str1)
print("Length: ",a)

print(str1[4])

print(max(str1))
print(min(str1))

for x in "python":
  print(x, end=" ")
print("")



#Slicing in string.
s="monthly"
print(s[0:7:2])
print(s[::])
print(s[1:7:2])



#Use of "in" in string.
print("\n")
if "in" in "india":
    print("founded")

#String comparison.(here capitalLetter < smallLetter)
print("\n")
if "A"<"a":
    print("CapitalLetter < smallLetter.")

#Useful inbuilt functions in string.
print("")
greet=" good morning"
print(greet.lower())
print(greet.upper())
print(greet.capitalize())
print(greet.find("go"))#prints the position #if not found prints -1
print(greet.find("zz"))

print(greet.replace("morning","evening"))#search and replace
print(greet.lstrip())#remove white spaces in left
print(greet.rstrip())#remove white spaces in right
print(greet.strip())#remove white spaces in beginning and end
print(greet.startswith(" "))



#Write code using find() and string slicing to extract the number at the end of the line, "Extract this number:    0.8475". Convert the extracted
#value to a floating point number and print it out.
text = "Extract this number:    0.8475";
pos=text.find("0.")
cha=text[pos::]
print(float(cha))
