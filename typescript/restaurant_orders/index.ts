import { restaurants, Restaurant } from "./restaurants";
import { orders, Order, PriceBracket } from "./orders";

/// Add your getMaxPrice() function below:
function getMaxPrice(bracket: PriceBracket): number {
  return {
    0: 10.0,
    1: 20.0,
    2: 30.0
  }[bracket]
}
/// Add your getOrders() function below:
function getOrders(price: PriceBracket, orders: Order[][]): Order[][] {
  let filteredOrders: Order[][] = [];
  filteredOrders = orders.map((order, i) => orders[i].filter(el => el.price <= getMaxPrice(price)))
  return filteredOrders;
}
/// Add your printOrders() function below:

/// Main
const elligibleOrders = getOrders(PriceBracket.Low, orders);
console.log(elligibleOrders);

function printOrders(restaurants: Restaurant[], orders: Order[][]): void {
  restaurants.forEach((rest, i) => {
    if (orders[i].length > 0) {
      console.log(rest.name)
      orders[i].forEach(order => console.log(`- ${order.name}: $${order.price}`))
    }
  })
}
printOrders(restaurants, elligibleOrders);
