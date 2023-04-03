let customersArray = ['Custy Stomer', 'C. Oostomar', 'C.U.S. Tomer', 3432434, 'Custo Mer', 'Custopher Ustomer', 3432435, 'Kasti Yastimeur'];

function checkCustomersArray(array) {
  array.forEach((el) => {
    if (typeof(el) != 'string') {
      console.log(`Type error: ${el} should be a string!`)
    }
  })
}

checkCustomersArray(customersArray);
function stringPush(val) {
  if(typeof(val) === 'string') {
    customersArray.push(val);
  }
}

// Array.prototype.stringPush = function(val) {
//   if (typeof(val) === 'string') {
//     this.push(val);
//   }
// }