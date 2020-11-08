import React, {useState} from 'react';
import axios from 'axios';

const UploadFile = () => {
    const UPLOAD_FILE_URL = "/upload";
    const [file,setFile] = useState(null);

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
            return console.log(response.data);
        } catch (error) {
            console.log(error);
        }
    }

    return (
        <div id="uploader-container">
            <div className="file-upload">
                <label>Daftar Dokumen: </label>
                <input type="file" name="file" onChange={handleChange} accept=".txt" />
                <button type="submit" value="upload" onClick={handleSubmit}>Submit</button>
            </div>
            <style jsx>{`
                #uploader-container {
                    display: flex;
                    justify-content: center;
                    margin-top: 5%;
                }

                label {
                    font-size: 1.2rem;
                    font-weight: 700;
                }

            `}</style>
        </div>
    )
}

export default UploadFile;
