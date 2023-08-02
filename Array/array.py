from array import *

# array formats: arrayName = array(typecodes,[])
#Typecode are the codes that are used to define the type of value the array will hold.
array1 = array('i', [10,20,30,40,50])

# let me use a for loop to get thevalues in array1
for item in array1:
    print(item)
array1.insert(8,60)
array1[5] = 80

array1.remove(30)
## now lets try the search operation:
print("search for item 40 in the array: ", array1.index(40))
print("first item in the array: ", array1[0])
print("second item in the array: ", array1[1])
print("first item in the array: ", array1)