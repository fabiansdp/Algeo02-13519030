import React from 'react';
import "../styles/table.css"

const TabelKata = ({ hasilQuery, isSearch }) => {
  return (
    <div id="table-container">
      <table>
        <thead>
          <tr>
            <th>Query</th>
            <th>Jumlah</th>
          </tr>
        </thead>
        <tbody>
          {isSearch 
          ? hasilQuery.map((item, index) => (
            <tr key={index} >
              <td>{item.kata}</td>
              <td>{item.jumlah}</td>
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