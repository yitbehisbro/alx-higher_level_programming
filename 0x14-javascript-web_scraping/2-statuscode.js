#!/usr/bin/node
require('request').get(process.argv[2])
  .on('response', function (response) {
    console.log('code: ' + response.statusCode);
  });
