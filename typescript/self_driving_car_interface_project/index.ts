import { getObstacleEvents } from './computer-vision';
interface Events {
  [event: string]: boolean;
}

interface AutonomousCar {
  isRunning?: boolean;
  respond: (events: Events) => void;
}

interface AutonomousCarProps{
  isRunning?: boolean;
  steeringControl: Steering
}

interface Control {
  execute: (command: string) => void;
}

interface Steering extends Control {
  turn: (direction: string) => void;
}

class Car implements AutonomousCar {
  constructor(props: AutonomousCarProps) {
    this.isRunning = props.isRunning
    this.steeringControl = props.steeringControl
  }
  isRunning;
  steeringControl;

  respond(events: Events) {
    if (!this.isRunning) {
      console.log('The car is off');
    }

    Object.keys(events).forEach(eventKey => {
      if (!eventKey) { return }
      if (eventKey === 'ObstacleLeft') {
        this.steeringControl.turn('right')
      } else if (eventKey === 'Obstacleright') {
        this.steeringControl.turn('left')
      }
    })
  }
}

class SteeringControl implements Steering {
  execute(command: string) {
    console.log(`Executing: ${command}`)
  }

  turn(direction: string) {
    this.execute(`turn ${direction}`)
  }
}

let steering = new SteeringControl;
let autonomousCar = new Car({ isRunning: true, steeringControl: steering })
autonomousCar.respond(getObstacleEvents())