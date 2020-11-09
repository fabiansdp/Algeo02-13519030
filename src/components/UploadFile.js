import React, {useState} from 'react';
import axios from 'axios';

const UploadFile = () => {
    const UPLOAD_FILE_URL = "/upload";
    const [file,setFile] = useState(null);
    const [name,setName] = useState("");
    const [loading, setLoading] = useState(false);
    const [uploaded,setUploaded] = useState(false);

    const handleChange = (e) => {
        if (e?.target?.files) {
            if (e?.target?.files[0]) {
                setFile(e.target.files[0]);
            }
        }
    };

    const handleSubmit = async() => {
        try {
            const data = new FormData();
            data.append('file', file);
            const response = await axios.post(UPLOAD_FILE_URL, data);
            if (response.data.completed) {
                setName(response.data.name);
                setUploaded(true);
            }
        } catch (error) {
            console.log(error);
        }
    }

    return (
        <div id="uploader-container">
            <div className="file-upload">
                <label>Daftar Dokumen: </label>
                <input type="file" name="file" onChange={handleChange} accept=".txt,.html" />
                <button className="upload-button" type="submit" onClick={handleSubmit}><b>Upload</b></button>
            </div>
            <div className="confirmation">
                <p>{name} uploaded</p>
            </div>
            <style jsx>{`
                #uploader-container {
                    display: flex;
                    align-items: center;
                    flex-direction: column;
                    margin-top: 5%;
                }

                label {
                    font-size: 1.2rem;
                    font-weight: 700;
                    color: #ffea00;
                    padding: 10px;
                }

                input {
                    padding: 10px;
                }

                .upload-button {
                    color: #1A8FE3;
                    background: #FFF;
                    margin-top: 10px;
                    cursor: pointer;   
                    border: 0;
                    border-radius: 15px;
                    -webkit-box-shadow: 5px 5px 14px 1px rgba(0,0,0,0.3); 
                    box-shadow: 5px 5px 14px 1px rgba(0,0,0,0.3);
                    outline: 0;
                    width: 50%;
                    padding: 10px 0px;
                }

                .file-upload {
                    display: flex;
                    flex-direction: column;
                    align-items: center;
                }

                .confirmation {
                    display: ${uploaded ? "block" : "none"};
                    color: #FFF;
                }
            `}</style>
        </div>
    )
}

export default UploadFile;
