from flask import Flask
from flask import request
from flask import jsonify
from Savoir import Savoir
import requests
import json
import time
import datetime

app = Flask(__name__)

def connect():
    with open('credentials.json') as json_data:
        credentials = json.load(json_data)
        json_data.close()
    rpcuser = credentials["rpcuser"]
    rpcpasswd = credentials["rpcpasswd"]
    rpchost = credentials["rpchost"]
    rpcport = credentials["rpcport"]
    chainname = credentials["chainname"]
    return Savoir(rpcuser, rpcpasswd, rpchost, rpcport, chainname)

multichain = connect()

@app.route('/')
def index():
    return 'This is the homepage'

@app.route('/add_loan_applicant_data',methods=['POST'])
def add_loan_applicat_data():
    if request.method == 'POST':
        data = request.get_json()
        print(data)
        r = requests.post('http://40.65.176.117:5000/apply_loan', json=jsonify(data))
        if (r.status_code == 200):
            return jsonify({"status":"success"})
        else:
            return jsonify({"status":"failure"})

@app.route('/get_all_applicant_data',methods=['GET'])
def get_all_applicant_data():
    if request.method == 'GET':
        multichain.subscribe("strm1")
        data = multichain.liststreamitems("strm1")
        print(data)
        response = []
        for x in data:
            obj = json.loads(bytearray.fromhex(x['data']).decode())
            print(obj)
            response.append(obj)

        return jsonify(response)

if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0', port=5000)
