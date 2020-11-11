import React from 'react';
import SearchBar from '../components/SearchBar';
import Result from '../components/Result';
import TabelKata from '../components/TabelKata';
import UploadFile from '../components/UploadFile';

const Home = () => (
  <div id="home-container">
    <UploadFile/>
    <SearchBar/>
    <Result/>
    <TabelKata/>
  </div>
)

export default Home;