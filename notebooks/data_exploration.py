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
# print(category_count.head()) # Uncomment to check results.


# Checking average rating divided for each city.
# print(df["stars"].head())
# print(df["stars"].info()) # Checking dtype for column stars - float 64.
city_group = df.groupby(["city"], as_index = False)["stars"].mean()
# print(city_group.head(10).sort_values(by = "stars", ascending = False)) # Uncomment to check results.


# Checking top 10 companies with the highest rate and review_count greater than 50.
rc_over_50 = df[df["review_count"] > 50].copy()
top_rated_companies = rc_over_50.sort_values(by = "stars", ascending = False)
# print(top_rated_companies.head(10)[["name", "stars", "review_count"]]) # Uncomment to check results.


# Checking correlation between number of opinions and stars.
# print(df[["name","stars", "review_count"]].sort_values(by = "review_count", ascending = False)) # Uncomment to check results.


# Companies with the lowest rate and number of opinions - unfiltered.
# print(df[["name", "stars", "review_count"]].sort_values(by = "stars", ascending = True).head(10)) # Uncomment to check results.


# Companies with the lowest rate and number of opinions - review_count > 50.
# print(rc_over_50.sort_values(by = "stars", ascending = True)[["name", "stars", "review_count"]].head(10))  # Uncomment to check results.