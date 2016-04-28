from flask import Flask, request, jsonify, send_from_directory, render_template

app = Flask(__name__, static_folder='static')

#@app.route('/static/<path:path>')
#def static(path):
#    return send_from_directory('static', path)

@app.route('/')
def root():
    return app.send_static_file('index.html')

#@app.route('/<path:filename>')
#def send_file(filename):
#    return send_from_directory(app.static_folder, filename)

@app.route('/tables/')
def tables():
    data = [{"label": "Overview", "name": "Overview", "content": "foo"},
    {"label": "Table 1", "name": "table1", "content": "bar"}]
    return jsonify(results=data)

@app.route('/data')
def names():
    data = {"names": ["John", "Jacob", "Julie", "Jennifer"]}
    return jsonify(data)

if __name__ == '__main__':
    # TODO discover db in directory
    # TODO analyze tables (.tables)
    # TODO run .schema for each table
    # TODO serve initial data
    app.run(debug=True)
