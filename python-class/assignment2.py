#assignment operator
a = 1
b = 7
c= 0
d= 1

#arithmetic operator
c = a + b
print ("The sum of a: {} and b: {} is {} " .format(a, b, c))

#comparison operator
if a>b:
    print("Yes, a is greater than b")
else:
    print("No, a is less than b")

#Bitwise operator
d= a&b
print ("The result of a and b is", d, bin(d))

#logical operators
print (a > 3 and a <10)

#membership operator

list = [1, 2, 3, 4, 5]

if (a in list):
    print ("a is present in the given list")
else:
    print ("a is not present in the given list")

#identity operators

f = [1, 2, 3]
g = [1, 2, 3]
f = g

print (f is g)
print (f is not g)
print (f is g)
