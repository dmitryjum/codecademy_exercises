/**
 * Returns nothing, but logs the salad string
 * 
 * @param fruit1 - first input string
 * @param fruit2 - second input string
 * @returns nothing
 */

function makeFruitSalad(fruit1: string, fruit2: string): void {
  let salad = fruit1 + fruit2 + fruit2 + fruit1 + fruit2+ fruit1 + fruit1;
  console.log(salad);
}



/**
 * logs "I'm ${status} 'repeat' number of times"
 * 
 * @param status - optional string status argument
 * @param repeat - optional number repeat argument
 * @returns nothing
 */
function proclaim(status = 'not ready...', repeat = 1) {
  for (let i = 0; i < repeat; i += 1) {
    console.log(`I'm ${status}`);
  }
}