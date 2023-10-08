// a JavaScript script that adds the class red to the header element when
// the user clicks on the tag with id red_header
const red_header_element = document.getElementById("red_header");
red_header_element.addEventListener("click", function(){
    document.querySelector("header").classList.add("red");
});
