humbargar = document.querySelector(".humbargar");
humbargar_box = document.querySelector(".humbargar-box");
navbar = document.querySelector(".navbar");

humbargar_box.addEventListener('click', () => {
    navbar.classList.toggle("expand");
    humbargar.classList.toggle("humbargar-change");
});