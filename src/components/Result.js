import React from 'react';
import "../styles/result.css"
import ResultWrapper from './ResultWrapper';

const Result = () => {
    return (
        <ResultWrapper>
            <div className="result">
                <div className="content">
                    <a href="#"><h3>Judul Dokumen</h3></a>
                    <p>Jumlah kata: ....</p>
                    <p>Tingkat Kemiripan: ....%</p>
                    <p>Kalimat pertama</p>
                </div>
                <div className="content">
                    <a href="#"><h3>Judul Dokumen</h3></a>
                    <p>Jumlah kata: ....</p>
                    <p>Tingkat Kemiripan: ....%</p>
                    <p>Kalimat pertama</p>
                </div>
            </div>
        </ResultWrapper>
    )
}

export default Result;