import sys
from flask import Flask, request

app = Flask(__name__)
BASE = "/home/vagrant/tests/out/" + (sys.argv[1].zfill(3))
F = open(BASE + '/th.log', 'w')

@app.route("/ready", methods=["POST"])
def ready():
    req = request.get_json(silent=True)
    F.write(str(req))
    lock = open(BASE + "/thlock", 'w')
    lock.close()

@app.route("/error", methods=["POST"])
def error():
    req = request.get_json(silent=True)
    F.write(str(req))

@app.route("/status", methods=["POST"])
def status():
    req = request.get_json(silent=True)
    F.write(str(req))

@app.route("/done", methods=["POST"])
def done():
    req = request.get_json(silent=True)
    F.write(str(req))

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)
