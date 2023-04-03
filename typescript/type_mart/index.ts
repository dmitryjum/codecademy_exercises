import products from './products';
let shipping: number;
let taxPercent: number;
let taxTotal: number;
let total: number;
let shippingAddress: string = '10 Wall St. Old York, NY';
const productName: string = 'tote bag';

const product = products.filter(el => el.name === productName)[0];

if (product.preOrder == 'true') {
  console.log("We'll send you a message when it's on its way");
}

if (Number(product.price) >= 25) {
  shipping = 0
  console.log('We provide free shipping for this product');
} else {
  shipping = 5
}

taxPercent = shippingAddress.match(/New York/g) !== null ? 0.1 : 0.05;
taxTotal = Number(product.price) * taxPercent;
total = Number(product.price) + taxTotal + shipping;

console.log(`${product.name}\n${shippingAddress}\n${Number(product.price)}\n${taxTotal}\n${shipping}\n${total}`)