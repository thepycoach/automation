import jinja2
import pdfkit
from datetime import datetime

my_name = "Frank Andrade"
item1 = "TV"
item2 = "Mueble"
item3 = "Lavadora"
today_date = datetime.today().strftime("%d %b, %Y")

context = {'my_name': my_name, 'item1': item1, 'item2': item2, 'item3': item3,
           'today_date': today_date}

template_loader = jinja2.FileSystemLoader('./')
template_env = jinja2.Environment(loader=template_loader)

html_template = 'plantilla-basica.html.html'
template = template_env.get_template(html_template)
output_text = template.render(context)

config = pdfkit.configuration(wkhtmltopdf='/usr/local/bin/wkhtmltopdf')
output_pdf = 'pdf_generado.pdf'
pdfkit.from_string(output_text, output_pdf, configuration=config, css='style.css')
