import "../styles/navbar.css";
import React, { useEffect, useState } from 'react';
import { Link } from 'react-router-dom';

const NavBar = () => {
  const [onTop, setOnTop] = useState(true);

  const handleScroll = () => {
    if (onTop !== (window.pageYOffset === 0)) {
      setOnTop(window.pageYOffset === 0);
    }
  };

  useEffect(() => {
    window.addEventListener("scroll", handleScroll);
    return () => {
      window.removeEventListener("scroll", handleScroll);
    };
  });

  return (
    <header className={onTop ? "" : "shadow"} >
      <nav>
        <div className="logo">
          <Link to="/"><h1>Auto A</h1></Link>
        </div>
        <div id="spacer" />
        <ul className="nav-links">
          <Link to="/" style={{ textDecoration: 'none' }}>
            <li>Beranda</li>
          </Link>
          <Link to="/about" style={{ textDecoration: 'none' }}>
            <li>Tentang Kami</li>
          </Link>
        </ul>
      </nav>
    </header>
  )
}

export default NavBar;