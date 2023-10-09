const url = 'https://swapi-api.hbtn.io/api/films/?format=json';
const element = document.getElementById("list_movies");

fetch(url)
.then(response => {
    if (!response.ok) {
        throw Error('Network not ok');
    }
    return response.json();
})
.then(data => {
    const films = data.results;
    films.forEach(flim => {
        title = flim.title
        const new_list = document.createElement("li");
        new_list.textContent = title;
        element.appendChild(new_list);
    });
})
.catch(error => {
    console.error('Fetch erorr:', error)
});