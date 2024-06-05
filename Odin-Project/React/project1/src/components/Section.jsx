import { useState } from 'react'
import Line from './Line.jsx'

function Section({
  title,
  lineList
}) {

  const infoListInit = lineList.map(line => line.info);

  const [hidden, setHidden] = useState(false);
  const [infoList, setInfoList] = useState(infoListInit);

  function editInfo() {
    setHidden(!hidden);
  }

  function submitInfo() {
    setHidden(!hidden);
  }

  const updateInfo = (newInfo, id) => {
    const newInfoList = infoList.map(item => {
      if (item.id === id) {
        return { ...item, info: newInfo };
      }
      return item;  
    });
    setInfoList(newInfoList);
  }

  return (
    <div className="section">
      <h2>{title}</h2>
      {lineList.map((line, index) => {
        <Line
          label={line.label}
          info={infoList[index]}
          hidden={hidden}
          id={id}
          onInfoUpdate={updateInfo}
        />
      })}
      <button onClick={editInfo} style={{ display: {hidden} ? 'none' : 'block' }}>
        Edit {title}
      </button>
      <button onClick={submitInfo} style={{ display: {hidden} ? 'block' : 'none' }}>
        Submit {title}
      </button>
    </div>
  )
}

export default Section
