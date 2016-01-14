from flask import Flask, request
import data_clients
import data_providers
import data_movements
from business.movements import process_movement

app = Flask(__name__)

@app.route("/")
def home_page():
    return "HOME PAGE"

@app.route("/clients")
def users():
    return data_clients.get_all()

@app.route("/providers")
def providers():
    return data_providers.get_all()

@app.route("/movements")
def movements():
    return data_movements.get_all()

@app.route('/movement', methods=['POST'])
def add_movement():
    return process_movement(request.json)

if __name__ == "__main__":
    app.run()
