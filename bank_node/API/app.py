from flask import Flask
from flask import request
from flask import jsonify
from Savoir import Savoir
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
        finaldata = json.dumps(data)
        hexval = finaldata.encode('utf-8')
        curid = datetime.datetime.now()
        multichain.publish("strm1", str(curid), hexval.hex())
        return 'Success!'

@app.route('/get_all_applicant_data',methods=['GET'])
def get_all_applicant_data():
    if request.method == 'GET':
        data = multichain.liststreamitems("strm1",verbose=true)
        print(data)
        return jsonify(multichain.getinfo())

if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0', port=5000)
