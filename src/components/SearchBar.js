import React from 'react';
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';
import { faSearch } from '@fortawesome/free-solid-svg-icons';

const SearchBar = () => (
    <div id="search-container">
        <div class="search">
            <input type="text" className="searchTerm" placeholder="Pencarian..." />
            <button type="submit" className="searchButton"><FontAwesomeIcon icon={faSearch}/></button>
        </div>
        <style jsx>{`
            #search-container {
                margin-top: 2rem;
                display: flex;
                justify-content: center;
            }

            .search {
                width: 50%;
                display: flex;
            }

            .searchTerm {
                width: 100%;
                border: 1px solid #a6a6a6;
                border-right: none;
                padding: 10px;
                border-radius: 5px 0 0 5px;
                outline: none;
            }

            .searchButton {
                width: 10%;
                border: 1px solid #a6a6a6;
                background: #FFFF;
                color: #000000;
                border-radius: 0 5px 5px 0;
                cursor: pointer;
                font-size: 20px;
            }
        `}</style>
    </div>
)

export default SearchBar;