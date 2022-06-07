"""
    Задание №1
    По списку url реализовать загрузку страниц категорий с нашего проекта
    и сохранение их в файлы.  Использовать asyncio и aiohttp.
"""
import aiohttp
from aiohttp import web
import asyncio


URL = "http://192.168.0.106:8002/catalogs/"
list_categoties = [f"{URL}{i}/" for i in range(1, 6)]


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


func_comp = [save_section(url, f'section-{i}.html')
             for i, url in enumerate(list_categoties, start=1)]

loop = asyncio.get_event_loop()
loop.run_until_complete(asyncio.wait(func_comp))
