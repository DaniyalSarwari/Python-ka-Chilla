#--------------Tuples-----------------
# ordered collection of elements
# - Unmutable
# - enclosed in ()
# - Different kind of element

# Indexing in tuples
tup1 = (1, "python", True )
print(tup1[0])
print(tup1[0:3])


# other use cases
tup2 = (10, "Hello", False, 3.5 )

print(tup1 + tup2)
print(tup1*2 + tup2)

num = (20, 50, 10, 80, 14, 100, 27)
print(min(num))
print(max(num))

#------------------lists---------------
# - ordered collection of items
# - Mutable
# - enclosed in [] brackets

# we do other operations using list like indexing 
# and calling associated methods

# list1 + list2
# list1 * 2
# list1.append() etc etc


#----------------dictionarys--------------
# - unordered collection of elements
# - use curly braces {}
# - key: value pair
# - Mutable

dic = {"key1": "val1", "key2": "val2"}
# dic.keys()
# dic.values()
# dic["addingelem"] = value
# associated method can be called to play around with dictionary
# dic1.update(dic2)       # concat two dictionary


#---------------sets------------------
# - unordered and unindexed
# - using curly braces
# - No dublicated allowed

set1= {1, 2.2, 5, True, "adnan", "ali"}
# set1.add("ali")
# set1.remove(1)