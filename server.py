import os
import sqlite3
from flask import Flask, request, g, jsonify, send_from_directory, render_template

app = Flask(__name__, static_folder='static')

def get_db_name():
    for f in os.listdir('.'):
        if f.find('.') >= 0 and f.split('.')[1] in ['sqlite', 'sqlite3', 'db3', 'db']:
            return f
    return 'DB not found'

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DB_NAME)
    return db

# query the db - from http://flask.pocoo.org/docs/0.10/patterns/sqlite3/
def query_db(query, args=(), one=False):
    cur = get_db().execute(query, args)
    rv = cur.fetchall()
    cur.close()
    get_db().commit()
    return (rv[0] if rv else None) if one else rv

def get_tables():
    return query_db("SELECT name FROM sqlite_master WHERE type='table'")

#@app.route('/static/<path:path>')
#def static(path):
#    return send_from_directory('static', path)

# init

DB_NAME = get_db_name()
print 'Database:', DB_NAME

# routes

@app.route('/')
def root():
    return app.send_static_file('index.html')

#@app.route('/<path:filename>')
#def send_file(filename):
#    return send_from_directory(app.static_folder, filename)

@app.route('/tables/')
def tables():
    tables = [{"label": t[0], "name": t[0], "content": "foo"} for t in get_tables()]

    return jsonify(results=tables) # jsonify(results=data)

@app.route('/data')
def names():
    data = {"names": ["John", "Jacob", "Julie", "Jennifer"]}
    return jsonify(data)

if __name__ == '__main__':
    # TODO run .schema for each table
    # TODO serve initial data
    app.run(debug=True)
