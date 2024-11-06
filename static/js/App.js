function logNumber(number) {
    fetch(`/api/log-number/${number}/`, {
        method: 'PATCH',
        headers: {
            'Content-Type': 'application/json',
        }
    })
    .then(response => response.json())
    .then(data => {
        console.log(data.message);
    })
    .catch(error => {
        console.error('Error:', error);
    });
}


function resetTable(table) {
    const response = fetch(`/reset-table/${table}`);
    if (response.ok) {
        
    }
}