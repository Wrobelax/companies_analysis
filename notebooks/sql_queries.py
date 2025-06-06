"""
Script for creating SQL database out of generated cleaned_data.csv.
"""

import pandas as pd
import sqlite3

# Importing file with cleaned data.
url = "../data/cleaned_data.csv"
df = pd.read_csv(url)

conn = sqlite3.connect("../data/companies_data.db")
# df.to_sql("companies", conn, if_exists = "replace", index = False) # Uncomment to generate database.



"""SQL queries"""
# Check basic structure.
query_1 = """
SELECT *
FROM companies
LIMIT 10;
"""

# Dividing categories of companies and checking how many are in each category.
query_2 = """
SELECT
    TRIM(SUBSTR(T.categories, INSTR(T.categories || ',', S.value), INSTR(SUBSTR(T.categories || ',', INSTR(T.categories || ',', S.value)), ',') -1)) AS category_div,
    COUNT(DISTINCT T.business_id) AS companies_number
FROM
    companies AS T,
    (SELECT 1 AS value UNION ALL SELECT 2 UNION ALL SELECT 3 UNION ALL SELECT 4 UNION ALL SELECT 5 UNION ALL SELECT 6 UNION ALL SELECT 7 UNION ALL SELECT 8 UNION ALL SELECT 9 UNION ALL SELECT 10) AS S
WHERE
    SUBSTR(T.categories || ',', S.value) != '' AND INSTR(SUBSTR(T.categories || ',', S.value), ',') > 0
GROUP BY
    categories
ORDER BY
    companies_number DESC;
"""


# Checking average rating divided for each city.
query_3 = """
SELECT city, AVG(stars)
FROM companies
GROUP BY city
ORDER BY AVG(stars) DESC;
"""


# Checking top 10 companies with the highest rate and review_count greater than 50.
query_4 = """
SELECT name, review_count, stars
FROM companies
WHERE review_count > 50
ORDER BY stars DESC
LIMIT 10
"""


# Checking correlation between number of opinions and stars.
query_5 = """
SELECT name, review_count, stars
FROM companies
ORDER BY review_count DESC
"""


# Companies with the lowest rate and number of opinions - unfiltered.
query_6 = """
SELECT name, review_count, stars
FROM companies
ORDER BY stars
LIMIT 10
"""


# Companies with the lowest rate and number of opinions - review_count > 50.
query_7 = """
SELECT name, review_count, stars
FROM companies
WHERE review_count > 50
ORDER BY stars
LIMIT 10
"""


# Checking SQL query.
result = pd.read_sql_query(query_X, conn) # set proper query number to see results from the base.
print(result)