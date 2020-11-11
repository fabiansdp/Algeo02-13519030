import React from 'react';
import "../styles/result.css"
import ResultWrapper from './ResultWrapper';
import { Link } from 'react-router-dom';

const Result = () => {
  const items = [
    {
      judul: "daftar_email_hr_internship.txt",
      jumlah: 1000,
      kemiripan: 90,
      first_sentence: "Fabian anak terpintar satu semesta raya"
    },
    {
      judul: "NASA_Webinar.txt",
      jumlah: 1000,
      kemiripan: 90,
      first_sentence: "Fabian anak terpintar satu semesta raya"
    },
    {
      judul: "PP01_13519140.txt",
      jumlah: 1000,
      kemiripan: 90,
      first_sentence: "Fabian anak terpintar satu semesta raya"
    },
    {
      judul: "PP01_13519214.txt",
      jumlah: 1000,
      kemiripan: 90,
      first_sentence: "Fabian anak terpintar satu semesta raya"
    },
    {
      judul: "robots.txt",
      jumlah: 1000,
      kemiripan: 90,
      first_sentence: "Fabian anak terpintar satu semesta raya"
    },
  ]
  return (
    <ResultWrapper>
      <div className="result">
      {items.map((item,index) => (
        <div className="content" key={index}>
          <Link to={`/docs/${item.judul}`}><h3>{item.judul}</h3></Link>
          <p>Jumlah kata: {item.jumlah}</p>
          <p>Tingkat Kemiripan: {item.kemiripan}%</p>
          <p>{item.first_sentence}</p>
        </div>
      ))}
      </div>
    </ResultWrapper>
  )
}

export default Result;