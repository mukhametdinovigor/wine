import os
import dotenv
import pandas
import datetime
import collections
from http.server import HTTPServer, SimpleHTTPRequestHandler
from jinja2 import Environment, FileSystemLoader, select_autoescape


def get_wines(excel_path):
    excel_df = pandas.read_excel(excel_path, usecols=['Категория', 'Название', 'Сорт', 'Цена', 'Картинка', 'Акция'], na_values=' ', keep_default_na=False)
    excel_wines = excel_df.to_dict(orient='records')
    wines = collections.defaultdict(list)
    for wine in excel_wines:
        wines[wine['Категория']].append(wine)
    wines = dict(sorted(wines.items()))
    return wines


def get_winery_age():
    foundation_year = 1920
    now_year = datetime.datetime.now().year
    age = now_year - foundation_year
    if 5 <= age % 100 <= 20 or age % 10 == 0 or 5 <= age % 10 <= 9:
        text_age = f'{age} лет'
    elif 2 <= age % 10 <= 4:
        text_age = f'{age} года'
    else:
        text_age = f'{age} год'
    return text_age


if __name__ == '__main__':
    dotenv.load_dotenv()
    excel_file_path = os.getenv('EXCEL_FILE_PATH')
    env = Environment(
        loader=FileSystemLoader('.'),
        autoescape=select_autoescape(['html', 'xml'])
    )
    winery_age = get_winery_age()
    wines = get_wines(excel_file_path)
    template = env.get_template('template.html')
    rendered_page = template.render(
        wines=wines,
        winery_age=winery_age
    )
    with open('index.html', 'w', encoding="utf8") as file:
        file.write(rendered_page)
    server = HTTPServer(('0.0.0.0', 8000), SimpleHTTPRequestHandler)
    server.serve_forever()
