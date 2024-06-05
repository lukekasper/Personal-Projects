import { useState } from 'react'
import Section from './Section.jsx'
import '../styles/App.css'

function App() {

  /// Initialization Info
  info1 = [
    { id: 1, label: "Name", info: "Luke Kasper" },
    { id: 2, label: "Email", info: "fake25email@gmail.com" },
    { id: 3, label: "Phone Number", info: "(888) 888-8888" },
  ];

  info2 = [
    { id: 4, label: "School Name", info: "Rutgers" },
    { id: 5, label: "Major", info: "Physics" },
    { id: 6, label: "Graduation Date", info: "05/12/2018" },
  ];

  info3 = [
    { id: 7, label: "Company Name", info: "Boeing" },
    { id: 8, label: "Position Title", info: "Engineer" },
    { id: 9, label: "Job Responsibilities", info: "Develop control law algorithms for V-22 flight control computers." },
    { id: 10, label: "Dates Worked", info: "05/12/2020 - 08/01/2023" },
  ];
  
  return (
    <>
      <Section
        title="General Information"
        lineList=info1
      />
      <Section
        title="Educational Experience"
        lineList=info2
      />
      <Section
        title="Occupational Experience"
        lineList=info3
      />
    </>
  )
}

export default App
