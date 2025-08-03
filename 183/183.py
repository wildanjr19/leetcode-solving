import pandas as pd

def find_customers(customers: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    data = customers[~customers['id'].isin(orders['customerId'])]
    '''
    customers['id'].isin(orders['customerId']) akan mengembalikan boolean
    yang menunjukkan apakah id customer ada di dalam customerId pada orders.

    Kemudian, kita menggunakan operator ~ untuk membalikkan boolean tersebut,
    sehingga kita mendapatkan customer yang id-nya tidak ada di dalam orders.
    '''
    
    data = data[['name']].rename(columns={'name' : 'Customers'})
    return data
