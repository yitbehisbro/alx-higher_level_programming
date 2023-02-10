#!/usr/bin/node
const request = require('request');
const idNum = process.argv[2];

request.get(
  'http://swapi.co/api/films/${idNum}/',
  async (err, res, body) => {
    if (err) console.error(err);
    else {
      const film = JSON.parse(body);

      for (const character of film.characters) {
        request.get(character, (err, res, body) => {
          if (err) console.error(err);
          const char = JSON.parse(body);
          console.log(char.name);
        });
      }
    }
  }
);
