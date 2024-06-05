import { useState } from 'react'
import Section from './Section.jsx'
import './App.css'

function App() {

  info1 = [
    { label: "Name", info: "Luke Kasper" },
    { label: "Email", info: "fake25email@gmail.com" },
    { label: "Phone Number", info: "(888) 888-8888" },
  ];

  info2 = [
    { label: "School Name", info: "Rutgers" },
    { label: "Major", info: "Physics" },
    { label: "Graduation Date", info: "05/12/2018" },
  ];

  info3 = [
    { label: "Company Name", info: "Boeing" },
    { label: "Position Title", info: "Engineer" },
    { label: "Job Responsibilities", info: "Develop control law algorithms for V-22 flight control computers." },
    { label: "Dates Worked", info: "05/12/2020 - 08/01/2023" },
  ];
  
  return (
    <>
      <Section
        title="General Information"
        line_lst=info1
      />
      <Section
        title="Educational Experience"
        line_lst=info2
      />
      <Section
        title="Occupational Experience"
        line_lst=info3
      />
    </>
  )
}

export default App
