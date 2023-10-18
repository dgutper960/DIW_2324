
const cambiarCss = () => {
    const navItems = document.querySelector("#navItems");
    navItems.classList.toggle("abrir");
};


function onIniciar() {
    console.log("Uso esta funcion para inicializar elementos de la pagina");
    const divMenu = document.querySelector("#divMenu");
    divMenu.addEventListener("click", cambiarCss)
}

window.onload = onIniciar();
