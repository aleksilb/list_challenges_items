import React, { useState } from 'react';
import {ItemList} from './ItemList';
import {Search} from './Search';
import { Button, CircularProgress } from '@material-ui/core';
import './App.css';

function App() {
  const [items, setItems] = useState([]);
  const [searching, setSearching] = useState(false);
  const [showTop, setShowTop] = useState(false);
  let apiDomain = '';

  if(process.env.NODE_ENV === 'development') {
      apiDomain = 'http://localhost:5000';
  } else if(process.env.NODE_ENV === 'production') {
      apiDomain = '/api';
  }

  let toggleTopItems = () => {
    if(showTop) {
      setShowTop(false);
      setItems([]);
    } else {
      setShowTop(true);
      fetch(apiDomain + "/top-items")
        .then(res => res.json())
        .then(
            (result) => {
                setItems(result);
            });
    }
  }

  let changeSearch = search => {
    setShowTop(false);
    if(search.length > 2) {
      setSearching(true);
      fetch(apiDomain +"/search/" + search)
          .then(res => res.json())
          .then(
              (result) => {
                  setItems(result);
                  setSearching(false)
              });
    } else {
      setItems([]);
    }
  }
  
  return (
    <div className="App">
      <div className="ui">
      <Search changeSearch={changeSearch} />
      <Button className="input" variant="contained" color={showTop ? "primary" : "default"} onClick={toggleTopItems}>Show top items</Button>
      </div>
      {searching ? <CircularProgress /> : <ItemList className="list" items={items} />}
    </div>
  );
}

export default App;
