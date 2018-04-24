from flask import Flask, jsonify

app = Flask(__name__)

roerder = True
verwarming = False
bierpomp = False

def temperatuur():
    return 25.88

@app.route("/")
def index():
    return (jsonify({'roerder': roerder, 'verwarming': verwarming, 'bierpomp': bierpomp, 'temperatuur': temperatuur()}))

@app.route("/roerder_aan", methods = ["POST"])
def roerder_aan():
    global roerder
    roerder = True
    return "OK"

@app.route("/roerder_uit", methods = ["POST"])
def roerder_uit():
    global roerder
    roerder = False
    return "OK"
