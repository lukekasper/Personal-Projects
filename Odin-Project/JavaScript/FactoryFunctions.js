// Closures
function makeAdding (firstNumber) {
  // "first" is scoped within the makeAdding function
  const first = firstNumber;
  return function resulting (secondNumber) {
    // "second" is scoped within the resulting function
    const second = secondNumber;
    return first + second;
  }
}
// but we've not seen an example of a "function"
// being returned, thus far - how do we use it?

const add5 = makeAdding(5);    
console.log(add5(2)) // logs 7; add5 has access to "first" because it was in the scope of makeAdding when the closure was made

// Factory Functions: used like constructors to create objects but do not contain the new keyword
function createUser (name) {
  const discordName = "@" + name;

  let reputation = 0;
  const getReputation = () => reputation;
  const giveReputation = () => reputation++;

  return { name, discordName, getReputation, giveReputation }; // shorthand form of { name: name, discordName: discordName...}
}

const josh = createUser("josh");
josh.giveReputation();
josh.giveReputation();

console.log({
  discordName: josh.discordName,
  reputation: josh.getReputation()
});

// reputation variable is considered private since outside the function there is no access to it (only getter/setter methods)

// shorthand for destructing objects:
const obj = { a: 1, b: 2 };
const { a, b } = obj;  // same as: const a = obj.a;    const b = obj.b;

// Extend one factory in another that needs some more metrics
function createPlayer (name, level) {
  const { getReputation, giveReputation } = createUser(name);

  const increaseLevel = () => level++;
  return { name, getReputation, giveReputation, increaseLevel };
}
// create your User, extract what you need from it, and re-return whatever you want to - hiding the rest

// Module pattern - IIFEs: pattern of wrapping a factory function inside an IIFE is called the module pattern
const calculator = (function () {
  const add = (a, b) => a + b;
  const sub = (a, b) => a - b;
  const mul = (a, b) => a * b;
  const div = (a, b) => a / b;
  return { add, sub, mul, div };
})();

calculator.add(3,5); // 8
calculator.sub(6,2); // 4
calculator.mul(14,5534); // 77476
