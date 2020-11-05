import React from 'react';
import Header from './components/Header';
import SearchBar from './components/SearchBar';
import Result from './components/Result';
import TabelKata from './components/TabelKata';
import UploadFile from './components/UploadFile';

function App() {
  return (
    <div className="App">
      <Header/>
      <UploadFile/>
      <SearchBar/>
      <Result/>
      <TabelKata/>
      <style jsx>{`
        @import url('https://fonts.googleapis.com/css2?family=Viga&display=swap');
        @import url('https://fonts.googleapis.com/css2?family=Roboto&display=swap');
        * {
          font-size: 16px;
        }  
      `}</style>
    </div>
  );
}

export default App;
