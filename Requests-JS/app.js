const requests = require('requests');

requests('https://attendancesit00.herokuapp.com/api/getjson')
.on('data', function (chunk) {
  console.log(chunk)
})
.on('end', function (err) {
  if (err) return console.log('connection closed due to errors', err);

  console.log('end');
});