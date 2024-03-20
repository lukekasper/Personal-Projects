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

// Practice:
function Book(title, author, pages, read) {
  this.title = title;
  this.author = author;
  this.pages = pages;
  this.read = read
  this.info = function() {
    const read_str = this.read ? "read" : "not read yet";
    const info_str = this.title + "by" + this.author + ", " + this.pages.toString() + " pages, " + read_str;
    return info_str
}
const donQuixote = new Book("Don Quixote", "Miguel de Cervantes", 909, True);
console.log(donQuixote.info());
