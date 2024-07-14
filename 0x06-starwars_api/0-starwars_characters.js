#!/usr/bin/node

// Require the 'request' library to make HTTP requests
const request = require('request');

// Make a GET request to the Star Wars API endpoint for the specified film ID
request('https://swapi-api.hbtn.io/api/films/' + process.argv[2], (err, res, body) => {
  if (err) throw err; // Handle error if request fails

  // Parse the response body (which is in JSON format) to extract the list of characters
  const actors = JSON.parse(body).characters;

  // Call the function 'exactOrder' to process each character's URL
  exactOrder(actors, 0);
});

// Define a recursive function to process each character's URL
const exactOrder = (actors, x) => {
  // Base case: if x reaches the length of actors array, return
  if (x === actors.length) return;

  // Make a GET request to the URL of the character
  request(actors[x], function (err, res, body) {
    if (err) throw err; // Handle error if request fails

    // Parse the response body (which is in JSON format) to extract the character's name
    console.log(JSON.parse(body).name); // Print the character's name to the console

    // Recursively call exactOrder for the next character in the actors array
    exactOrder(actors, x + 1);
  });
};
