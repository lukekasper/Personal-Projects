import { useState } from 'react'
import Line from './Line.jsx'

function Section({
  title,
  line_lst
}) {

  return (
    <div className="section">
      <h2>{title}</h2>
      {line_lst.map((line) => {
        <Line
          label={line.label}
          info={line.info}
        />
      })}
    </div>
  )
}

export default Section
