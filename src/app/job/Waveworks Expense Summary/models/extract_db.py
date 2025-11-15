"""
Database Extraction Module.

This module contains a utility function to connect to a SQLite database
using SQLAlchemy and extract data from a specified table into a pandas DataFrame.
"""

import pandas as pd
from sqlalchemy import create_engine, text


def extract_db(path: str, table: str) -> pd.DataFrame:
    """
    Connects to a SQLite database file and executes a simple SELECT query.

    Uses SQLAlchemy's create_engine and pandas' read_sql for efficient data loading.

    Args:
        path (str): The absolute or relative file path to the SQLite database
        table (str): The name of the table to select data from (e.g., 'daily_expenses').

    Returns:
        pd.DataFrame: A pandas DataFrame containing all records from the specified table.
                      Returns an empty DataFrame if the connection fails or the table is empty.
    """

    DATABASE_URL = f"sqlite:///{path}"
    engine = create_engine(DATABASE_URL)
    query = text(f"SELECT * FROM {table}")
    df = pd.read_sql(query, engine)

    return df