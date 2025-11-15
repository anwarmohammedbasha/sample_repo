"""
Expense Summary ETL Job

This script orchestrates the full ETL workflow for generating a category-wise
expense summary. It extracts raw daily expenses, applies transformations such as
category grouping and summarization, and finally loads the processed results
into an output CSV file.
"""

from models import extract, transform, load

data = extract(expenses_path="data/coffee-shop/daily_expenses.csv")
transformed_data = transform(data)
load(transformed_data)
