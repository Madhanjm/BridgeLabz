this_tuple = ("apple", "banana", "cherry")
print(this_tuple)

print(len(this_tuple))

print(type(this_tuple))

this_tuple = tuple(("apple", "banana", "cherry"))
print(this_tuple)

print(this_tuple[1])
print(this_tuple[-1])
print(this_tuple[0:2])
print(this_tuple[:2])
print(this_tuple[0:])
print(this_tuple[-3:-1])
#for reversal step counter have to specify -1
print(this_tuple[-1:-3:-1])

this_tuple = tuple(("apple", "banana", "cherry"))
if "apple" in this_tuple:
    print("yes")
else:
    print("No")
    
this_tuple = tuple(("apple", "banana", "cherry"))
x=list(this_tuple)
x[0]="mango"
this_tuple=tuple(x)
print(this_tuple)
print(type(this_tuple))


this_tuple = tuple(("apple", "banana", "cherry"))
x=list(this_tuple)
x.append("chiku",)
this_tuple=tuple(x)
print(this_tuple)

this_tuple = tuple(("apple", "banana", "cherry"))
x=("straberry",)
this_tuple+=x
print(this_tuple)

this_tuple = tuple(("apple", "banana", "cherry"))
x=list(this_tuple)
x.remove("apple")
this_tuple=tuple(x)
print(this_tuple)

#del this_tuple
#print(this_tuple)

fruits=("apple","mango","chiku","banana")
(x,y,z,a)=fruits
print(x)
print(y)
print(z)
print(a)

fruits=("apple","mango","chiku","banana")
(x,y,*z)=fruits
print(x)
print(y)
print(z)

for i in fruits:
    print(i)

fruits=("apple","mango","chiku")
for i in range(len(fruits)):
    print(fruits[i])
    
fruits=("apple","mango")
i=0
while i<len(fruits):
    print(fruits[i])
    i+=1
    
#join tuples
fruits=("apple","mango","chiku")
number=(1,2,3,4)
join=fruits+number
print(join)    

#Multiply tuple
fruits=("apple","mango","chiku")
join=fruits*2
print(join)   

fruits=("apple","mango","chiku","apple")
print(fruits.count("apple"))

fruits=("apple","mango","chiku","apple")
print(fruits.index("mango"))

