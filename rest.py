from flask import Flask, request
app = Flask(__name__)
import json
import logistic_regression
from subprocess import call

@app.route('/', methods = ["POST"])
def query_example():
	data = request.get_json()
	dump_data = json.dumps(data)
	dict_json = json.loads(dump_data)
	hkid = dict_json['id']
	f = open("id.txt","w+")
	f.write(hkid)
	f.close()
	call(["python3", "logistic_regression.py"])
	return 'Json received'

app.run(host='0.0.0.0', port= 9685)    