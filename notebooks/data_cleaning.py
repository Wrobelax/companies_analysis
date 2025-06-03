"""This is a script used for data reading, cleaning and extracting new file.
Some code was left commented as it was used ald left for reference.
"""

import pandas as pd


# Reading file and assigning it to pandas module.
url = "../data/yelp_academic_dataset_business.json"
df = pd.read_json(url, lines = True)



"""Basic data exploration for data cleaning."""
# Checking general data
print(df.info()) # 'business_id as a unique identifier. Date present, format to be adjusted. 153k rows.
# print(df.head(10)) # 'business_id', 'name', 'address', 'city', 'state', 'postal_code', 'latitude', 'longitude', 'stars', 'review_count', 'is_open', 'attributes'
# print(df.isnull()) # 'attributes', 'categories' and 'hours' with missing data.

# Checking individual columns.
# print(df["name"].head(10)) # Unique names of companies. dtype: object - ok.
# print(df["address"].head(10)) # Mix of numbers and letters. dtype: object - ok.
# print(df["postal_code"].head(10)) # Numbers only, no dashes or letters. dtype: object - potentially to be changed.
# print(df["state"].head(10)) # Unified into two letters - abbreviations. dtype: object - ok.
# print(df["attributes"].head(10)) # Unique categories of a business. dtype: object - ok. Potentially drop.
# print(df["categories"].head(10)) # Unique description of a business. dtype: object - ok. Potentially drop.
# print(df["hours"].head(10)) # Opening hours. dtype: object - to be unified into date.

# Checking unique data.
# print(df["attributes"].nunique()) # Dict type.
# print(df["categories"].nunique()) # 83k unique categories.



"""Data cleaning, formatting, type changing, filling missing data."""
# Removing trailing spaces.




# df.to_csv("../data/cleaned_data.csv", index = False) # Saving cleaned file in csv format for easier handling.