//a JavaScript script that updates the text color
// of the header element to red (#FF0000) when
// the user clicks on the tag with id red_header
const documents = document.getElementById("red_header");
documents.addEventListener("click", function(){
    documents.style.color = "#FF0000";
});
