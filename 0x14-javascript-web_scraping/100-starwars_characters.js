#!/usr/bin/node

const request = require('request');

if (process.argv.length !== 3) {
  console.error('Usage: node printMovieCharacters.js <movie_id>');
  process.exit(1);
}

const movieId = process.argv[2];
const apiUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

request(apiUrl, function (error, response, body) {
  if (error) {
    console.error(error);
    return;
  }

  if (response.statusCode !== 200) {
    console.error('Request failed with status code:', response.statusCode);
    return;
  }

  try {
    const movieData = JSON.parse(body);
    const movieCharacters = movieData.characters;

    movieCharacters.forEach(characterUrl => {
      request(characterUrl, function (charError, charResponse, charBody) {
        if (charError) {
          console.error(charError);
          return;
        }

        if (charResponse.statusCode !== 200) {
          console.error('Request failed with status code:', charResponse.statusCode);
          return;
        }

        const characterData = JSON.parse(charBody);
        console.log(characterData.name);
      });
    });
  } catch (parseError) {
    console.error(parseError);
  }
});
