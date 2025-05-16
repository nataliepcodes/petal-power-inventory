"""
You’re the lead data analyst for a chain of gardening stores called Petal Power. 
Help them analyze their inventory!
"""

import pandas as pd

# 1: Load the data into a DataFrame called inventory
inventory = pd.read_csv('inventory.csv')

# 2: Inspect the first 10 rows of inventory
print(inventory.head(10))

# 3: The first 10 rows represent data from your Staten Island location. Select these rows and save them to staten_island.
staten_island = inventory.iloc[:10]

# 4: A customer just emailed you asking what products are sold at your Staten Island location. Select the column product_description from staten_island and save it to the variable product_request.
product_request = inventory['product_description']

# 5: Another customer emails to ask what types of seeds are sold at the Brooklyn location. Select all rows where location is equal to Brooklyn and product_type is equal to seeds and save them to the variable seed_request
seed_request = inventory[(inventory.location == 'Brooklyn') & (inventory.product_type == 'seeds')]
print(seed_request)

