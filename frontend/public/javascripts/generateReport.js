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

submit_report_request = function() {
  var id = document.getElementById('hkid_val').value;
  console.log(id);
  var data = {};
  data['id'] = id;
  var json = JSON.stringify(data);
  if (id !== null) {
    $.ajax({
      type: 'POST',
      url: window.location.origin + ':5000/get_all_applications_by_id',
      headers: {
        'Content-Type': 'application/json'
      },
      dataType: 'json',
      data: json,
      success: function(applicant) {
        $('#form').hide();
        console.log(applicant[0].id);
        $('#score').html(applicant[applicant.length - 1].score);
        $('#score').css('text-align', 'center');
        $('#score').css('font-size', '60px');
        $('#score').css('font-weight', 'bold');
        $('#score').css('color', 'tomato');
        for (var i = 0; i < applicant.length; i++) {
          $('#itemList').append(
            '<tr><td>' +
              id +
              '</td><td>' +
              applicant[i]['home_ownership'] +
              '</td><td>' +
              applicant[i]['status'] +
              '</td><td>' +
              applicant[i]['score'] +
              '</td></tr>'
          );
        }
        $('#report').show();
      }
    });
  } else {
    alert('Please enter ID');
  }
};
