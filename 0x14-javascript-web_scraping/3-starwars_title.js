#!/usr/bin/node
const request = require('request');
const url = 'https://swapi-api.alx-tools.com/api/films/' + process.argv[2] + '/?format=json';
request(url, (error, response, body) => {
  if (error) console.log(error);
  console.log(JSON.parse(body).title);
});
