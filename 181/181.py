import pandas as pd

"""
suffixes : memberikan nama tambahan pada kolom yang memiliki nama sama
left_on : kolom dari DataFrame pertama yang digunakan untuk penggabungan
right_on : kolom dari DataFrame kedua yang digunakan untuk penggabungan
"""
def find_employees(employee: pd.DataFrame) -> pd.DataFrame:
    results = pd.merge(employee, employee, left_on = 'managerId', right_on = 'id', suffixes = ('_employee', '_manager'))
    results2 = results[results['salary_employee'] > results['salary_manager']]
    results2.rename(columns = {'name_employee': 'Employee'}, inplace = True)

    return results2[['Employee']]