"""
Transformation module for the Pending Payments & Owed Amount ETL job.

Filters unpaid invoices and aggregates total pending amount, number of open
invoices, and payment status count for each customer.
"""

def transform(data):
    """
    Transform the merged sales/customer data to compute pending values.

    Parameters
    ----------
    data : pandas.DataFrame
        The merged DataFrame containing sales and customer information.

    Returns
    -------
    pandas.DataFrame
        Aggregated data with total pending amount and open invoice count.
    """

    # Filter unpaid invoices
    unpaid = data[data["payment_status"] != "Paid"]

    # Aggregate pending data per customer
    unpaid_data = (
        unpaid.groupby("customer_id")
        .agg(
            total_amount=("final_line_total_INR", "sum"),
            open_invoices=("invoice_id", "count"),
        )
        .reset_index()
    )

    print("Data Transformed")
    return unpaid_data
