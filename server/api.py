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
    return do_item_query("SELECT * FROM item WHERE name LIKE '%" + search_string + "%' AND lists > 0 ORDER BY lists DESC")


@app.route('/top-items', methods=['GET'])
def get_top_items():
    return do_item_query("SELECT * FROM item ORDER BY lists DESC LIMIT 100")


@app.route('/items/<item_id>/check', methods=['PUT'])
def check_item(item_id):
    do_query("UPDATE item SET checked = TRUE WHERE id = " + item_id)
    return "{}"


def do_item_query(query):
    results = do_query(query)
    items = []
    for result in results:
        items.append({"id": result[0], "name": result[1], "lists": result[2]})
    return jsonify(items)


def do_query(query):
    connection = sqlite3.connect(os.path.join(current_dir, 'listchallenge.db'))
    cursor = connection.cursor()
    cursor.execute(query)
    results = cursor.fetchall()
    connection.commit()
    connection.close()
    return results


if __name__ == "__main__":
    app.run()
