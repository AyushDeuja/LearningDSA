from numpy import *

# val = array([1, 2, 3, 4, 5.5,6.4,7,8,9, "A"])
# val = linspace(1,10,9)  # 9 values between 1 and 10
# val = arange(1,10,2)  # values between 1 and 10 with step 2
# val = logspace(1,10,5)  # 5 values between 10^1 and 10^10
# val = zeros(5) # array of 5 zeros
# val = ones((3,4), int)  # 3x4 array of ones
val = full(10,5) # array of 10 elements with all values as 5


for x in val: 
    print(x, end=" ")

print('\n')
zero = array(10)
print(zero)

print('\n')
one = array([10,20,30,40,50])
print(one)

print('\n')
two = array([[1,2,3],[4,5,6],[7,8,9]])
print(two)

print('\n')
three = array([[[1,2,3],[4,5,6],[7,8,9]], [[10,11,12],[13,14,15],[16,17,18]]])
print(three)