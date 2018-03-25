old_report_request = function() {
  var x = document.getElementById('submit');
  x.onclick = function() {
    var xhttp = new XMLHttpRequest();
    xhttp.open('POST', 'http://52.187.163.79:9685', true);
    xhttp.setRequestHeader('Content-type', 'application/json');
    var val = document.getElementById('hkid_val').value;
    console.log(val);
    var data = {};
    data['id'] = val;
    console.log(data);
    var lamda = JSON.stringify(data);
    xhttp.send(lamda);

    xhttp.onload = function() {
      window.location.href = 'scoredash/index.html';
    };
  };
};

let id;

submit_report_request = function() {
  id = document.getElementById('hkid_val').value;
  var data = {};
  data['id'] = id;
  var json = JSON.stringify(data);
  if (!id) {
    $.ajax({
      type: 'POST',
      url: 'http://localhost:5000/get_application_by_id',
      headers: {
        'Content-Type': 'application/json'
      },
      dataType: 'json',
      data: json,
      success: function(returndata) {
        $('#form').hide();
        var applicant = returndata;
        $('#score').html(applicant['score']);
        var tableObject = [];
        applicant.forEach(function(item, index) {
          for (var key in item) {
            if (
              key === 'id' ||
              key === 'loan_amnt' ||
              key === 'score' ||
              key === 'status'
            ) {
              var temp = {};
              temp[key] = item[key];
            }
            tableObject.push(temp);
          }
        });
        $('#itemTemplate')
          .tmpl(tableObject)
          .appendTo('#itemList tbody');
        $('#report').show();
      }
    });
  } else {
    alert('Please enter ID');
  }
};
