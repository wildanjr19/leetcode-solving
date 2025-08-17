import pandas as pd

def biggest_single_number(my_numbers: pd.DataFrame) -> pd.DataFrame:
    result = my_numbers.groupby('num').size().reset_index(name='count')
    result = result[result['count'] == 1]
    
    # jika tidak ada yang muncul sekali, kembalikan null
    if result.empty:
        return pd.DataFrame({'num': [None]})
    
    # urutkan num
    result = result.sort_values(by='num', ascending=False)
    # hapus kolom count
    result = result.drop(columns='count')
    return result.head(1)