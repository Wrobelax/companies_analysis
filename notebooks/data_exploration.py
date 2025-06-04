"""
This is a script used for data exploration, looking for trends and commons.
"""

# Importing modules.
import pandas as pd


# Reading file and assigning it to pandas module.
data = "../data/cleaned_data.csv"
df = pd.read_csv(data)



"""Data exploration"""
# Dividing categories of companies and checking how many are in each category.
df["category_list"] = df["categories"].dropna().apply(lambda x: [c.strip() for c in x.split(",")])
all_cat = df["category_list"].explode()
category_count = all_cat.value_counts()
# print(category_count.head())


# Checking average rating divided for each city.
# print(df["stars"].head())
# print(df["stars"].info()) # Checking dtype for column stars - float 64.
city_group = df.groupby(["city"], as_index = False)["stars"].mean()
# print(city_group.head(10).sort_values(by = "stars", ascending = False)) # Checking results