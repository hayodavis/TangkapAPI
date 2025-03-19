from flask import Flask, jsonify, render_template
import requests

app = Flask(__name__)

# Ganti dengan IP dari MicroDot Anda
ESP32_IP = "http://192.168.56.104:5000/"  # Sesuaikan dengan IP ESP32 di jaringan Anda

# Fungsi untuk mengambil data dari MicroDot
def get_sensor_data(endpoint):
    try:
        response = requests.get(f"{ESP32_IP}/api/{endpoint}")
        return response.json()
    except requests.exceptions.RequestException as e:
        return {"error": str(e)}

@app.route('/')
def index():
    return render_template('index.html')

# Route untuk mendapatkan semua data sensor
@app.route('/api/sensors', methods=['GET'])
def get_all_sensors():
    data = {
        "suhu": get_sensor_data("suhu"),
        "kelembapan": get_sensor_data("kelembapan"),
        "amonia": get_sensor_data("amonia"),
        "oksigen": get_sensor_data("oksigen"),
        "karbondioksida": get_sensor_data("karbondioksida"),
        "karbonmonoksida": get_sensor_data("karbonmonoksida")
    }
    return jsonify(data)

# Route untuk mendapatkan data suhu saja
@app.route('/api/suhu', methods=['GET'])
def get_suhu():
    return jsonify(get_sensor_data("suhu"))

# Jalankan server Flask
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=True)
