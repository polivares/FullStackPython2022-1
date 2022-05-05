/* 
Código basado en el material de la siguiente url
https://medium.com/front-end-weekly/callbacks-promises-and-async-await-ad4756e01d90
*/

// Código sin callback
function printString(string) {
  setTimeout(() => {
    console.log(string);
  }, Math.floor(Math.random() * 100) + 1);
}

function printAll() {
  printString("A");
  printString("B");
  printString("C");
}
printAll(); // ¡Llamados asíncronos! ¿Cómo lo podemos solucionar? Callbacks!

