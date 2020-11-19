import aiohttp
from bs4 import BeautifulSoup
import re
import sqlite3
import asyncio
from typing import NamedTuple


class LcItem(NamedTuple):
    item_id: int
    name: str
    lists: int


async def update_items(num: int):
    conn = sqlite3.connect('listchallenge.db')
    while True:
        next_id = get_last_id(conn) + 1
        async with aiohttp.ClientSession() as session:
            await asyncio.gather(*[update_item(item_id, conn, session) for item_id in range(next_id, next_id + num)])
    conn.close()


async def update_item(item_id, conn, session):
    item = await get_item(item_id, session)
    print(item)
    save_item(item, conn)
    conn.commit()


async def get_item(item_id, session):
    r = await session.get('https://www.listchallenges.com/lists/containing-item/' + str(item_id))
    item = parse_item(item_id, await r.text())
    return item


def parse_item(item_id, content):
    soup = BeautifulSoup(content, 'html.parser')
    title = soup.title.string.strip()
    name = title.replace('Lists containing', '').replace('\'', '').strip()
    list_el = soup.find("div", string=re.compile("\d\slist"))
    lists = '0'
    if list_el is not None:
        lists = list_el.string.replace('lists', '').replace('list', '').strip()
        if "of" in lists:
            lists = lists.split("of")[1].strip()
        lists = lists.replace(',', '')
    return LcItem(item_id, name, lists)


def query_db(query, conn):
    c = conn.cursor()
    c.execute(query)
    return c


def save_item(item: LcItem, conn):
    query_db("INSERT INTO item VALUES (" + str(item.item_id) + ",'" + item.name + "'," + str(item.lists) + ")", conn)


def get_last_id(conn):
    c = query_db("SELECT MAX(id) FROM item", conn)
    return c.fetchone()[0]


loop = asyncio.get_event_loop()
loop.run_until_complete(update_items(5))
