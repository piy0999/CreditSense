window.onload = function() {
  var x = document.getElementById('submit');
  x.onclick = function() {
    var xhttp = new XMLHttpRequest();
    xhttp.open(
      'POST',
      'http://52.230.125.236:5000/add_loan_applicant_data',
      true
    );
    xhttp.setRequestHeader('Content-type', 'application/json');
    var id = document.getElementById('hkid_val').value;
    var empl_yrs = document.getElementById('empl_yrs').value;
    var ownership = document.getElementById('ownership').value;
    var type = document.getElementById('type').value;
    var data = {};
    data['id'] = id;
    data['empl_yrs'] = empl_yrs;
    data['ownership'] = ownership;
    data['type'] = type;
    console.log(data);
    var lamda = JSON.stringify(data);
    xhttp.send(lamda);

    xhttp.onload = function() {
      alert('Your application has been received');
    };
  };
};
