import React from 'react';

const TabelKata = () => {
    return (
        <div id="table-container">
            <table>
                <thead>
                    <tr>
                        <th>Term</th>
                        <th>Query</th>
                        <th>D1</th>
                    </tr>
                </thead>
                <tbody>
                    <tr>
                        <td>Term</td>
                        <td>Query</td>
                        <td>D1</td>
                    </tr>
                    <tr>
                        <td>Term</td>
                        <td>Query</td>
                        <td>D1</td>
                    </tr>
                </tbody>
            </table>
            <style jsx>{`
                #table-container {
                    margin-top: 5%;
                    display: flex;
                    justify-content: center;
                    margin-bottom: 100px;
                }    

                table {
                    width: 70%;
                }

                table,th,td {
                    border: 1px solid black;
                }
            `}</style>
        </div>
    )
}

export default TabelKata;