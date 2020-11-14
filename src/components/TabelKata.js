import React from 'react';
import "../styles/table.css"

const TabelKata = ({ hasilQuery, isSearch, dataTabel }) => {
  return (
    <div id="table-container">
      <table>
        <thead>
          <tr>
            <th>Dokumen\Term</th>
            {isSearch 
            ? hasilQuery.map((item, index) => (
              <th key={index}>{item}</th>
            ))
            : <th>TBD</th>
            }
          </tr>
        </thead>
        <tbody>
          {isSearch 
          ? dataTabel.map((item, index) => (
            <tr key={index} >
              <td>{item.dokumen}</td>
              {Object.entries(item.jumlah).map(([key,value]) => {
                if (hasilQuery.includes(key)) {
                  return (
                    <td key={key}>{value}</td>
                  )
                }
            })}
            </tr>
          ))
          : <tr>
              <td>TBD</td>
              <td>NaN</td>
            </tr>
          }
        </tbody>
      </table>
    </div>
  )
}

export default TabelKata;