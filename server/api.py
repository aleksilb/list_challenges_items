import flask
import sqlite3
import os
from flask import jsonify
from flask_cors import CORS

current_dir = os.path.dirname(__file__)
app = flask.Flask(__name__)
CORS(app)


@app.route('/search/<search_string>', methods=['GET'])
def search_items(search_string):
    return item_query("SELECT * FROM item WHERE name LIKE '%" + search_string + "%' AND lists > 0 ORDER BY lists DESC")


@app.route('/top-items', methods=['GET'])
def get_top_items():
    return item_query("SELECT * FROM item ORDER BY lists DESC LIMIT 100")


def item_query(query):
    conn = sqlite3.connect(os.path.join(current_dir, 'listchallenge.db'))
    c = conn.cursor()
    c.execute(query)
    items = []
    for result in c.fetchall():
        items.append({"id": result[0], "name": result[1], "lists": result[2]})
    return jsonify(items)


if __name__ == "__main__":
    app.run()
