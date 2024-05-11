# 3. Write a python function to calculate Euclidean Distance and Minkowski Distance.
# Ans:
# import numpy as np

# a=[5,8,6,4,7,2]
# b=[1,4,3,1,6,0]

# def minkowski(a:list, b:list, r):

import numpy as np

def euclidean_distance(a, b):
    return np.sqrt(np.sum((np.array(a) - np.array(b)) ** 2))

def minkowski_distance(a, b, r):
    return np.sum(np.abs(np.array(a) - np.array(b)) ** r) ** (1 / r)

# Example
a = [5, 8, 6, 4, 7, 2]
b = [1, 4, 3, 1, 6, 0]
r = 3

euclidean = euclidean_distance(a, b)
minkowski = minkowski_distance(a, b, r)

print("Euclidean Distance:", euclidean)
print("Minkowski Distance with r =", r, ":", minkowski)
