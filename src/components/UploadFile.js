import React from 'react';

const UploadFile = () => {
    return (
        <div id="uploader-container">
            <p>Daftar Dokumen: </p>
            <form action="">
                <input type="file" id="myFile" name="filename"/>
                <input type="submit"/>
            </form>
            <style jsx>{`
                #uploader-container {
                    display: flex;
                    justify-content: center;
                    margin-top: 5%;
                }

                #uploader-container p {
                    margin: 0;
                }

                form {
                    margin-left: 1rem;
                }
            `}</style>
        </div>
    )
}

export default UploadFile;
