import sqlite3
from flask import Flask
from flask import g

DATABASE = './database.db'

app = Flask(__name__)

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)

    db.row_factory = sqlite3.Row

    return db

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db = db.close()

@app.route('/')
def index():
    cur = get_db().execute("SELECT nom FROM test")
    result = cur.fetchall()
    cur.close()
    for r in result:
        return r['nom']


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
