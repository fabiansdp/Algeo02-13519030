import React, {useState} from 'react';
import axios from 'axios';

const UploadFile = () => {
    const UPLOAD_FILE_URL = "/upload";
    const [file,setFile] = useState(null);
    const [name,setName] = useState("");
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
                <button type="submit" value="upload" onClick={handleSubmit}>Submit</button>
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
