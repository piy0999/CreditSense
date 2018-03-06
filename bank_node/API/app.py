from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'This is the homepage'

@app.route('/add_loan_applicant_data',methods=['POST'])
def add_loan_applicat_data():
    if request.method == 'POST':
        data = request.form

    return 'Success'

@app.route('/get_all_applicant_data',methods=['GET'])
def get_all_applicant_data():
    if request.method == 'GET':
        data =
    return 'choddiya tarun69 ko'
if __name__ == "__main__":
    app.run(debug=True)
