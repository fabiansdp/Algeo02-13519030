import React from 'react';
import ResultWrapper from './ResultWrapper';

const Result = () => {
    return (
        <ResultWrapper>
            <div className="result">
                <div className="number">
                    <p>1.</p>
                </div>
                <div className="content">
                    <a href=""><h3>Judul Dokumen</h3></a>
                    <p>Jumlah kata: ....</p>
                    <p>Tingkat Kemiripan: ....%</p>
                    <p>Kalimat pertama</p>
                </div>
            </div>
            <style jsx>{`
                .result {
                    display: flex;
                    margin-left: 7%;
                    text-align: left;
                }

                .content {
                    margin-left: 15px;
                }

                a {
                    text-decoration: none;
                }

                h3, p {
                    font-family: 'Roboto', serif;
                    font-size: 1.2rem;
                }
            `}</style>
        </ResultWrapper>
    )
}

export default Result;