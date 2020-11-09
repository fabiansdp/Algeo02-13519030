import React, {useState} from 'react';
import axios from 'axios';

const SearchBar = () => {
    const QUERY_URL = "/query";
    const [query, setQuery] = useState(null);

    const handleChange = async(e) => {
        if (e?.target?.value) {
            setQuery(e.target.value);
            try {
                const data = new FormData();
                data.append('query', query);
                const response = await axios.post(QUERY_URL, query);
                console.log(response)
            } catch (error) {
                console.log(error)
            }
        }
    };

    return (
        <div id="search-container">
            <div class="search">
                <input type="text" name="query" className="searchTerm" placeholder="Pencarian..." onChange={handleChange} />
                
            </div>
            <style jsx>{`
                #search-container {
                    margin-top: 2rem;
                    display: flex;
                    justify-content: center;
                }

                .search {
                    width: 55%;
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