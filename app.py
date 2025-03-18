from flask import Flask, render_template, jsonify
import requests

app = Flask(__name__)

# Ganti dengan alamat API Raspberry Pi Pico W yang benar
PICO_W_API_URL = "http://192.168.56.150:5000/"

def ambil_data_telur():
    try:
        response = requests.get(PICO_W_API_URL)
        data = response.json()
        return data
    except requests.exceptions.RequestException as e:
        return {"error": str(e)}

@app.route('/')
def index():
    data = ambil_data_telur()
    return render_template("index.html", data=data)

@app.route('/api')
def api():
    data = ambil_data_telur()
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)
