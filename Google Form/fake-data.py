import pandas as pd
from faker import Faker

# create fake data: name, mail, address
fake = Faker()
profiles = [fake.profile() for i in range(10)]

# store fake data in Pandas
df = pd.DataFrame(profiles)
df = df[['name', 'mail', 'address']]

# create fake data: phone number, comment
numbers = [fake.phone_number() for i in range(0, 10)]
comment = '-'

# store fake data in Pandas
df['Phone number'] = numbers
df['Comments'] = comment

# change column names
df.rename(columns={'name': 'Name', 'mail': 'Email', 'address': 'Address'}, inplace=True)

# export data to csv file
df.to_csv('fake_data.csv', index=False)
