# import array as arr
from array import *

val = array('i', [1, 2, 3, 4, 5,6,7,8,9])

for i in range(0,len(val)):
    print(val[i], end=" ")

print('\n')
for x in val: 
    print(x, end=", ")

print('\n')
print(val.typecode)

print('\n')
val.reverse()
for i in range(0,len(val)):
    print(val[i], end=" ")

print('\n')
val.insert(2,100)
val.append(50)
val.remove(9)
for i in range(0,len(val)):
    print(val[i], end=" ")

print('\n')
copyArray = array(val.typecode,(x for x in val))
copyArray.pop(3)

for i in range(0,len(copyArray)):
    print(copyArray[i], end=" ")

newVal = array('i', [10,20,30, 40,50,60,70,80,90])
# a = val[2:6]
a = newVal[2:-3]
print('\n')
for i in range(0,len(a)):
    print(a[i], end=" ")

print('\n')

# arr = array('i', [])

# n = int(input("Enter number of elements: "))
# for i in range(0,n):
#     x = int(input("Enter element: "))
#     arr.append(x)

# print("The elements in the array are: ")
# for i in range(0,len(arr)):
#     print(arr[i], end=" ")

i = newVal.index(50)
print(f"\nThe index of 50 in newVal array is: {i}")

