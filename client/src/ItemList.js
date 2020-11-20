import React from 'react';
import List from '@material-ui/core/List';
import { ListItem, ListItemIcon, ListItemText } from '@material-ui/core';
import ArrowForwardIcon from '@material-ui/icons/ArrowForward';
import { Checkbox } from '@material-ui/core';

export function ItemList({items, checkItem}) {
    return <List>
        {items.map(item =>
            <ListItem key={item.id} component="a" href={"https://www.listchallenges.com/lists/containing-item/"+item.id} target="_blank" >
                <ListItemIcon>
                    <Checkbox onClick={checkItem.bind(this, item.id)} />
                </ListItemIcon>
                <ListItemText primary={item.name} secondary={item.lists} />
                <ListItemIcon>
                    <ArrowForwardIcon />
                </ListItemIcon>
            </ListItem>)}
    </List>
}
