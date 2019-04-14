'use strict';
const request = require('request');

// request
//   .get('http://attendancesit00.herokuapp.com/api/getjson')
//   .on('response', function(response) {
//     console.log(response.statusCode);
//     console.log(response.headers['content-type']);
//     console.log(error);
//   });


request('https://attendancesit00.herokuapp.com/api/getjson',(error, response, body)=>{
    console.log('Error : ',error);
    console.log('Response : ',response);
    console.log('Body : ',body);
});