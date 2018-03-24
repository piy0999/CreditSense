var express = require('express'),
  path = require('path');

app = express();

app.set('port', 8080);

app.use('/bank', express.static('bank'));
app.use('/user', express.static('user'));
