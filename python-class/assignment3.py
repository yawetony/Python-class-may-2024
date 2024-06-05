# Append a string element to the string list:
stringList = ['mon', 'tue', 'wed', 'thu']
print(stringList)
stringList.append('fri')
print(stringList)

#Insert item in a list
fruits = ['apple', 'banana', 'cherry']
print(fruits)
fruits.insert(1, "orange")
print(fruits)

# Extend a list:
list1 = ['john', 'paul', 'mary']
list2 = ['adam', 'aggrey', 'joy']
print(list1)
list1.extend(list2)
print(list1)

#remove an item from the list:
plants = ['beans', 'maize', 'coffee', 'passion']
print(plants)
plants.remove('maize')
print(plants)

#remove element at specified position (pop)
classroom =['chalk', 'books', 'pen', 'pencil', 'blackboard']
print (classroom)
classroom.pop(1)
print(classroom)

#number of elements
set = [1,2,3,4,5,3,4,5,5,1,2]
print(set)
set1 = set.count(5)
print(set1)

#sort the list
alpha = [2,1,7,6,5,3,]
print(alpha)
alpha.sort()
print (alpha)

#reverse a string
txt1 = "Mulwanyamuli the former katikilo" [::-1]
print (txt1)

#concatenate two strings
string1 = "Today is a great day"
string2 = "To go for a run"
print (string1 + string2)





