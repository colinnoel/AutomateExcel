import pandas as pd
import ssl

ssl._create_default_https_context = ssl._create_unverified_context

# The webpage URL whose table we want to extract
url = "https://www.geeksforgeeks.org/extended-operators-in-relational-algebra/"

# Assign the table data to a Pandas dataframe
table = pd.read_html(url)[0]

table.to_excel("data.xlsx")