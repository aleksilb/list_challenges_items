import React, { useEffect, useState } from 'react';
import IconButton from '@material-ui/core/IconButton';
import { TextField } from '@material-ui/core';
import { Clear } from '@material-ui/icons';

export function Search({changeSearch}) {
    const [search, setSearch] = useState('');
    const searchWait = 500;

    useEffect (() => {
        let searchTimer = setTimeout(()=> {
            console.log(search);
            changeSearch(search);
        }, searchWait);

        return () => {clearTimeout(searchTimer)}
    }, [search]);

    const clearSearch = () => {
        setSearch('');
    }

    return <form className="input">
        <TextField label="Search" onChange={(event) => {setSearch(event.target.value)}} value={search} />
        <IconButton color="primary" aria-label="clear" component="span" onClick={clearSearch}>
            <Clear />
        </IconButton>
    </form>
}