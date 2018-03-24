$(document).ready(function() {
  var items = [
    { Name: 'Apple', Price: '80', Quantity: '3', Total: '240' },
    { Name: 'Orance', Price: '50', Quantity: '4', Total: '200' },
    { Name: 'Banana', Price: '20', Quantity: '8', Total: '160' },
    { Name: 'Cherry', Price: '250', Quantity: '10', Total: '2500' }
  ];

  $('#itemTemplate')
    .tmpl(items)
    .appendTo('#itemList tbody');
});
