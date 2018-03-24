list = [
  'id',
  'loan_amnt',
  'funded_amnt',
  'funded_amnt_inv',
  'term',
  'int_rate',
  'installment',
  'grade',
  'sub_grade',
  'emp_length',
  'home_ownership',
  'annual_inc',
  'purpose',
  'dti',
  'delinq_2yrs',
  'inq_last_6mths',
  'open_acc',
  'revol_bal',
  'revol_util',
  'total_acc',
  'initial_list_status',
  'total_pymnt',
  'total_pymnt_inv',
  'total_rec_prncp',
  'total_rec_int',
  'last_pymnt_amnt'
];

var obj = {
  annual_inc: '24000',
  delinq_2yrs: '0',
  dti: '27.65',
  emp_length: '10+ years',
  funded_amnt: '5000',
  funded_amnt_inv: '4975',
  grade: 'B',
  home_ownership: 'RENT',
  id: '1077501',
  initial_list_status: 'f',
  inq_last_6mths: '1',
  installment: '162.87',
  int_rate: '10.65',
  last_pymnt_amnt: '171.62',
  loan_amnt: '5000',
  open_acc: '3',
  purpose: 'credit_card',
  revol_bal: '13648',
  revol_util: '83.7',
  sub_grade: 'B2',
  term: ' 36 months',
  total_acc: '9',
  total_pymnt: '5861.07',
  total_pymnt_inv: '5831.78',
  total_rec_int: '861.07',
  total_rec_prncp: '5000'
};

function getRandomInt(min, max) {
  return Math.floor(Math.random() * (max - min + 1)) + min;
}

window.onload = function() {
  var x = document.getElementById('submit');
  x.onclick = function() {
    var xhttp = new XMLHttpRequest();
    xhttp.open('POST', 'http://localhost:5000/add_application', true);
    xhttp.setRequestHeader('Content-type', 'application/json');
    for (i in obj) {
      document.getElementById(i).defaultValue = obj[i];
    }

    var data = {};
    data['id'] = getRandomInt(1, 10000).toString();
    for (var i = 1; i < list.length; i++) {
      var val = document.getElementById(list[i]).value;
      data[list[i]] = val;
    }
    console.log(data);
    var lamda = JSON.stringify(data);
    xhttp.send(lamda);

    xhttp.onload = function() {
      alert('Your application has been received');
    };
  };
};
