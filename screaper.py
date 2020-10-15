import requests
from bs4 import BeautifulSoup
import re
import sqlite3
from typing import NamedTuple

class LcItem(NamedTuple):
    id: int
    name: str
    lists: int

def update_items(num:int):
    conn = sqlite3.connect('../Database/listchallenge.db')
    next_id = get_last_id(conn) + 1
    if num == 0:
        while True:
            update_item(next_id, conn)
            next_id = next_id + 1
            conn.commit()
    else:
        for id in range(next_id, next_id + num):
            update_item(id, conn)
            conn.commit()
    conn.close()

def update_item(id, conn):
    item = get_item(id)
    save_item(item, conn)
    print(item)

def get_item(id):
    r = requests.get('https://www.listchallenges.com/lists/containing-item/' + str(id))
    soup = BeautifulSoup(r.content, 'html.parser')
    title = soup.title.string.strip()
    name = title.replace('Lists containing','').replace('\'','').strip()
    list_el = soup.find("div", string = re.compile("\d\slist"))
    lists = '0'
    if list_el is not None:
        lists = list_el.string.replace('lists','').replace('list','').strip()
        if "of" in lists:
            lists = lists.split("of")[1].strip()
        lists = lists.replace(',','')
    return LcItem(id, name, lists)

def save_item(item:LcItem, conn):
    c = conn.cursor()
    query = "INSERT INTO item VALUES ("+ str(item.id) +",'"+item.name+"',"+str(item.lists)+")"
    c.execute(query)

def get_last_id(conn):
    c = conn.cursor()
    c.execute("SELECT MAX(id) FROM item")
    return c.fetchone()[0]

update_items(0)