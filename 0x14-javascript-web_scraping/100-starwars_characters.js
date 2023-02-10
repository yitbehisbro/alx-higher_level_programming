#!/usr/bin/node
const request = require('request');
const idNum = process.argv[2];

request('http://swapi.co/api/films/${idNum}/', function (err, response, body) {
  if (err == null) {
    const resp = JSON.parse(body);
    const characters = resp.characters;
    for (let i = 0; i < characters.length; i++) {
      request(characters[i], function (err, response, body) {
        if (err == null) {
          console.log(JSON.parse(body).name);
        }
      });
    }
  }
});
