import pandas as pd


def largest_orders(orders: pd.DataFrame) -> pd.DataFrame:
    result = orders.groupby('customer_number').size().reset_index(name='total_orders')
    result = result[ result['total_orders'] == result['total_orders'].max()]
    result = result.drop(['total_orders'], axis=1)
    return result