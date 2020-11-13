import React from 'react';

const TabelKata = ({ hasilQuery }) => {
    console.log(hasilQuery)
    return (
        <div id="table-container">
            <table>
                <thead>
                    <tr>
                        <th>Query</th>
                        <th>Jumlah</th>
                    </tr>
                </thead>
                <tbody>
                    <tr>
                        <td>Term</td>
                        <td>Query</td>
                    </tr>
                </tbody>
            </table>
            <style jsx>{`
                #table-container {
                    margin-top: 5%;
                    display: flex;
                    justify-content: center;
                    margin-bottom: 100px;
                    border-radius: 20px;
                }    

                table {
                    width: 50%;
                    background: #FFF;
                    border-radius: 10px;
                    text-align: center;
                    -webkit-box-shadow: 5px 5px 14px 1px rgba(0,0,0,0.3); 
                    box-shadow: 5px 5px 14px 1px rgba(0,0,0,0.3);
                }
            `}</style>
        </div>
    )
}

export default TabelKata;