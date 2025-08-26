import pandas as pd

def sales_person(sales_person: pd.DataFrame, company: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    # merge order dan company
    merged_data = pd.merge(orders, company, on='com_id')

    # filter sales_person yang tidak memiliki order dari company 'RED'
    result = sales_person[~sales_person['sales_id'].isin(merged_data[merged_data['name'] == 'RED']['sales_id'])]
    return result