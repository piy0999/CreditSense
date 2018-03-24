$(document).ready(function() {
  $.ajax({
    type: 'POST',
    url: 'http://localhost:5000',
    data: data,
    success: success,
    dataType: dataType
  });

  $('#itemTemplate')
    .tmpl(items)
    .appendTo('#itemList tbody');
});
