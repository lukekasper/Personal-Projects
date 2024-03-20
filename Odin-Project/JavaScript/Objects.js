//////////////////////////////////////// Javascript Objects ////////////////////////////////////////
const myObject = {
  property: 'Value!',
  otherProperty: 77,
  "obnoxious property": function() {
    // do stuff!
  }
};

// dot notation
myObject.property; // 'Value!'

// Object constructor
function Player(name, marker) {
  this.name = name;
  this.marker = marker;
  this.sayName = function() {
    console.log(this.name)
  };
}

const player = new Player('steve', 'X');
player1.sayName(); // logs 'steve'

Object.getPrototypeOf(player1) === Player.prototype; // returns true
Object.getPrototypeOf(player2) === Player.prototype; // returns true

// Attributes and methods defined on the prototype object are available in all the created objects
Player.prototype.sayHello = function() {
   console.log("Hello, I'm a player!");
};

player1.sayHello(); // logs "Hello, I'm a player!"
player2.sayHello(); // logs "Hello, I'm a player!"

player1.valueOf(); // Output: Object { name: "steve", marker: "X", sayName: sayName() }

// Can set prototype to make `Player` objects inherit from `Person`
Object.setPrototypeOf(Player.prototype, Person.prototype);

//////////////////////////////////////// 'this' in Javascript ////////////////////////////////////////

////////// function invocation //////////
// this refers to the global object 'window' in function invocation
  
// IIFE (immediately-invoked function expression)
const message = (function(name) {
  return 'Hello ' + name + '!';
})('World');
  
function sum(a, b) {
  console.log(this === window); // => true
  this.myNumber = 20; // add 'myNumber' property to global object
  return a + b;
}
// sum() is invoked as a function
// this in sum() is a global object (window)
sum(15, 16);     // => 31
window.myNumber; // => 20

////////// method invocation //////////
// this refers to the object that owns the method

const calc = {
  num: 0,
  increment() {
    console.log(this === calc); // => true
    this.num += 1;
    return this.num;
  }
};

// method invocation. this is calc
calc.increment(); // => 1
calc.increment(); // => 2

// constructor invocation
// Constructor invocation is performed when new keyword is followed by an expression that evaluates to a function object
// this is the newly created object in a constructor invocation
function Country(name, traveled) {
  this.name = name ? name : 'United Kingdom';
  this.traveled = Boolean(traveled); // transform to a boolean
}

Country.prototype.travel = function() {
  this.traveled = true;
};

// Constructor invocation
const france = new Country('France', false);
// Constructor invocation
const unitedKingdom = new Country;

france.travel(); // Travel to France

////////// indirect invocation //////////
// Indirect invocation is performed when a function is called using myFun.call() or myFun.apply() methods
// this is the first argument of .call() or .apply() in an indirect invocation
const rabbit = { name: 'White Rabbit' };

function concatName(string) {
  console.log(this === rabbit); // => true
  return string + this.name;
}

// Indirect invocations
concatName.call(rabbit, 'Hello ');  // => 'Hello White Rabbit'
concatName.apply(rabbit, ['Bye ']); // => 'Bye White Rabbit

////////// bound invocation //////////
// A bound function is a function whose context and/or arguments are bound to specific values using .bind() method
// this is the first argument of myFunc.bind(thisArg) when invoking a bound function
// It is a powerful technique that allows creating functions with a predefined this value
const numbers = {
  array: [3, 5, 10],

  getNumbers() {
    return this.array;
  }
};

// Create a bound function
const boundGetNumbers = numbers.getNumbers.bind(numbers);
boundGetNumbers(); // => [3, 5, 10]

// Extract method from object
const simpleGetNumbers = numbers.getNumbers;
simpleGetNumbers(); // => undefined or throws an error in strict mode

////////// arrow function //////////
// Arrow function is designed to declare the function in a shorter form and lexically bind the context
// this is the enclosing context where the arrow function is defined
class Point {
  constructor(x, y) {
    this.x = x;
    this.y = y;
  }

  log() {
    console.log(this === myPoint); // => true
    setTimeout(() => {
      console.log(this === myPoint);      // => true
      console.log(this.x + ':' + this.y); // => '95:165'
    }, 1000);
  }
}
const myPoint = new Point(95, 165);
myPoint.log();
