var express = require('express');
var path = require('path');
var bodyParser = require('body-parser');
var cors = require('cors');
var passport = require('passport');

// routers
var authRouter = require('./routes/auth');
var indexRouter = require('./routes/index');
var newsRouter = require('./routes/news');

var app = express();

// view engine setup
app.set('views', path.join(__dirname, '../client/build/'));
app.set('view engine', 'jade');
app.use('/static', express.static(path.join(__dirname, '../client/build/static/')));

app.use(bodyParser.json());
app.use(cors());

var config = require('./config/config.json');
require('./models/main.js').connect(config.mongoDbUri);

//load passport strategies
app.use(passport.initialize());
var localSignUpStrategy = require('./passport/signup_passport');
var localLoginStrategy = require('./passport/login_passport');
passport.use('local-signup', localSignUpStrategy);
passport.use('local-login', localLoginStrategy);

// check authentication
const authChecker = require('./middleware/auth_checker');
app.use('/news', authChecker);

app.use('/', indexRouter);
app.use('/auth', authRouter);
app.use('/news', newsRouter);

// catch 404 and forward to error handler
app.use(function(req, res, next) {
  res.status(404);
});

module.exports = app;
