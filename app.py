import sqlite3
from flask import Flask
from flask import g
from os import environ

app = Flask(__name__)
app.config.from_object(environ.get('app_setting'))

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        full_name = '/'.join((app.config.get("DB_PATH"), app.config.get('DB_NAME')))
        db = g._database = sqlite3.connect(full_name)

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
