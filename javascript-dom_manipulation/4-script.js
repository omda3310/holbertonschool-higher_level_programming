//a JavaScript script that adds a li element to a list
//when the user clicks on the element with id add_item
document.getElementById("add_item").addEventListener("click", () => {
    list_items = document.querySelector(".my_list");
    child_item = document.createElement("li");
    child_item.textContent("Item");
    list_items.appendChild(child_item);
});
