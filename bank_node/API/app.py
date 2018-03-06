from flask import Flask
from Savoir import Savoir
import json

app = Flask(__name__)

def connect():
    with open('credentials.json') as json_data:
        credentials = json.loads(json_data)
        json_data.close()
    rpcuser = credentials.rpcuser
    rpcpasswd = credentials.rpcpasswd
    rpchost = credentials.rpchost
    rpcport = credentials.rpcport
    chainname = credentials.chainname
    print(rpcuser, rpcpasswd, rpchost, rpcport, chainname)
    return Savoir(rpcuser, rpcpasswd, rpchost, rpcport, chainname)

multichain = connect()

@app.route('/')
def index():
    return 'This is the homepage'

@app.route('/add_loan_applicant_data',methods=['POST'])
def add_loan_applicat_data():
    if request.method == 'POST':
        data = request.form
        return multichain.getinfo()

@app.route('/get_all_applicant_data',methods=['GET'])
def get_all_applicant_data():
    if request.method == 'GET':
        return multichain.getinfo()

if __name__ == "__main__":
    print(multichain.getinfo())
    app.run(debug=True)
