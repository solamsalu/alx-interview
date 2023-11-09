#!/usr/bin/node

const axios = require('axios');

function getMovieCharacters(movieId) {
    const movieUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}/`;

    axios.get(movieUrl)
        .then(response => {
            const characters = response.data.characters;

            characters.forEach(characterUrl => {
                axios.get(characterUrl)
                    .then(characterResponse => {
                        const characterName = characterResponse.data.name;
                        console.log(characterName);
                    })
                    .catch(error => {
                        console.error(`Error fetching character data: ${error.message}`);
                    });
            });
        })
        .catch(error => {
            console.error(`Error fetching movie data: ${error.message}`);
        });
}

const movieId = process.argv[2];

if (!movieId) {
    console.error('Usage: node script.js <Movie ID>');
    process.exit(1);
}

getMovieCharacters(movieId);
