function fetchAndDisplayTranslation() { 
const url ='https://hellosalut.stefanbohacek.dev/?lang=fr';
const elements_hello = document.getElementById('hello');

fetch(url)
.then(response => {
    if(!response.ok){
        throw new Error('Error')
    }
    return response.json();
})
.then(data => {
    const value = data.hello;
    elements_hello.textContent = value;
})
.catch(error => {
    console.error('Error');
});
}
document.addEventListener('DOMContentLoaded', fetchAndDisplayTranslation);