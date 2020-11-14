import React, { useState } from 'react';
import SearchBar from '../components/SearchBar';
import Result from '../components/Result';
import TabelKata from '../components/TabelKata';
import UploadFile from '../components/UploadFile';

const Home = () => {
  const [hasilQuery, setHasilQuery] = useState(null);
  const [listDokumen, setListDokumen] = useState([]);
  const [isSearch, setIsSearch] = useState(false);
  const [dataTabel, setDataTabel] = useState([]);

  return (
    <div id="home-container">
      <UploadFile/>
      <SearchBar setHasilQuery={setHasilQuery} setListDokumen={setListDokumen} setIsSearch={setIsSearch} setDataTabel={setDataTabel} />
      <Result listDokumen={listDokumen} isSearch={isSearch} />
      <TabelKata hasilQuery={hasilQuery} isSearch={isSearch} dataTabel={dataTabel} />
    </div>
  )
}

export default Home;