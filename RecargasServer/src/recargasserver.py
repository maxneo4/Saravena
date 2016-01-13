from flask import Flask, request
import data_users
import data_providers
import data_movements

app = Flask(__name__)

@app.route("/")
def home_page():
    return "HOME PAGE"

@app.route("/users")
def users():
    return data_users.get_all()

@app.route("/providers")
def providers():
    return data_providers.get_all()

@app.route("/movements")
def movements():
    return data_movements.get_all()

@app.route('/movement', methods=['POST'])
def add_movement():
    return data_movements.insert(request.json)    

if __name__ == "__main__":
    app.run()
