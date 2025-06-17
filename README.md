**Project status**: Completed - closed.

This project is a data analysis of a publicly available data from: 
https://www.kaggle.com/datasets/yelp-dataset/yelp-dataset


The project consists of cleaning data, data analysis and data modeling by using Pandas, Matplotlib, Seaborn or Numpy Python libraries as well as SQL queries. All data was pushed and managed on Github via Git bash.


**Structure of the project is as follows:**
- ".gitignore" : Created to ignore raw data from upload. They exceed 50 mb and are too large.

_Folder "data":_
- "cleaned_data.csv" : Outcome of data cleaning. File used for further analysis.
- "companies_data.db" : File generated out of 'cleaned_data.csv' to ask SQL queries.


_Folder "notebooks":_
- "data_cleaning.py" : Python file created to read, clean and save new data file.
- "data_exploration.py" : Python file used to run exploration of data. It covers the same queries as 'sql_queries.py' but with use of Pandas module.
- "sql_queries.py" : Python file used to generate 'companies_data.db' and run exploratory queries by using SQL(sqlite3 module). It covers the same queries as 'data_exploration.py'.


_Folder "outputs":_
- "categories_number_of_companies.png" : Bar chart gradient-shaded with top 10 categories based on number of companies.
- "companies_rating.png" : Bar chart with rank of companies vs volume.
- "rating_review_count.png" : Scatter plot with rank of companies vs. volume.
- "states_rating" : Bar chart with sum of rating per a state.