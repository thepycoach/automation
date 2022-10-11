import pandas as pd
from datetime import datetime
from docxtpl import DocxTemplate

doc = DocxTemplate("plantilla-rrhh-info.docx")
mi_nombre = "Frank Andrade"
mi_numero = "(123) 456-789"
mi_correo = "frank@gmail.com"
mi_direccion = "123 Main Street, NY"
fecha_hoy = datetime.today().strftime("%d %b, %Y")

my_context = {'mi_nombre': mi_nombre, 'mi_numero': mi_numero, 'mi_correo': mi_correo,
              'mi_direccion': mi_direccion, 'fecha_hoy': fecha_hoy}

df = pd.read_csv('fake_data.csv')

for index, fila in df.iterrows():
    context = {'nombre_persona_rrhh': fila['name'],
               'direccion': fila['address'],
               'numero_telefono': fila['phone_number'],
               'correo': fila['email'],
               'puesto_trabajo': fila['job'],
               'nombre_empresa': fila['company']}

    context.update(my_context)

    doc.render(context)
    doc.save(f"doc_generado_{index}.docx")