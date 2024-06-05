import { useState } from 'react'
import Line from './Line.jsx'

function Section({
  title,
  line_lst
}) {

  const [hidden, setHidden] = useState(false);

  function toggleInputVis() {
    setHidden(!hidden);
  }

  function submitInfo() {
    setHidden(!hidden);
    // TODO - Submit info to update info state variable
  }

  return (
    <div className="section">
      <h2>{title}</h2>
      {line_lst.map((line) => {
        <Line
          label={line.label}
          info={line.info}
          hidden={hidden}
        />
      })}
      <button onClick={toggleInputVis} style={{ display: {hidden} ? 'none' : 'block' }}>
        Edit {title}
      </button>
      <button onClick={submitInfo} style={{ display: {hidden} ? 'block' : 'none' }}>
        Submit {title}
      </button>
    </div>
  )
}

export default Section
