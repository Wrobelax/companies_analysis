"""
This is a script for data modeling and visualisation used for generating outputs.
Some lines with code are commented as they were used solely for analysis and left for reference.
"""


# Modules importing.
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
from sklearn.metrics import r2_score, mean_squared_error

sns.set(style = "whitegrid")

# Importing file with cleaned data into dataframe.
url = "../data/cleaned_data.csv"
df = pd.read_csv(url)



"""Data modeling."""
# Visualization of number of companies to rating (stars).
min_star = df['stars'].min()
max_star = df['stars'].max()
bins = np.arange(min_star - 0.25, max_star + 0.25 + 0.5, 0.5)

# plt.figure(figsize = (10,6))
# sns.histplot(x = "stars", data = df, palette = "viridis", bins = bins, shrink = 1)
# plt.title("Companies to rank")
# plt.xlabel("Rating")
# plt.ylabel("Number of companies")
# plt.xticks(np.arange(np.floor(min_star), np.ceil(max_star) + 0.5, 0.5))
# plt.tight_layout()
# plt.savefig("../outputs/companies_rating.png") # Saving results to file


# Visualization of a rating per state.
avg_state_rating = df.groupby("state")["stars"].mean()

# plt.figure(figsize = (12,6))
# sns.barplot(avg_state_rating, color = "darkblue")
# plt.title("State rating")
# plt.xlabel("States")
# plt.ylabel("Rating")
# plt.tight_layout()
# plt.savefig("../outputs/states_rating.png") # Saving results to file


# Visualization of top 10 categories based on number of companies.
df["category_list"] = df["categories"].dropna().apply(lambda x: [c.strip() for c in x.split(",")])
all_cat = df["category_list"].explode()
category_count = all_cat.value_counts()

# plt.figure(figsize = (14,6))
# sns.barplot(category_count.head(10), palette= "mako")
# plt.title("Top 10 categories based on number of companies")
# plt.xlabel("Categories")
# plt.ylabel("Number of companies")
# plt.tight_layout()
# plt.savefig("../outputs/categories_number_of_companies.png") # Saving results to file


# Visualization of review count vs. rating.
# plt.figure(figsize = (8,6))
# sns.scatterplot(x = "stars", y = "review_count", data = df, hue = "review_count", palette = "plasma", legend = False)
# plt.title("Rating vs. count of reviews")
# plt.xlabel("Rating")
# plt.ylabel("Count of reviews")
# plt.tight_layout()
# plt.savefig("../outputs/rating_review_count.png") # Saving results to file