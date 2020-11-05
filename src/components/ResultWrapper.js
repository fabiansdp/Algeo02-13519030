import React from 'react';

const ResultWrapper = ({children}) => (
    <div id="result-container">
        <h2>Hasil Pencarian</h2>
        {children}
        <style jsx>{`
            #result-container {
                margin-top: 5%;
                text-align: center;
                padding: 0 10%;
            }

            h2 {
                font-family: 'Viga', sans-serif;
                font-size: 2rem;
            }    
        `}</style>
    </div>
)

export default ResultWrapper;