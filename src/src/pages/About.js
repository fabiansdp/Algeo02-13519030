import React from 'react';
import "../styles/about.css";
import { Link } from 'react-router-dom';
import aboutItems from "../constants/about-items";

const About = () => {
  return (
    <div id="about-container">
      <div className="about-box">
        <div className="header">
          <h1>Tentang Kami</h1>
        </div>
        <div className="section">
          <h3>Konsep Singkat</h3>
          <p>{aboutItems.konsep.content}</p>
          <img src="/rumus.png" alt=""/>
        </div>
        <div className="section">
          <h3>Penggunaan Program</h3>
          <p>{aboutItems.penggunaan.content}</p>
          <ul className="list-penggunaan">
            <li>{aboutItems.penggunaan.list1}</li>
            <li>{aboutItems.penggunaan.list2}</li>
          </ul>
        </div>
        <div className="section">
          <h3>Anggota Kelompok 27</h3>
          <ul className="anggota">
            <li>1. Ferdy Irawan F.</li>
            <li>2. Fakhri Nail W.</li>
            <li>3. Fabian Savero Diaz P.</li>
          </ul>
        </div>
        <Link to={{pathname: "https://github.com/fabiansdp/Algeo02-13519030"}} target="_blank" >
          <h3>Informasi Lebih Lanjut</h3>
        </Link>
      </div>
    </div>
  );
};

export default About;