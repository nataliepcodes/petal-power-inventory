"""
You’re the lead data analyst for a chain of gardening stores called Petal Power. 
Help them analyze their inventory!
"""

import pandas as pd
print(pd. __version__)

# 1: Load the data into a DataFrame called inventory
inventory = pd.read_csv('inventory.csv')

# 2: Inspect the first 10 rows of inventory
print(inventory.head(10))

# 3: The first 10 rows represent data from your Staten Island location. Select these rows and save them to staten_island.
staten_island = inventory.iloc[:10]
print(staten_island)

# 4: A customer just emailed you asking what products are sold at your Staten Island location. Select the column product_description from staten_island and save it to the variable product_request.
product_request = inventory['product_description']
print(product_request)

