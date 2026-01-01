import re
#Search the string to see if it starts with "The" and ends with "Spain":
txt="The Abin in Spain"
x=re.search("^The.*Spain$",txt)
if x:
    print("Yes Match found")
    print(x)
else:
    print("No Match")
    
#Ascii match
s="hi madhan"
print(re.findall("\w",s,re.A))

#match only didgit

x="hello 6 for men 10"
y=re.findall("\d+",x)
print(y)

print(re.search(r"^hello",x))

print(bool(re.match(r"^\d{10}$", "9876543210")))
print(bool(re.match(r"^\d{10}$", "98765432101")))


x="hello 6 for men 10"
words=re.findall(r"[a-z]+",x)
print(words)

x="hell"
words=re.findall(r"^[a-z]+$",x)
print(words)

#email
r"^[\w\.-]+@[\w\.-]+\.\w+$"

#date validation dd-mm-yyyy
r"^\d{2}-\d{2}-\d{4}$"

