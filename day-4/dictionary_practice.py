#Dictionaries are used to store data values in key:value pairs.
#A dictionary is a collection which is ordered, changeable and do not allow duplicates.
#As of Python version 3.7, dictionaries are ordered. In Python 3.6 and earlier, dictionaries are unordered

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict)

#refer the dict using key name
print(thisdict["brand"])

#Dictionaries cannot have two items with the same key
#Duplicate values will overwrite existing values:
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  "year": 2020
}
print(thisdict)

#using len we can find dict length
print(len(thisdict))

#dict constructor
thisdict = dict(name = "John", age = 36, country = "Norway")
print(thisdict)

#acces using key
thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = thisdict["model"]
print(x)
#access using get method
x = thisdict.get("model")
print(x)

#using key() we can get the all the keys
x=thisdict.keys()
print(x)

#add keys
car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

x = car.keys()
print(x) #before the change
car["color"] = "white"
print(x) #after the change

#using get() we can get the values
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = thisdict.values()
print(x)

#changing the value
car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

x = car.values()
print(x) #before the change
car["year"] = 2020
print(x) #after the change

#The items() method will return each item in a dictionary, as tuples in a list
x = thisdict.items()
print(x)

#we can check specific key present using in 
print("model" in car)

#updating the value using update()
sdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
sdict.update({"year": 2020})
print(sdict)
#using update we can add items to dictionary only if it is not present

#using pop() we can delete the dictionary
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.pop("model")
print(thisdict)

#popitem() removes the last item
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.popitem()
print(thisdict)

#using del keyword and passing key and it can also delete the entire dictionary
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
del thisdict["year"]
print(thisdict)

#clear method empty the dictionary
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.clear()
print(thisdict)

#using for loop
#printing keys
thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
for x in thisdict:
  print(x)
  #or
for x in thisdict.keys():
    print(x)

#print values
for i in thisdict:
    print(thisdict[x])
#or
for x in thisdict.values():
  print(x)
  
#using item() we can get key values
for x,y in thisdict.items():
    print(x,y)  
    
#copy a dictionary use copy()
thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x=thisdict.copy()
print(x)

#use dict() to make copy()
thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x=dict(thisdict)
print(x)

#A dictionary can contain dictionaries, this is called nested dictionaries.
#The below dictionary contains 3 dictionary inside
myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}

#if you want to add three dictionaries into a new dictionary:
    #Create three dictionaries, then create one dictionary that will contain the other three dictionaries:
child1 = {
  "name" : "Emil",
  "year" : 2004
}
child2 = {
  "name" : "Tobias",
  "year" : 2007
}
child3 = {
  "name" : "Linus",
  "year" : 2011
}

myfamily={
    "child1":child1,
    "child2":child2,
    "child3":child3
}
print(myfamily)

#access dict in nested loops
myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}

print(myfamily["child2"]["name"])

#using items()
myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}

for x, obj in myfamily.items():
    print(x)
    
    for y in obj:
        print(y + ':', obj[y])
        
"""      
methods in dictionary

1 clear()->Removes all the elements from the dictionary
2 copy()->Returns a copy of the dictionary
3 fromkeys()->Returns a dictionary with the specified keys and value
4 get()->Returns the value of the specified key
5 items()->Returns a list containing a tuple for each key value pair
6 keys() ->Returns a list containing the dictionary's keys
7 pop()->Removes the element with the specified key
8 popitem()->Removes the last inserted key-value pair
9 setdefault()->Returns the value of the specified key. If the key does not exist: insert the key, with the specified value
10 update()->	Updates the dictionary with the specified key-value pairs
11 values()->Returns a list of all the values in the dictionary
"""