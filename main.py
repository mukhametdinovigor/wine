import os
import dotenv
import pandas
import datetime
import collections
from http.server import HTTPServer, SimpleHTTPRequestHandler
from jinja2 import Environment, FileSystemLoader, select_autoescape


dotenv.load_dotenv()
EXCEL_FILE_PATH = os.getenv('EXCEL_FILE_PATH')
env = Environment(
    loader=FileSystemLoader('.'),
    autoescape=select_autoescape(['html', 'xml'])
)


def get_excel_df(excel_path):
    excel_df = pandas.read_excel(excel_path, usecols=['Категория', 'Название', 'Сорт', 'Цена', 'Картинка', 'Акция'], na_values=' ', keep_default_na=False)
    return excel_df


def get_wines(excel_df):
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
    if (age % 10 == 1) and (age != 11) and (age != 111):
        text_age = f'{age} год'
    elif (age % 10 > 1) and (age % 10 < 5) and (age != 12) and (age != 13) and (age != 14):
        text_age = f'{age} года'
    else:
        text_age = f'{age} лет'
    return text_age


def main():
    winery_age = get_winery_age()
    excel_wines = get_excel_df(EXCEL_FILE_PATH)
    wines = get_wines(excel_wines)
    template = env.get_template('template.html')
    rendered_page = template.render(
        wines=wines,
        winery_age=winery_age
    )
    with open('index.html', 'w', encoding="utf8") as file:
        file.write(rendered_page)
    server = HTTPServer(('0.0.0.0', 8000), SimpleHTTPRequestHandler)
    server.serve_forever()


if __name__ == '__main__':
    main()
