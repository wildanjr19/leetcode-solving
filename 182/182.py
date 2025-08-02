import pandas as pd

def duplicate_emails(person: pd.DataFrame) -> pd.DataFrame:
    results = pd.DataFrame() # buat dataframe kosong

    # pilih baris dimana email sudah pernah muncul sebelumnya (duplikat) -> person.duplicated(subset=['email'])
    # lalu pilih hanya kolom email saja
    # [false, false, true] -> akan diambil yang true saja
    results = person.loc[person.duplicated(subset=['email']), ['email']]
    return results.drop_duplicates()