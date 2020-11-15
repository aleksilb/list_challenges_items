import React, { useState } from 'react';
import { ItemList } from './ItemList';

export function TopItems() {
    const [items, setItems] = useState([]);

    fetch("http://localhost:5000/top-items")
        .then(res => res.json())
        .then(
            (result) => {
                setItems(result);
            });
    
    return <ItemList items={items} />
}