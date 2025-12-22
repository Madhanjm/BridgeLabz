this= {"apple", "banana", "cherry"}
print(this)

this = {"apple", "banana", "cherry", "apple"}
print(this)

this = {"apple", "banana", "cherry", "apple",1,True,1}
print(this)

this = {"apple", "banana", "cherry", "apple",1,True,1}
print(len(this))

set1 = {"abc", 34, True, 40, "male"}
print(type(set1))

set1 = set(("abc", 34, True, 40, "male"))
print(set1)

set1 = {"abc", 34, True, 40, "male"}
for x in set1:
    print(x)
    
set1 = {"abc", 34, True, 40, "male"}
print("abc" in set1)

set1 = {"abc", 34, True, 40, "male"}
print("abc" not in set1)

set1 = {"abc", 34, True, 40, "male"}
set1.add("hi")
print(set1)

set1 = {"abc", 34, True, 40, "male"}
this = {"apple", "banana", "cherry", "apple"}
#update() can add any objects
set1.update(this)
print(set1)

set1 = {"abc", 34, True, 40, "male"}
set1.remove("abc")#through errors if item not there in set
print(set1)

set1 = {"abc", 34, True, 40, "male"}
set1.discard("abc")# do not through errors if item not there in set
print(set1)

set1 = {"abc", 34, True, 40, "male"}
set1.pop()# it will remove a random item
print(set1)

set1 = {"abc", 34, True, 40, "male"}
set1.clear()
print(set1)

set1 = {"abc", 34, True, 40, "male"}
del set1
#print(set1)

set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = set1.union(set2)#if you use | opeartor works same
print(set3)

set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = {"John", "Elena"}
set4 = {"apple", "bananas", "cherry"}
mset1 = set1.union(set2, set3, set4)
print(mset1)

set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = {"John", "Elena"}
set4 = {"apple", "bananas", "cherry"}
mset = set1 | set2 | set3 |set4# | operator only for sets
print(mset)

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set3 = set1.intersection(set2)
print(set3)

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set3 = set1&(set2)#same working as intersection
print(set3)

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set1.intersection_update(set2)#change the original set insted of new set
print(set1)

set1 = {"apple", "banana" , "cherry"}
set2 = {"google", "microsoft", "apple"}
#The difference() method will return a new set that will contain only the items from the first set that are not present in the other set.
#use - insted of difff but - will work on sets only
set3 = set1.difference(set2)
print(set3)

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
#change the original set and return 1st set items not present in second
set1.difference_update(set2)
print(set1)

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1.symmetric_difference(set2)
print(set3)

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set1.symmetric_difference_update(set2)
print(set1)

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set1.symmetric_difference_update(set2)
print(set1)

#frozen set constructor
x = frozenset({"apple", "banana", "cherry"})
print(x)
print(type(x))

fs = frozenset({1, 2, 3})
cp = fs.copy()
print(fs)
print(cp)

a = frozenset({1, 2, 3, 4})
b = frozenset({3, 4, 5})
print("diff")
print(a.difference(b))
print(a - b)

a = frozenset({1, 2, 3, 4})
b = frozenset({3, 4, 5})
print(a.intersection(b))
print(a & b)

a = frozenset({1, 2})
b = frozenset({3, 4})
c = frozenset({2, 3})
print(a.isdisjoint(b))#return True if there is no comman elemnt
print(a.isdisjoint(c))

a = frozenset({1, 2})
b = frozenset({1, 2, 3})
print(a.issubset(b))
print(a <= b)
print(a < b)

a = frozenset({1, 2, 3})
b = frozenset({1, 2})
print(a.issuperset(b))
print(a >= b)
print(a > b)


a = frozenset({1, 2, 3})
b = frozenset({3, 4, 5})
print(a.symmetric_difference(b))
print(a ^ b)

a = frozenset({1, 2})
b = frozenset({2, 3})
print(a.union(b))
print(a | b)