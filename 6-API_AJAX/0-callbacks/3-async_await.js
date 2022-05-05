/* 
Código basado en el material de la siguiente url
https://medium.com/front-end-weekly/callbacks-promises-and-async-await-ad4756e01d90
*/

/*
Async/Await son "adornos" para las promesas, que permiten tener un código mucho
más legible.
Una función asincrónica es marcada con el prefijo async. Cada llamada en espera
deben ser marcadas con await.
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

  async function printAll(){
    await printString("A")
    await printString("B")
    await printString("C")
  }
  printAll()