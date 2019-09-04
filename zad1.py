import pandas as pd

test_csv = pd.read_csv('test.csv')
#print(test_csv.head())
print(type(test_csv['data_urodzenia'][9]))

def persons_born_after(df, date):
    all_dates = pd.to_datetime(pd.Series(df['data_urodzenia']), format='%d.%m.%Y')
    all_dates = all_dates[all_dates > date]
    return all_dates.count()
    
def womens_names(df):
    womens = df['imie'][df['imie'].map(lambda x: x[-1]=='a')]
    return set(womens)
   
   
date_after = '31.12.1999'
print("number of persons born after", date_after, "=", persons_born_after(test_csv, date_after))
print("all womans names:", womens_names(test_csv))