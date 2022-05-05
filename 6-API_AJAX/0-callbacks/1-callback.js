/* 
Código basado en el material de la siguiente url
https://medium.com/front-end-weekly/callbacks-promises-and-async-await-ad4756e01d90
*/

/* 
Callback es un método que puedes dar como parámetro de entrada a función.
Esto permite generar una sincronía en las llamadas entre funciones.
*/
function printString(string, callback) {
    setTimeout(() => {
      console.log(string);
      callback();
    }, Math.floor(Math.random() * 100) + 1);
  }
  
  function printAll() {
    printString("A", () => {
      printString("B", () => {
        printString("C", () => {});
      });
    });
  }
  printAll();
  /* 
  Solucionado, pero usando múltiples anidaciones de callbacks para que funcione.
  ¿Y si fueran 20 llamadas sincrónicas? (Callback hell)
  */
