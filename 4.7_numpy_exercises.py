#!/usr/bin/env python
# coding: utf-8

# # Numpy Exercise


import functools as ft
import itertools as it
import operator
import numpy as np

a = np.array([4, 10, 12, 23, -2, -1, 0, 0, 0, -6, 3, -7])


# 1. How many negative numbers are there?


nnegatives = (a < 0).sum()
assert nnegatives == 4


# 2. How many positive numbers are there?


npositives = (a > 0).sum()
assert npositives == 5


# 3. How many even positive numbers are there?


neven_positives = (a[a > 0] % 2 == 0).sum()
assert neven_positives == 3


# 4. If you were to add 3 to each data point, how many positive numbers would there be?

a_plus_3 = a + 3
npositives_plus_3 = (a_plus_3 > 0).sum()
assert npositives_plus_3 == 10


# 5. If you squared each number, what would the new mean and standard deviation be?

a_squared = a ** 2
print("Mean:", a_squared.mean())
print("Standard deviation:", a.std())


# 6. A common statistical operation on a dataset is centering. This means to adjust the data such that the center of the data is at 0. This is done by subtracting the mean from each data point. Center the data set.

a_centered = a - a.mean()
print("centered:", a_centered)


# 7. Calculate the z-score for each data point.

z_scores = (a - a.mean()) / a.std()
print(z_scores)


# 8. Copy the setup and exercise directions from More Numpy Practice into your 4.7_numpy_exercises.py and add your solutions.

# Life w/o numpy to life with numpy

## Setup 1
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Use python's built in functionality/operators to determine the following:


# Exercise 1 - Make a variable called sum_of_a to hold the sum of all the numbers in above list
sum_of_b = sum(b)
print("Sum of b:", sum_of_b)


# Exercise 2 - Make a variable named min_of_a to hold the minimum of all the numbers in the above list
min_of_b = min(b)
print("Min of b:", min_of_b)


# Exercise 3 - Make a variable named max_of_a to hold the max number of all the numbers in the above list
max_of_b = max(b)
print("Max of b:", max_of_b)


# Exercise 4 - Make a variable named mean_of_a to hold the average of all the numbers in the above list
mean_of_b = sum_of_b / len(b)
print("Mean of b:", mean_of_b)


# Exercise 5 - Make a variable named product_of_a to hold the product of multiplying all the numbers in the above list together
product_of_b = ft.reduce(operator.mul, b)
print("Product of b:", product_of_b)


# Exercise 6 - Make a variable named squares_of_a. It should hold each number in a squared like [1, 4, 9, 16, 25...]
squares_of_b = list(map(operator.mul, b, b))
print("Squares of b:", squares_of_b)


# Exercise 7 - Make a variable named odds_in_a. It should hold only the odd numbers
odds_in_b = list(filter(lambda x: x % 2 == 1, b))
print("Odds in b:", odds_in_b)


# Exercise 8 - Make a variable named evens_in_a. It should hold only the evens.
evens_in_b = list(filter(lambda x: x % 2 == 0, b))
print("Evens in b:", evens_in_b)


## What about life in two dimensions? A list of lists is matrix, a table, a spreadsheet, a chessboard...
## Setup 2: Consider what it would take to find the sum, min, max, average, sum, product, and list of squares for this list of two lists.
b = [[3, 4, 5], [6, 7, 8]]

b = np.array(b)


# Exercise 1 - refactor the following to use numpy. Use sum_of_b as the variable. **Hint, you'll first need to make sure that the "b" variable is a numpy array**
# sum_of_b = 0
# for row in b:
#     sum_of_b += sum(row)
# print(sum_of_b)

sum_of_b = b.sum()
print("Sum of c:", sum_of_b)


# Exercise 2 - refactor the following to use numpy.
# min_of_b = min(b[0]) if min(b[0]) <= min(b[1]) else min(b[1])
# print(min_of_b)

min_of_b = b.min()
print("Min of b:", min_of_b)


# Exercise 3 - refactor the following maximum calculation to find the answer with numpy.
# max_of_b = max(b[0]) if max(b[0]) >= max(b[1]) else max(b[1])
# print(max_of_b)

