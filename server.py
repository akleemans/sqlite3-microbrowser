from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return 'Flask is running!'

@app.route('/data')
def names():
    data = {"names": ["John", "Jacob", "Julie", "Jennifer"]}
    return jsonify(data)

if __name__ == '__main__':
    # TODO discover db in directory
    # TODO analyze tables (.tables)
    # TODO run .schema for each table
    # TODO serve initial data
    app.run()
