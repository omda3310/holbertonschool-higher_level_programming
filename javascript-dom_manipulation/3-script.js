//If the current class is red, when the user click
// on id toggle_header element,the class must be
// updated to green ; and the reverse.
document.getElementById("toggle_header").addEventListener("click", () => {
    const class_header = document.querySelector("header");
    if(class_header.classList.contains("red")){
        class_header.classList.remove("red");
        class_header.classList.add("green");
    }
    else{
        class_header.classList.remove("green");
        class_header.classList.add("red");
    }
});