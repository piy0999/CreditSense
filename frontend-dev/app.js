var express = require('express'),
  path = require('path');

app = express();

app.use(express.static('public'));
app.use('/bank', express.static('bank'));
app.use('/user', express.static('user'));

app.listen(80);
