#!/usr/bin/node

const util = require('util');
const request = util.promisify(require('request'));
const filmID = process.argv[2];

async function getSwCharacters(filmID) {
	const url = 'https://swapi-api.alx-tools.com/api/films/' + filmID;
	let response = await (await request(url)).body;
	response = JSON.parse(response);
	const characters = response.characters;

	for (let i = 0; i < characters.length; i++) {
		const newUrl = characters[i];
		let character = await (await request(newUrl)).body;
		character = JSON.parse(character);
		console.log(character.name);
	}
}

getSwCharacters(filmID);
