# 4. Write decdion tree and random seed = 2
# Ans:

from sklearn.tree import DecisionTreeClassifier
import numpy as np

# Setting random seed for reproducibility
np.random.seed(2)

# Sample data
X = np.array([[1, 2], [3, 4], [5, 6], [7, 8]])
y = np.array([0, 1, 0, 1])

# Creating the Decision Tree Classifier
clf = DecisionTreeClassifier()

# Fitting the classifier to the data
clf.fit(X, y)

