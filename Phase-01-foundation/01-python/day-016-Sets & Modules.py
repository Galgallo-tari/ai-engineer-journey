# sets

#Set ..... Mutable, No Duplicate and Unordered

cs_courses = {'Math', 'Design', 'AI', 'IT'}
art_courses = {'Craft', 'Math', 'History', 'Design'}

print(cs_courses.intersection(art_courses))     #{'Math', 'Design'}
print(cs_courses.difference(art_courses))       #{'IT', 'AI'}
print(art_courses.difference(cs_courses))       #{'History', 'Craft'}
print(cs_courses.union(art_courses))            #{'IT', 'History', 'Math', 'Design', 'AI', 'Craft'}


cs_courses.add('LLM')
print(cs_courses)


# cs_courses.clear()
# print(cs_courses)


#
# To remove an element from the set,
# you have two options.
# You can either use the .remove() method or the .discard() method,
# and pass in the element that you want to remove as argument.

#The .remove() method will raise a KeyError if the element is not found,
# while the .discard() method will not:


# cs_courses.remove('tt')
# print(cs_courses)

cs_courses.discard ('tt')
print(cs_courses)


# Subset — "Is everything in A also in B?"
# A set A is a subset of B if every element of A exists in B.

#Superset — "Does A contain everything in B?"
#A set A is a superset of B if A has all the elements of B (and possibly more).


B = {1, 2, 3, 4, 5}
A = {2, 3, 4}       # ← every element of A is inside B ✓

print(A.issubset(B))        #"Is every element of A found in B?"
print(A.issuperset(B))      #"Does A contain every element of B?"

#The .isdisjoint() method checks if two sets are disjoint,
# which means they don't have any elements in common.

print(A.isdisjoint(B)) # False

#The union operator | returns a new set with all the elements from both sets

#The intersection operator & returns a new set with only the elements that the sets have in common

#The difference operator - returns a new set with the elements of the first set that are not in the other sets


