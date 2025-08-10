import pandas as pd

def employee_bonus(employee: pd.DataFrame, bonus: pd.DataFrame) -> pd.DataFrame:
    # gabungkan dua dataframe
    result = pd.merge(employee, bonus, on='empId', how='left')

    # cari bonus yang kurang dari 1000 dan ikutkan yang null
    result = result[(result['bonus'] < 1000) | (result['bonus'].isna())] 

    # kembalikan hanya nama dan bonus
    return result[['name', 'bonus']]
