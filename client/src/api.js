let apiDomain = '';

if(process.env.NODE_ENV === 'development') {
    apiDomain = 'http://localhost:5000';
} else if(process.env.NODE_ENV === 'production') {
    apiDomain = '/api';
}

export function getTopItems() {
    return fetch(apiDomain + "/top-items")
        .then(res => res.json());
}

export function searchItems(query) {
    return fetch(apiDomain +"/search/" + query)
        .then(res => res.json())
}

export function checkItem(itemId) {
    fetch(apiDomain + "/items/" + itemId + "/check", {method : "PUT"})
        .then();
}
