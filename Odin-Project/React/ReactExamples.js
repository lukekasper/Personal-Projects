// Loop over a list of items using map function
function List(props) {
  return (
    <ul>
      // generates a list of li elements for each animal
      {props.animals.map((animal) => {
        // conditionally render animal elements starting with an "L"
        return animal.startsWith("L") ? <li key={animal}>{animal}</li> : null;
        // optionally use below for the same functionality.  && only works this way in react with boolean value on the left side.
        // return animal.startsWith("L") && <li key={animal}>{animal}</li>;
      })}
    </ul>
  );
}

function App() {
  const animals = ["Lion", "Cow", "Snake", "Lizard"];

  return (
    <div>
      <h1>Animals: </h1>
      // this is where we assign the props as the animals list
      <List animals={animals} />
    </div>
  );
}

// data with unique ids as keys
const todos = [
  { task: "mow the yard", id: uuid() },
  { task: "Work on Odin Projects", id: uuid() },
  { task: "feed the cat", id: uuid() },
];

function TodoList() {
  return (
    <ul>
      {todos.map((todo) => (
        // here we are using the already generated id as the key.
        <li key={todo.id}>{todo.task}</li>
      ))}
    </ul>
  );
}
