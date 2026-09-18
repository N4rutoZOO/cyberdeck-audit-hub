from flask import Flask, jsonify, render_template, request
from pathlib import Path
import yaml

app = Flask(__name__)
CONFIG = Path(__file__).parent / 'config' / 'tools.yaml'

def load_tools():
    with CONFIG.open(encoding='utf-8') as f:
        return yaml.safe_load(f).get('tools', [])

@app.get('/')
def index():
    return render_template('index.html', tools=load_tools())

@app.get('/api/tools')
def tools():
    return jsonify(load_tools())

@app.post('/api/validate-target')
def validate_target():
    data = request.get_json(silent=True) or {}
    ssid = (data.get('ssid') or '').strip()
    bssid = (data.get('bssid') or '').strip().upper()
    valid_bssid = len(bssid) == 17 and all(c in '0123456789ABCDEF:' for c in bssid)
    return jsonify({'allowed': bool(ssid) and valid_bssid, 'reason': 'SSID et BSSID requis'}), 200

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=False)
