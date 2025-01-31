import "../styles/searchbar.css"
import React, {useState} from 'react';
import axios from 'axios';
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';
import { faSearch } from '@fortawesome/free-solid-svg-icons';

const SearchBar = ({ setHasilQuery, setListDokumen, setIsSearch, setDataTabel}) => {
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
            setHasilQuery(response.data.query)
            setListDokumen(response.data.hasil)
            setDataTabel(response.data.dataTabel)
            setIsSearch(true)
            
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
        </div>
    )
}

export default SearchBar;