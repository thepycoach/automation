import pandas as pd

df = pd.read_csv('fake_data.csv')
# print(df)

for i in range(0, len(df)):
    for column in df.columns:
        print(column)
        print(df.loc[i, column])
