"""This is a script used for data reading, cleaning and extracting new file.
Some code was left commented as it was used ald left for reference.
"""

# Importing modules.
import pandas as pd
import numpy as np


# Reading file and assigning it to pandas module.
url = "../data/yelp_academic_dataset_business.json"
df = pd.read_json(url, lines = True)



"""Basic data exploration for data cleaning."""
# Checking general data
# print(df.info()) # 'business_id as a unique identifier. Date present, format to be adjusted. 153k rows.
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
# print(df["city"].str.isalpha()) # Not all city names have only letters.
# print(df["city"].str.isalpha().value_counts()) # 39k hits with special characters. Potentially spaces and "-".
city_special_char = (((~df["city"].str.isalpha()) & (~df["city"].str.contains(r"[ -]", regex=True))).sum())
# print(city_special_char) # 208 hits where special character is present in city and is not a space or "-".
# print(df.loc[city_special_char, "city"].head(10)) # "." and "'" present - ok.
# print(df["state"].str.islower().value_counts()) # All upper - ok.
# print(df["state"].str.isalpha().value_counts()) # All alphabetic - ok.


# Checking unique data.
# print(df["attributes"].nunique()) # Dict type.
# print(df["categories"].nunique()) # 83k unique categories.


# Checking if there are trailing spaces.
spaces = df.select_dtypes(include="object").apply(lambda col: col.str.strip() != col)
columns_with_spaces = spaces.any()[spaces.any()].index.tolist()
# print("columns with extra spaces:", columns_with_spaces) # columns with extra spaces: ['name', 'address', 'city', 'attributes', 'categories', 'hours']



"""Data cleaning, formatting, type changing, filling missing data."""
# Removing trailing spaces.
df["name"] = df["name"].str.strip()
df["address"] = df["address"].str.strip()
df["city"] = df["city"].str.strip()
df["attributes"] = df["attributes"].str.strip()
df["categories"] = df["categories"].str.strip()


# Filling missing data.
df = df.replace("", np.nan)


# Dropping opening hours. It will not be used for analysis.
df = df.drop(columns = ["hours"])



"""Saving cleaned file"""
# df.to_csv("../data/cleaned_data.csv", index = False) # Saving cleaned file in csv format for easier handling.