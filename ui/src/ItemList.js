import React from 'react';
import List from '@material-ui/core/List';
import { ListItem, ListItemIcon, ListItemText } from '@material-ui/core';
import ArrowForwardIcon from '@material-ui/icons/ArrowForward';

export function ItemList({items}) {
    return <List>
        {items.map(item => <ListItem  component="a" href={"https://www.listchallenges.com/lists/containing-item/"+item.id} target="_blank">
                <ListItemText primary={item.name} secondary={item.lists} />
                <ListItemIcon>
                    <ArrowForwardIcon />
                </ListItemIcon>
            </ListItem>)}
    </List>
}