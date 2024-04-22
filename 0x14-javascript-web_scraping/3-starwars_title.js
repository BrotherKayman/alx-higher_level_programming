#!/usr/bin/node

const request = require('request');

function fetchMovieTitle(episodeNum) {
  const API_URL = `https://swapi-api.hbtn.io/api/films/${episodeNum}`;

  request(API_URL, function (err, response, body) {
    if (err) {
      console.error('Error:', err);
      return;
    }

    if (response.statusCode === 200) {
      try {
        const movieData = JSON.parse(body);
        console.log(movieData.title);
      } catch (parseError) {
        console.error('Error parsing response:', parseError);
      }
    } else {
      console.error('Error code:', response.statusCode);
    }
  });
}

const episodeNum = process.argv[2];
fetchMovieTitle(episodeNum);
