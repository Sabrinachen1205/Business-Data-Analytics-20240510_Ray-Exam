# 1. Write a solution to find the ids of products that are both low fat and recyclable.
# product_id	low_fats	recycle
# 0	            Y	        N
# 1	            Y	        Y
# 2	            N	        Y
# 3	            Y	        Y
# 4	            N	        N

import pandas as pd

# Creating a DataFrame with the given data
data = {
    'product_id': [0, 1, 2, 3, 4],
    'low_fats': ['Y', 'Y', 'N', 'Y', 'N'],
    'recycle': ['N', 'Y', 'Y', 'Y', 'N']
}

df = pd.DataFrame(data)

# Filtering products that are both low fat and recyclable
filtered_products = df[(df['low_fats'] == 'Y') & (df['recycle'] == 'Y')]

# Getting the ids of the filtered products
product_ids = filtered_products['product_id'].tolist()

print("Product IDs of products that are both low fat and recyclable:", product_ids)
