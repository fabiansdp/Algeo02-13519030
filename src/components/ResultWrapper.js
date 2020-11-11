import React from 'react';
import "../styles/resultWrapper.css"

const ResultWrapper = ({children}) => (
    <div id="result-container">
        <h2>Hasil Pencarian</h2>
        {children}
    </div>
)

export default ResultWrapper;