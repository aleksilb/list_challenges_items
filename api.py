import flask
import sqlite3
from flask import jsonify
from flask_cors import CORS

app = flask.Flask(__name__)
app.config["DEBUG"] = True
CORS(app)

@app.route('/search/<search_string>', methods=['GET'])
def search_items(search_string):
    return item_query("SELECT * FROM item WHERE name LIKE '%" + search_string + "%' AND lists > 0 ORDER BY lists DESC")

@app.route('/top-items', methods=['GET'])
def get_top_items():
    return item_query("SELECT * FROM item ORDER BY lists DESC LIMIT 100")

def item_query(query):
    conn = sqlite3.connect('../Database/listchallenge.db')
    c = conn.cursor()
    c.execute(query)
    items = []
    for result in c.fetchall():
        items.append({"id":result[0],"name":result[1],"lists":result[2]})
    return jsonify(items)

app.run()