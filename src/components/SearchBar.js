import React, {useState} from 'react';
import axios from 'axios';
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';
import { faSearch } from '@fortawesome/free-solid-svg-icons';

const SearchBar = () => {
    const QUERY_URL = "/query";
    const [query, setQuery] = useState("");

    const handleChange = (e) => {
        if (e?.target?.value) {
            setQuery(e.target.value);
        }
    }

    const handleSubmit = async() => {
        try {
            const data = new FormData();
            data.append('query', query);
            const response = await axios.post(QUERY_URL, data);
            console.log(response.data)
        } catch (error) {
            console.log(error)
        }
    }

    return (
        <div id="search-container">
            <div class="search">
                <input type="text" name="query" className="searchTerm" placeholder="Pencarian..." onChange={handleChange} on/>
            </div>
            <span onClick={handleSubmit}><FontAwesomeIcon icon={faSearch}/></span>
            <style jsx>{`
                #search-container {
                    margin-top: 2rem;
                    display: flex;
                    justify-content: center;
                }

                span {
                    position: relative;
                    top: 15px;
                    cursor: pointer;
                    font-size: 1.5rem;
                    color: #1A8FE3;
                }

                .search {
                    width: 55%;
                    -webkit-box-shadow: 5px 5px 14px 1px rgba(0,0,0,0.3); 
                    box-shadow: 5px 5px 14px 1px rgba(0,0,0,0.3);
                }

                .searchTerm {
                    width: 100%;
                    border: 1px solid #a6a6a6;
                    border-right: none;
                    padding: 25px;
                    border-radius: 20px;
                    outline: none;
                }
            `}</style>
        </div>
    )
}

export default SearchBar;