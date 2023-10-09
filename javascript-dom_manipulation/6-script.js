//a JavaScript script that fetches the character name from this URL

const Names = document.getElementById("character");

fetch("https://swapi-api.hbtn.io/api/people/5/?format=json")
  .then(response => response.json())
  .then(data => {
    Names.textContent = data.name;
  })
  .catch(error => {
    Names.textContent = "Error fetching character name";
  });