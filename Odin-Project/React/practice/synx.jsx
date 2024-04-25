import { useState } from 'react';

export default function SyncedInputs() {
  const [text, setText] = useState('');

  function handleChange(e) {
    setText(e.target.value);
  }
  
  return (
    <>
      <Input 
        label="First input"
        text={text}
        event={handleChange}
      />
      <Input 
        label="Second input"
        text={text}
        event={handleChange}
      />
    </>
  );
}

function Input({ label, text, event }) {


  return (
    <label>
      {label}
      {' '}
      <input
        value={text}
        onChange={event}
      />
    </label>
  );
}
