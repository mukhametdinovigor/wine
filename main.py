import pandas
import datetime
import collections
from http.server import HTTPServer, SimpleHTTPRequestHandler
from jinja2 import Environment, FileSystemLoader, select_autoescape

env = Environment(
    loader=FileSystemLoader('.'),
    autoescape=select_autoescape(['html', 'xml'])
)

excel_data_df = pandas.read_excel('wine2.xlsx', usecols=['Категория', 'Название', 'Сорт', 'Цена', 'Картинка'], na_values=' ', keep_default_na=False)
wines = excel_data_df.to_dict(orient='records')
dict_of_wines = collections.defaultdict(list)
for i in range(len(wines)):
    dict_of_wines[wines[i]['Категория']].append(wines[i])
dict_of_wines = dict(sorted(dict_of_wines.items()))

foundation_year = 1920
now_year = datetime.datetime.now().year
age = now_year - foundation_year
text_age = ''

if (age % 10 == 1) and (age != 11) and (age != 111):
    text_age = f'{age} год'
elif (age % 10 > 1) and (age % 10 < 5) and (age != 12) and (age != 13) and (age != 14):
    text_age = f'{age} года'
else:
    text_age = f'{age} лет'


template = env.get_template('template.html')

rendered_page = template.render(
    dict_of_wines=dict_of_wines,
    text_age=text_age
)

with open('index.html', 'w', encoding="utf8") as file:
    file.write(rendered_page)

server = HTTPServer(('0.0.0.0', 8000), SimpleHTTPRequestHandler)
server.serve_forever()
