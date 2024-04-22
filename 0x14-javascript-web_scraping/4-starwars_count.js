#!/usr/bin/node

const request = require('request');
const apiUrl = process.argv[2];
const characterId = '18';

/**
 * Fetch movie data from the Star Wars API.
 * @param {string} apiUrl - The URL of the Star Wars API endpoint.
 * @param {Function} callback - Callback function to handle the API response.
 */

function fetchMovieData(apiUrl, callback) {
  request(apiUrl, function (error, response, body) {
    if (error) {
      callback(error, null);
      return;
    }

    if (response.statusCode !== 200) {
      callback(`Request failed with status code: ${response.statusCode}`, null);
      return;
    }

    try {
      const data = JSON.parse(body);
      callback(null, data);
    } catch (parseError) {
      callback(`Error parsing response: ${parseError}`, null);
    }
  });
}


function MoviesWithWedge(movies, characterId) {
  return movies.reduce((count, movie) => {
    const hasWedge = movie.characters.some(character => character.endsWith(`/${characterId}/`));
    return hasWedge ? count + 1 : count;
  }, 0);
}


function FetchData(apiUrl, characterId) {
  fetchMovieData(apiUrl, (error, data) => {
    if (error) {
      console.error('Error:', error);
      return;
    }

    const wedgeAntillesMoviesCount = MoviesWithWedge(data.results, characterId);
    console.log(wedgeAntillesMoviesCount);
  });
}

if (process.argv.length !== 3) {
  process.exit(1);
}

FetchData(apiUrl, characterId);
