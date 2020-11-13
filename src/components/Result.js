import React from 'react';
import "../styles/result.css"
import ResultWrapper from './ResultWrapper';
import { Link } from 'react-router-dom';

const Result = ({ listDokumen, isSearch }) => {
  return (
    <ResultWrapper>
      <div className="result">
      {isSearch
        ? listDokumen.map((item,index) => (
          <div className="content" key={index}>
            <Link to={`/docs/${item.url}`}><h3>{item.judul}</h3></Link>
            <p>Jumlah kata: {item.jumlah}</p>
            <p>Tingkat Kemiripan: {item.similarity}%</p>
            <p>{item.first_sentence}</p>
          </div>
        ))
        : <p>Lakukan Pencarian</p>
      }
      </div>
    </ResultWrapper>
  )
}

export default Result;