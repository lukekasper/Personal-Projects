import { useState } from 'react'

function Line({
  label,
  info
}) {

  return (
    <p className="line">
      <span className="label">{label}: </span>
      <span className="info">{info}</span>
    </p>
  )
}

export default Line
