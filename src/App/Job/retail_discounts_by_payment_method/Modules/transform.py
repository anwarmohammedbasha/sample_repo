def transform(data):
    filtered = data[data['discount_percentage'] > 0]

    grouped = (
        filtered
        .groupby(['payment_method', 'category'])['discount_percentage']
        .mean()
        .reset_index()
        .rename(columns={
            'discount_percentage': 'avg_discount_percentage'
        })
    )
    return grouped
