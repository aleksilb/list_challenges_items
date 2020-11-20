import React, {useState} from 'react';
import {ItemList} from './ItemList';
import {Search} from './Search';
import {Button, CircularProgress} from '@material-ui/core';
import './App.css';
import * as api from './api.js';

function App() {
    const [items, setItems] = useState([]);
    const [searching, setSearching] = useState(false);
    const [showTop, setShowTop] = useState(false);

    let toggleTopItems = () => {
        if (showTop) {
            setShowTop(false);
            setItems([]);
        } else {
            setShowTop(true);
            api.getTopItems()
                .then(
                    (result) => {
                        setItems(result);
                    });
        }
    }

    let changeSearch = search => {
        setShowTop(false);
        if (search.length > 2) {
            setSearching(true);
            api.searchItems(search)
                .then(
                    (result) => {
                        setItems(result);
                        setSearching(false)
                    });
        } else {
            setItems([]);
        }
    }

    const checkItem = itemId => {
        setItems(items.filter(item => item.id !== itemId));
        api.checkItem(itemId);
    }

    return (
        <div className="App">
            <div className="ui">
                <Search changeSearch={changeSearch}/>
                <Button className="input" variant="contained" color={showTop ? "primary" : "default"}
                        onClick={toggleTopItems}>Show top items</Button>
            </div>
            {searching ? <CircularProgress/> : <ItemList className="list" items={items} checkItem={checkItem}/>}
        </div>
    );
}

export default App;
