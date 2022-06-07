"""
    Задание №2
    Передавать только адрес заглавной страницы а для извлечения
    адресов категорий использовать библиотеку beautifulsoup (или любой другой парсер по желанию)

"""
import aiohttp
from aiohttp import web
import asyncio
import requests
from lxml import html

# Параметры:
URL = "http://192.168.0.106:8002"
header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 '
                        '(KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36'}

# Тут сохраним все уникальные ссылки - теги a c сайта, включая вложенные.
LIST_URL = []

def request_to_site(url):
    """
    Функция рекурсивно вытаскивает с сайта все возможные ссылки, включая вложенные.
    Используется XPath
    """
    response = requests.get(url, headers=header)
    root = html.fromstring(response.text)
    result = root.xpath("//a/@href")  # тут можно добавить дополнительные значения атрибутов под конкретную задачу
    result = filter(lambda x: x not in ['#', ''], result)
    for i in result:
        if i not in LIST_URL:
            LIST_URL.append(i)
            request_to_site(f'{URL}{i}')


# Cоберем все ссылки
request_to_site(URL)
LIST_URL = list(map(lambda i: f'{URL}{i}', LIST_URL))  # сформируем полный путь


# 2. Сохраняем данные в файлы

async def save_section(url, save_file_name):
    print(f'Отправлен запрос: {url}')
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            if response.status == 200:
                txt = await response.text()
                with open(save_file_name, 'w', encoding='utf-8') as f:
                    print(txt, file=f)
                print(f'Для {url} cохранили файл {save_file_name}')
            else:
                print(f'Для {url} получен код {response.status}!')


func_comp = [save_section(url, f'task2-page-{i}.html')
             for i, url in enumerate(LIST_URL, start=1)]

loop = asyncio.get_event_loop()
loop.run_until_complete(asyncio.wait(func_comp))
