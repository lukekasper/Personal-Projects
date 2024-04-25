import { useState } from 'react';
import { foods, filterItems } from './data.js';

export default function FilterableList() {
  const [query, setQuery] = useState('');
  
  function handleChange(e) {
    setQuery(e.target.value);
  }
  
  return (
    <>
      <SearchBar
        query={query}
        event={handleChange}  
      />
      <hr />
      <List 
        items={foods}
        query={query}
        event={handleChange}  
      />
    </>
  );
}

function SearchBar({ query, event }) {

  return (
    <label>
      Search:{' '}
      <input
        value={query}
        onChange={event}
      />
    </label>
  );
}

function List({ items, query, event }) {
  filtered_items = filterItems(items, query);
  return (
    <table>
      <tbody>
        {filtered_items.map(food => (
          <tr key={food.id}>
            <td>{food.name}</td>
            <td>{food.description}</td>
          </tr>
        ))}
      </tbody>
    </table>
  );
}
