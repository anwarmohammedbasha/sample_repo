"""
Data Loading Module.

This module provides the 'load' function to connect to a PostgreSQL database
and handle the loading of transformed data. It includes logic to manage
data freshness by deleting existing records for the current processing date
before appending new data.
"""

from sqlalchemy import create_engine, text
from datetime import date


def load(data):
    """
        Connects to the PostgreSQL database to perform a two-step load operation
        on the 'waveworks_expense_summary' table.

        1. Deletes existing records that match the current ingestion date (upsert-like behavior).
        2. Appends the new, transformed data to the table.

        Args:
            data (pd.DataFrame): The transformed DataFrame ready for ingestion.
                                 It must contain an 'ingest_date' column.

        Returns:
            None

    """

    DATABASE_URL = "postgresql+psycopg2://postgres:admin@localhost:5432/test_db"
    engine = create_engine(DATABASE_URL)

    del_query = text("""
                     DELETE FROM waveworks_expense_summary
                     WHERE ingest_date = :ingest_date
                     """)

    ingest_date = date.today()

    with engine.begin() as conn:
        conn.execute(del_query, {"ingest_date": ingest_date})

    data.to_sql('waveworks_expense_summary', con=engine, index=False, if_exists='append')
