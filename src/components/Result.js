import React from 'react';
import ResultWrapper from './ResultWrapper';

const Result = () => {
    return (
        <ResultWrapper>
            <div className="result">
                <div className="content">
                    <a href=""><h3>Judul Dokumen</h3></a>
                    <p>Jumlah kata: ....</p>
                    <p>Tingkat Kemiripan: ....%</p>
                    <p>Kalimat pertama</p>
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
                    background: #FFF;
                    margin-left: 6%;
                    text-align: left;
                    border-radius: 30px;
                }

                .content {
                    width: 100%;
                    padding: 1rem 1.5rem;
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