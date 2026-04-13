from flask import Flask, jsonify, request, send_from_directory
import json, os

app = Flask(__name__, static_folder='.')
DATA_FILE = 'gastos.json'

def read_data():
    if not os.path.exists(DATA_FILE):
        return {"gastos": []}
    with open(DATA_FILE, 'r') as f:
        return json.load(f)

def write_data(data):
    with open(DATA_FILE, 'w') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

@app.route('/')
def index():
    return send_from_directory('.', 'index.html')

@app.route('/futbol')
def futbol():
    return send_from_directory('.', 'futbol.html')

@app.route('/api/gastos', methods=['GET'])
def get_gastos():
    return jsonify(read_data())

@app.route('/api/gastos', methods=['POST'])
def save_gastos():
    data = request.get_json()
    write_data(data)
    return jsonify({"ok": True})

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
