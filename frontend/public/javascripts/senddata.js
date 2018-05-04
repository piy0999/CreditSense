list = [
  'id',
  'dti',
  'inq_last_6mths',
  'open_acc',
  'emp_length_num',
  'revol_util',
  'grade',
  'payment_inc_ratio',
  'purpose',
  'delinq_2yrs_zero',
  'pub_rec_zero',
  'pub_rec',
  'short_emp',
  'home_ownership',
  'sub_grade_num',
  'last_major_derog_none',
  'last_delinq_none',
  'delinq_2yrs'
];

var obj = {
  id: 'A111112(4)',
  member_id: '1296599',
  loan_amnt: '5000',
  funded_amnt: '5000',
  funded_amnt_inv: '4975',
  term: ' 36 months',
  int_rate: '10.65',
  installment: '162.87',
  grade: 'B',
  sub_grade: 'B2',
  emp_title: '',
  emp_length: '10+ years',
  home_ownership: 'RENT',
  annual_inc: '24000',
  is_inc_v: 'Verified',
  issue_d: '20111201T000000',
  loan_status: 'Fully Paid',
  pymnt_plan: 'n',
  url: 'https://www.lendingclub.com/browse/loanDetail.action?loan_id=1077501',
  desc:
    '  Borrower added on 12/22/11 > I need to upgrade my business technologies.<br>',
  purpose: 'credit_card',
  title: 'Computer',
  zip_code: '860xx',
  addr_state: 'AZ',
  dti: '27.65',
  delinq_2yrs: '0',
  earliest_cr_line: '19850101T000000',
  inq_last_6mths: '1',
  mths_since_last_delinq: '',
  mths_since_last_record: '',
  open_acc: '3',
  pub_rec: '0',
  revol_bal: '13648',
  revol_util: '83.7',
  total_acc: '9',
  initial_list_status: 'f',
  out_prncp: '0',
  out_prncp_inv: '0',
  total_pymnt: '5861.07',
  total_pymnt_inv: '5831.78',
  total_rec_prncp: '5000',
  total_rec_int: '861.07',
  total_rec_late_fee: '0',
  recoveries: '0',
  collection_recovery_fee: '0',
  last_pymnt_d: '20150101T000000',
  last_pymnt_amnt: '171.62',
  next_pymnt_d: '',
  last_credit_pull_d: '20150101T000000',
  collections_12_mths_ex_med: '0',
  mths_since_last_major_derog: '',
  policy_code: '1',
  not_compliant: '0',
  status: 'Fully Paid',
  inactive_loans: '1',
  bad_loans: '0',
  emp_length_num: '11',
  grade_num: '5',
  sub_grade_num: '0.4',
  delinq_2yrs_zero: '1',
  pub_rec_zero: '1',
  collections_12_mths_zero: '1',
  short_emp: '0',
  payment_inc_ratio: '8.1435',
  final_d: '20141201T000000',
  last_delinq_none: '1',
  last_record_none: '1',
  last_major_derog_none: '1'
};

function getRandomInt(min, max) {
  return Math.floor(Math.random() * (max - min + 1)) + min;
}

window.onload = function() {
  var x = document.getElementById('submit');
  x.onclick = function() {
    var xhttp = new XMLHttpRequest();
    xhttp.open('POST', window.location.origin + ':5000/add_application', true);
    xhttp.setRequestHeader('Content-type', 'application/json');
    xhttp.responseType = 'json';
    for (var i = 0; i < list.length; i++) {
      key = list[i];
      document.getElementById(key).defaultValue = obj[key];
    }

    var data = {};
    //data['id'] = getRandomInt(1, 10000).toString();
    data['id'] = document.getElementById('id').value;
    for (var i = 1; i < list.length; i++) {
      var val = document.getElementById(list[i]).value;
      data[list[i]] = val;
    }
    console.log(JSON.stringify(data));
    var lamda = JSON.stringify(data);
    xhttp.send(lamda);

    xhttp.onload = function() {
      res = xhttp.response;
      if (res['status'] === 'success') {
        alert('Your application has been received');
      } else {
        alert('error');
      }
    };
  };
};
