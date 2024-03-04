




function onIniciar() {
  console.log("Hola Mundo");

  // 1. Conseguimos todos los botonos
  const botonesTab = document.querySelectorAll(".botonesTab__pestanya");
  // 2. Conseguimos todos los bloquews de texto"
  const bloquesTexto = document.querySelectorAll(".contenedorTexto__bloque");
  // 3. añadir Evenlistener a todos los botones
  botonesTab.forEach( (boton, i)=>{
      console.log(boton); // Cada boton

      boton.addEventListener("click", ()=>{
        console.log("Click en boton"+(i+1))
        boton.classList.add("activo");
      })
  })

}


window.onload = onIniciar();
