/////////////////////// RENDERING ///////////////////////
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


/////////////////////// PROPS ///////////////////////
// Using Props to modifiy characteristics of a single reuseable component
//function Button(props) {
function Button({ text = "Click Me!", color = "blue", fontSize = 12, handleClick }) {
  const buttonStyle = {
    color: color,
    fontSize: fontSize + "px"
  };

  return (
    // This syntax with the anonomyous function is necessary to prevent the function from being called on rendering the component
    <button onClick={() => handleClick('https://www.theodinproject.com')} style={buttonStyle}>
      {text}
    </button>
  );
}

export default function App() {
  const handleButtonClick = (url) => {
    window.location.href = url;
  };

  return (
    <div>
      <Button handleClick={handleButtonClick} />
    </div>
  );
}


// Nesting components and using the 'children' prop
import Avatar from './Avatar.js';

function Card({ children }) {
  return (
    <div className="card">
      {children}
    </div>
  );
}

function Profile() {
  return (
    <Card>
      <Avatar
        size={100}
        person={{ 
          name: 'Katsuko Saruhashi',
          imageId: 'YfeOqp2'
        }}
      />
    </Card>
  );
}

function Avatar({ person, size }) {
  return (
    <img
      className="avatar"
      src={getImageUrl(person)}
      alt={person.name}
      width={size}
      height={size}
    />
  );
}

function getImageUrl(person, size = 's') {
  return (
    'https://i.imgur.com/' +
    person.imageId +
    size +
    '.jpg'
  );
}


/// Prop Types
import React from 'react';
import PropTypes from 'prop-types';

const RenderName = (props) => {
  return <div>{props.name}</div>;
};

RenderName.propTypes = {
  name: PropTypes.string,
};

RenderName.defaultProps = {
  name: 'Zach',
};

export default RenderName;