max_of_b = b.max()
print("Max of b:", max_of_b)


# Exercise 4 - refactor the following using numpy to find the mean of b
# mean_of_b = (sum(b[0]) + sum(b[1])) / (len(b[0]) + len(b[1]))
# print(mean_of_b)

mean_of_b = b.mean()
print("Mean of b:", mean_of_b)


# Exercise 5 - refactor the following to use numpy for calculating the product of all numbers multiplied together.
# product_of_b = 1
# for row in b:
#     for number in row:
#         product_of_b *= number
# print(product_of_b)

product_of_b = b.prod()
print("Product of b:", product_of_b)


# Exercise 6 - refactor the following to use numpy to find the list of squares
# squares_of_b = []
# for row in b:
#     for number in row:
#         squares_of_b.append(number**2)
# print(squares_of_b)

squares_of_b = b ** 2
assert squares_of_b.flatten().tolist() == [9, 16, 25, 36, 49, 64]


# Exercise 7 - refactor using numpy to determine the odds_in_b
# odds_in_b = []
# for row in b:
#     for number in row:
#         if(number % 2 != 0):
#             odds_in_b.append(number)
# print(odds_in_b)

odds_in_b = b[b % 2 == 1]
assert odds_in_b.flatten().tolist() == [3, 5, 7]


# Exercise 8 - refactor the following to use numpy to filter only the even numbers
# evens_in_b = []
# for row in b:
#     for number in row:
#         if(number % 2 == 0):
#             evens_in_b.append(number)
# print(evens_in_b)

evens_in_b = b[b % 2 == 0]
assert evens_in_b.flatten().tolist() == [4, 6, 8]


# Exercise 9 - print out the shape of the array b.
print(b.shape)


# Exercise 10 - transpose the array b.
print(b.transpose())


# Exercise 11 - reshape the array b to be a single list of 6 numbers. (1 x 6)
print(b.flatten())


# Exercise 12 - reshape the array b to be a list of 6 lists, each containing only 1 number (6 x 1)
print(b.reshape((b.size, 1)))


## Setup 3
c = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# HINT, you'll first need to make sure that the "c" variable is a numpy array prior to using numpy array methods.
c = np.array(c)


# Exercise 1 - Find the min, max, sum, and product of c.
print("Min:", c.min())
print("Max:", c.max())
print("Sum:", c.sum())
print("Product:", c.prod())


# Exercise 2 - Determine the standard deviation of c.
print("Standard deviation:", c.std())


# Exercise 3 - Determine the variance of c.
print("Variance:", c.var())


# Exercise 4 - Print out the shape of the array c
print("Shape:", c.shape)


# Exercise 5 - Transpose c and print out transposed result.
print("Transposition:\n", c.T)


# Exercise 6 - Multiply c by the c-Transposed and print the result.
print(c * c.T)


# Exercise 7 - Write the code necessary to sum up the result of c times c transposed. Answer should be 261
print((c * c.T).sum())


# Exercise 8 - Write the code necessary to determine the product of c times c transposed. Answer should be 131681894400.
print((c * c.T).prod())


## Setup 4
d = [
    [90, 30, 45, 0, 120, 180],
    [45, -90, -30, 270, 90, 0],
    [60, 45, -45, 90, -45, 180],
]

d = np.array(d)


# Exercise 1 - Find the sine of all the numbers in d
print(np.sin(d))


# Exercise 2 - Find the cosine of all the numbers in d
print(np.cos(d))


# Exercise 3 - Find the tangent of all the numbers in d
print(np.tan(d))


# Exercise 4 - Find all the negative numbers in d
print(d[d < 0])


# Exercise 5 - Find all the positive numbers in d
print(d[d > 0])


# Exercise 6 - Return an array of only the unique numbers in d.
print(np.unique(d))


# Exercise 7 - Determine how many unique numbers there are in d.
print(np.unique(d).size)


# Exercise 8 - Print out the shape of d.
print(d.shape)


# Exercise 9 - Transpose and then print out the shape of d.
print(d.T.shape)


# Exercise 10 - Reshape d into an array of 9 x 2
print(d.reshape(9, 2))

