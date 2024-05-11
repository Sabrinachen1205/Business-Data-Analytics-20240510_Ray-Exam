# 5. Write information gain function
# Ans:

import math

label = ['1', '1', '1', '0', '0', '0', '0', '0', '0', '0']
label_left = ['0', '0', '0']
label_right = ['1', '1', '1', '0', '0', '0', '0']

def get_probability(x: list):
    probabilities = {}
    for value in set(x):
        probability = x.count(value) / len(x)
        entropy = round(-1 * probability * math.log(probability, 2), 4)
        probabilities[value] = entropy
    return probabilities

def entropy(x: list):
    probabilities = get_probability(x)
    entropy_value = sum(probabilities.values())
    return entropy_value

def information_gain(x: list, x_left: list, x_right: list):
    # Calculate entropy of x (before split)
    entropy_before_split = entropy(x)
    
    # Calculate entropy of x_left, x_right
    entropy_after_split_left = entropy(x_left)
    entropy_after_split_right = entropy(x_right)
    
    # Calculate entropy after split
    entropy_after_split = (len(x_left) / len(x)) * entropy_after_split_left + (len(x_right) / len(x)) * entropy_after_split_right
    
    # Calculate information gain
    information_gain_value = entropy_before_split - entropy_after_split
    
    return information_gain_value

# Test
print("Information Gain:", information_gain(label, label_left, label_right))

