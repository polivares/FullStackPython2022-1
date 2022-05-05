/* 
Código basado en el material de la siguiente url
https://medium.com/front-end-weekly/callbacks-promises-and-async-await-ad4756e01d90
*/

/*
El anidamiento producido por CallBacks se puede resolver utilizando Promises.
Promise encapsula el funcionamiento de la función en un objeto. 
Si se "resuelve" correctamente, debe llamarse a función resolve. En caso contrario,
se debe llamar a función reject.
*/

function printString(string){
    return new Promise((resolve, reject) => {
      setTimeout(
        () => {
         console.log(string)
         resolve()
        }, 
       Math.floor(Math.random() * 100) + 1
      )
    })
}

/* Los resolve son capturados por el then, y los reject son capturados por el catch */
function printAll(){
  printString("A")
  .then(() => printString("B"))
  .then(() => printString("C"))
}
printAll()