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


# Visualizing linear regression for stars vs. review_count.
df_sorted = df.sort_values(by = "stars")
X = df_sorted[["stars"]]
Y = df_sorted["review_count"]
lr = LinearRegression()
lr.fit(X, Y)

X_range = np.linspace(X.min(), X.max(), 100).reshape(-1, 1)
Y_pred_line = lr.predict(X_range)

# plt.figure(figsize = (10,6))
# sns.scatterplot(x = "stars", y = "review_count", data = df_sorted, color = "blue", alpha = 0.7, s = 80)
# plt.plot(X_range, Y_pred_line, color = "red", linestyle = "-", linewidth = 2, label = "Regression line")
# plt.title("Linear regression: Review Count vs. Rating")
# plt.xlabel("Rating")
# plt.ylabel("Review count")
# plt.legend()
# plt.grid(True, linestyle = "--", alpha = 0.6)
# plt.tight_layout()
# plt.show()
# plt.savefig("../outputs/linear_regression.png") # Saving results to file


# Visualizing polynomial regression (degree = 2) as linear showed flat.
A = df_sorted["stars"].values.reshape(-1, 1)
B = df_sorted["review_count"].values
A_range = np.linspace(A.min(), A.max(), 200).reshape(-1, 1)

poly_reg = PolynomialFeatures(degree = 3)
A_poly = poly_reg.transform(A_range)

model_poly = LinearRegression()
model_poly.fit(A_poly, B)
B_pred_poly = model_poly.predict(A_poly)

plt.figure(figsize = (12, 7))
sns.scatterplot(x = "stars", y = "review_count", data = df_sorted, color = "purple", alpha = 0.7, s = 80)
plt.plot(A_poly, B_pred_poly, color = "blue", linestyle = "-", linewidth = 2, label = "Polynomial regression 2 degree")

plt.title("Polynomial regression 2 degree")
plt.xlabel("Rating")
plt.ylabel("Review Count")
plt.legend()
plt.grid(True, linestyle='--', alpha=0.6)
plt.tight_layout()
plt.show()