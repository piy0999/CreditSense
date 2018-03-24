from flask import Flask, request, jsonify
from Savoir import Savoir
import requests, json, time, datetime, hashlib

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

def hash(unhashed):
    byte_id = unhashed.encode('utf-8')
    hash_object = hashlib.sha256(byte_id)
    hashed = hash_object.hexdigest()
    return hashed

def all_applications():
    multichain.subscribe("strm1")
    data = multichain.liststreamitems("strm1")
    applications = {}
    for application in data:
        application = json.loads(bytearray.fromhex(x['data']).decode())
        applications[application['id']] = application
    return applications

def get_application_by_id(given_id):
    data = all_applications()
    if hash(given_id) in data:
        return data[hash(given_id)]
    else:
        return None

@app.route('/')
def index():
    return 'This is the creditsense consortium.\n'

@app.route('/status',methods=['GET'])
def status():
    data = list(all_applications().values())

    total_applications = len(data)
    pending_applications = 0
    approved_applications = 0
    disapproved_applications = 0

    for application in data:
        if application['status'] == 'pending':
            pending_applications += 1
        elif application['status'] == 'approved':
            approved_applications += 1
        elif application['status'] == 'disapproved':
            disapprove_applications += 1

    return jsonify({
        'total_applications':total_applications,
        'pending_applications':pending_applications,
        'approved_applications':approved_applications,
        'disapproved_applications':disapproved_applications
    })

@app.route('/all_applications',methods=['GET'])
def wrapper_all_applications():
    jsonify(list(all_applications().values()))

@app.route('/pending_applications',methods=['GET'])
def pending_applications():
    applications = list(all_applications().values())
    pending_applications = []
    for application in applications:
        if application['status'] == 'pending':
            pending_applications.append(application)
    return jsonify(pending_applications)

@app.route('/add_application',methods=['POST'])
def add_application():
    required_fields = ['id','loan_amnt', 'funded_amnt', 'funded_amnt_inv', 'term', 'int_rate',
                'installment', 'grade', 'sub_grade', 'emp_length', 'home_ownership',
                'annual_inc', 'verification_status', 'purpose', 'dti',
                'delinq_2yrs', 'inq_last_6mths', 'open_acc', 'revol_bal', 'revol_util',
                'total_acc', 'initial_list_status', 'total_pymnt', 'total_pymnt_inv',
                'total_rec_prncp', 'total_rec_int', 'last_pymnt_amnt',
                'total_rev_hi_lim', 'loan_status_coded']
    data = request.get_json()
    if all(field in data for field in required_fields):
        data['id'] = hash(id)
        data['status'] = 'pending'
        r = requests.post('http://40.65.176.117:5000/apply_loan', json=data)
        if (r.status_code == 200):
            return jsonify({"status":"success"})
        else:
            return jsonify({"status":"failure"})
    else:
        return jsonify({"status":"required params not provided"})

@app.route('/get_application_by_id',methods=['GET'])
def wrapper_get_application_by_id():
    return jsonify(get_application_by_id(given_id))

@app.route('/update_application',methods=['POST'])
def update_application():
    data = request.get_json()
    applicant_data = get_application_by_id(data['id'])
    if applicant_data is not None:
        applicant_data['status'] = data['status']
        r = requests.post('http://40.65.176.117:5000/apply_loan', json=applicant_data)
        if (r.status_code == 200):
            return jsonify({"status":"success"})
        else:
            return jsonify({"status":"failure"})
    else:
        return jsonify({"status":"applicant doesn't exist"})

if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0', port=5000)
