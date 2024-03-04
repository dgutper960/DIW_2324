




function onIniciar() {
  console.log("Hola Mundo");

  // 1. Conseguimos todos los botonos
  const botonesTab = document.querySelectorAll(".botonesTab__pestanya");
  // 2. Conseguimos todos los bloquews de texto"
  const bloquesTexto = document.querySelectorAll(".contenedorTexto__bloque");
  // 3. añadir Evenlistener a todos los botones
  botonesTab.forEach( (boton, i)=>{

      boton.addEventListener("click", ()=>{
        console.log("Click en boton"+i);
        // quitamos activo a todos los botones y al texto
        botonesTab.forEach( (botonFE, j)=>{
          botonFE.classList.remove("activo")
          bloquesTexto[j].classList.remove("activo");
        });
        // añadimos activo al boton pulsado y al texto correspondiente
        boton.classList.add("activo");
        bloquesTexto[i].classList.add("activo");
      });
  })

}


window.onload = onIniciar();
