"""This is a script used for data reading, cleaning and extracting new file."""

import json
import pandas as pd


# Reading file and assigning it to pandas module.
url = "../data/yelp_academic_dataset_business.json"
df = pd.read_json(url, lines = True)



"""Basic data exploration"""
print(df.info()) # 'business_id as a unique identifier. Date present, format to be adjused.
print(df.head(10)) # 'business_id', 'name', 'address', 'city', 'state', 'postal_code', 'latitude', 'longitude', 'stars', 'review_count', 'is_open', 'attributes'
print(df.isnull()) # 'attributes', 'categories' and 'hours' with missing data.




# df.to_csv("../data/cleaned_data.csv", index = False) # Saving cleaned file in csv format for easier handling.