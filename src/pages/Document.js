import React, { useState, useEffect } from 'react';
import "../styles/document.css"
import axios from 'axios';

const Document = ({ match }) => {
  const[item, setItem] = useState({});
  const[content, setContent] = useState([]);
  
  useEffect(() => {
    fetchItem();
  },[])

  const fetchItem = async() => {
    try {
      const item = await axios.get(`/doc/${match.params.id}`);
      setItem(item.data);
      setContent(item.data.content);
    } catch (error) {
      console.log(error);
    }
  }
  

  return (
    <div id="document-container">
      <div className="document-box">
        <div className="header">
          <h1>{item.name}</h1>
        </div>
        <div className="content">
          {content.map((line,index) => (
            <p key={index}>{line}</p>
          ))}
        </div>
      </div>
    </div>
  );
};

export default Document;