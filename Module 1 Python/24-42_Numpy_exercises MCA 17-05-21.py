#Exercise 1. Import the numpy package under the name np
import numpy as np

# 2. Print the numpy version and the configuration
print(np.__version__)
print()

#Exercise 3. Create a null vector of size 10
arr1 = np.array([])
print()

#Exercise 4. How to find the memory size of any array
arr2 = np.arange(10)
print(arr2.nbytes)
print()

#Exercise 5. How to get the documentation of the numpy add function from the command line?
help(np.add)
print()

# Exercise 6. Create a null vector of size 10 but the fifth value which is 1
arr3 = np.zeros(10)
arr3[4] = 1
print(arr3)
print()

# Exercise 7. Create a vector with values ranging from 10 to 49
arr4 = np.arange(10,49)
print(arr4)
print()

# Exercise 8. Reverse a vector (first element becomes last)
arr5 = np.arange(10)
arr5 = arr5[::-1]
print(arr5)
print()

# Exercise 9. Create a 3x3 matrix with values ranging from 0 to 8
arr6 = np.arange(0,9).reshape(3,3)
print(arr6)
print()

# Exercise 10. Find indices of non-zero elements from [1,2,0,0,4,0]
arr7 = np.array([1,2,0,0,4,0])
arr7 = arr7[arr7 > 0]
print(arr7.nonzero())
print(arr7)
print()

# Exercise 11. Create a 3x3 identity matrix
arr8 = np.identity(3)
print(arr8)
print()

# Exercise 12. Create a 3x3x3 array with random values
arr9 = np.random.randint(1,1000,27).reshape(3,3,3)
print(arr9)
print()

# Exercise 13. Create a 10x10 array with random values and find the minimum and maximum values
arr10 = np.random.randint(1,1000,100).reshape(10,10)
print("Minimum Value: ",arr10.min())
print("Maximum Value: ",arr10.max())
print()

arr1 = np.random.randint(1,1000,100).reshape(10,10)
min = arr1.min()
max = arr1.max()
print(arr1)
print(f"Minimum value is: {min}")
print(f"Maximum value is: {max}")
print()

# Exercise 14. Create a random vector of size 30 and find the mean value
arr11 = np.random.randint(25,589,30)
print(arr11.mean())
print()

# 15. Create a 2d array with 1 on the border and 0 inside
arr12 = np.ones((10,10))
arr12[1:-1,1:-1] = 0
print(arr12)
print()

# Exercise 16. How to add a border (filled with 0's) around an existing array?
arr13 = np.zeros((10,10))
arr13[1:-1,1:-1] = 1
arr14 = np.pad(arr13,pad_width=1,mode='constant',constant_values=1)
print(arr14)
print()

# Exercise 17. What is the result of the following expression?
print(0* np.nan)
print(np.nan == np.nan)
print(np.inf > np.nan)
print(np.nan - np.nan)
print(np.nan in set([np.nan]))
print(0.3 == (3 * 0.1))
print()

# Exercise 18. Create a 5x5 matrix with values 1,2,3,4 just below the diagonal
arr15 = np.array((5,5))
arr16 = np.diag(1+np.arange(4),k=-1)
print(arr16)

# 19. Create a 8x8 matrix and fill it with a checkerboard pattern
arr17 = np.ones((8,8), dtype=int)
arr17[::2,::2] = 0
arr17[1::2,1::2] = 0
print(arr17)
print()

# Exercise 20. Consider a (6,7,8) shape array, what is the index (x,y,z) of the 100th element?
arr18 = np.zeros((6,7,8))
arr19 = np.unravel_index(99,(6,7,8))
print(arr19)
print()

# Exercise 21. Create a checkerboard 8x8 matrix using the tile function
arr20 = np.array([1,2])
arr21 = np.tile(arr20,(8,8))
print(arr21)
print()

# Exercise 22. Normalize a 5x5 random matrix
arr23 = np.random.randint(27,563,25).reshape(5,5)
arr24 = (arr23-np.mean(arr23))/(np.std(arr23))
print(arr24)
print()

