import pandas as pd
from datetime import datetime
from docxtpl import DocxTemplate

doc = DocxTemplate("template-manager-info.docx")
my_name = "Frank Andrade"
my_phone = "(123) 456-789"
my_email = "frank@gmail.com"
my_address = "123 Main Street, NY"
today_date = datetime.today().strftime("%d %b, %Y")

my_context = {'my_name': my_name, 'my_phone': my_phone, 'my_email': my_email, 'my_address': my_address,
              'today_date': today_date}

df = pd.read_csv('fake_data.csv')

for index, row in df.iterrows():
    context = {'hiring_manager_name': row['name'],
               'address': row['address'],
               'phone_number': row['phone_number'],
               'email': row['email'],
               'job_position': row['job'],
               'company_name': row['company']}

    context.update(my_context)

    doc.render(context)
    doc.save(f"generated_doc_{index}.docx")
