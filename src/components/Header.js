import React from 'react'

const Header = () => (
    <div id="header-container">
        <h1>Auto A</h1>
        <style jsx>{`
            #header-container {
                text-align: center;
            }
            h1 {
                font-family: 'Viga', sans-serif;
                font-size: 3rem;
                color: #ffea00;
            }
        `}</style>
    </div>
);

export default Header