# Exercise 24. Multiply a 5x3 matrix by a 3x2 matrix (real matrix product)
arr25 = np.arange(0,15).reshape(5,3)
arr26 = np.arange(0,6).reshape(3,2)
arr27 = np.dot(arr25,arr26)
print(f"Dot product of the two arrays is: \n {arr27}")
print()

# 25. Given a 1D array, negate all elements which are between 3 and 8, in place.

arr30 = np.arange(10)
arr31 = (arr30 > 3) & (arr30 < 8)
arr30[arr31] *=-1
print("Negated Array between 3 and 8")
print(arr30)

# 26. What is the output of the following script?
print(sum(range(5),-1))
from numpy import *
print(sum(range(5),-1)) # ignores -1 as numpy reads this as an axis identifier

# 27. Consider an integer vector Z, which of these expressions are legal?
# Z**Z # Legal
# 2 << Z >> 2 # Legal  left shift 2 by each element of the vector and right shift each element of the vector by 2
# Z <- Z # Illegal
# 1j*Z  # Illegal in phython but 1* j * z is legal if j is also a vector
# Z/1/1 # Legal
# Z<Z>Z # Illegal

# 28. What are the result of the following expressions?

# np.array(0) / np.array(0) # cant divide by zero
# np.array(0) // np.array(0) # cant divide by zero
# np.array([np.nan]).astype(int).astype(float) # Not sure

# 29. How to round away from zero a float array ?

def round_away_zero(array):
    return np.round(array,0)

arr32  = np.random.uniform(2.1,11.3,15)
print(arr32)
print("Rounded away from zero Array")
print(round_away_zero(arr32))

# 30. How to find common values between two arrays?
arr33 = np.random.randint(10,20,15)
print("First Array")
print(arr33)
arr34 = np.random.randint(10,20,15)
print("Second Array")
print(arr34)
arr_list= []
for i in arr33:
    if i in arr34:
        arr_list.append(i)
arr35 = np.array(arr_list)
print("Common elements are:")
print(arr35)

# 31. How to ignore all numpy warnings (not recommended)?
# np.seterr(all="ignore")


# 32. Is the following expressions true?
print ( np.sqrt(-1) == np.emath.sqrt(-1) ) # I don't know why though


# 33. How to get the dates of yesterday, today and tomorrow?

from datetime import date
from datetime import timedelta
today = date.today()
tomorrow = today + timedelta(days=1)
yesterday = today - timedelta(days=1)
print("Today, ",today, " Yesterday, ", yesterday," and Tomorrow, ", tomorrow)

# 34. How to get all the dates corresponding to the month of July 2016?

import calendar as cl
year = 2016
month = 7

print(cl.month(year,month))

# 35. How to compute ((A+B)\*(-A/2)) in place (without copy)?

AB_array = np.random.randint(10,20,15)
BA_array = np.random.randint(20,30,15)
calc_array = np.array((AB_array+BA_array)*(-AB_array/2)) #dont know how to use "\*"
print(calc_array)

# 36. Extract the integer part of a random array using 5 different methods


# 37. Create a 5x5 matrix with row values ranging from 0 to 4

five_by_five_array = np.random.randint(0,5,25).reshape(5,5)
print(five_by_five_array)

# 38. Consider a generator function that generates 10 integers and use it to build an array
from random import seed
from random import randint
seed(1)
integer_list = []

def generate_integers():
    for i in range(10):
        integer_list.append(randint(0,10))
    return integer_list

gen_array = np.array(generate_integers())
print("Random Array")
print(gen_array)

# 39. Create a vector of size 10 with values ranging from 0 to 1, both excluded

vector_0_1_array = np.random.uniform(0.1,0.9,10)
print(vector_0_1_array)
print("zero Array to One")
print(vector_0_1_array)


# 40. Create a random vector of size 10 and sort it
vector_Array = np.random.random(10)
print("Vector to be sorted")
print(vector_Array)
print("Sorted vector")
print(sorted(vector_Array))

# 41. How to sum a small array faster than np.sum?
sumArray = np.random.random(5)
print("Array to sum")
print(sumArray)
print(sumArray.sum())

# 42. Consider two random array A and B, check if they are equal

arrA = np.random.random(15)
arrB = np.random.random(15)
print(np.array_equal(arrA,arrB))

