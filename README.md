# Новое русское вино

Сайт магазина авторского вина "Новое русское вино".

## Запуск

- Скачайте код
- Запустите сайт командой `python3 main.py`
- Перейдите на сайт по адресу [http://127.0.0.1:8000](http://127.0.0.1:8000).

Для того чтобы на сайте отображались карточки с вином из таблицы Excel, необходимо создать файл `.env` и записать в него переменную окружения
`EXCEL_FILE_PATH` и присвоить ей  путь к файлу `wine.xlsx`

Пример: `EXCEL_FILE_PATH='C:\Users\User\Desktop\projects\wine\wine.xlsx'`


Редактировать карточки с товаром можно в файле wine.xslx, последовательно заполните все необходимые ячейки

### Карточки с вином. Пример:

| Категория     | Название      | Сорт           | Цена          | Картинка        | Акция                |
| ------------- |:-------------:| -------------  |:-------------:| -------------   |:-------------:       |
| Белые вина    | Белая леди    | Дамский пальчик| 399           | belaya_ledi.png | Выгодное предложение |
| Красные вина  | Хванчкара     | Александраули  | 550           | hvanchkara.png  |                      |
| Напитки       | Чача          |                | 299           | chacha.png      |                      |
|               |               |                |               |                 |                      |



## Цели проекта

Код написан в учебных целях — это урок в курсе по Python и веб-разработке на сайте [Devman](https://dvmn.org).
