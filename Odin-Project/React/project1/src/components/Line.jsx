import { useState } from 'react'
import '../styles/Line.css'

function Line({
  label,
  info,
  hidden,
  id,
  onInfoUpdate
}) {
  
  return (
    <p className="line">
      <span className="label">{label}: </span>
      <span className="info" style={{ display: hidden ? 'none' : 'block' }>{info}</span>
      <input
        className="input"
        type="text" value={info}
        style={{ display: hidden ? 'block' : 'none' }
        onChange={(event) => onInfoUpdate(event.target.value, id)}
      />
    </p>
  )
}

export default Line
