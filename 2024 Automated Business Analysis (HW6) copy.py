# 6. Mutual Information
# Ans:

import math
from collections import Counter

def get_probability(x: list):
    probabilities = {}
    for value in set(x):
        probability = x.count(value) / len(x)
        entropy = round(-1 * probability * math.log(probability, 2), 4)
        probabilities[value] = entropy
    return probabilities

def mutual_information(x: list, y: list):
    entropy_x = sum(get_probability(x).values())
    entropy_y = sum(get_probability(y).values())
    joint_probability = Counter(zip(x, y))
    entropy_x_y = sum(-p * math.log(p, 2) for p in (joint_probability[(xi, yi)] / len(x) for xi, yi in joint_probability))
    
    entropy_x_sum = sum(get_probability(x).values())
    entropy_y_sum = sum(get_probability(y).values())
    entropy_x_y_sum = entropy_x_y
    
    total_sum = entropy_x_sum + entropy_y_sum - entropy_x_y_sum
    
    print('mutual information')
    print(f'entropy_x: {entropy_x}, entropy_y: {entropy_y}, entropy_x_y: {entropy_x_y}')
    print(f'entropy_x_sum: {entropy_x_sum}, entropy_y_sum: {entropy_y_sum}, entropy_x_y_sum: {entropy_x_y_sum}')
    print(f'entropy_x_sum({entropy_x_sum}) + entropy_y_sum({entropy_y_sum}) - entropy_x_y_sum({entropy_x_y_sum})')
    
    return total_sum

# Test
x = ['S', 'B', 'S', 'B', 'B', 'S', 'B', 'S', 'B', 'B']
y = ['Black', 'Red', 'Yellow', 'Red', 'Yellow', 'Black', 'Black', 'Yellow', 'Yellow', 'Red']

print("Mutual Information:", mutual_information(x, y))
