   // Maximum number of squares to display
   const MAX_NUMBERS = 8;

function logNumber(number) {
    
    // Create square in frontend
    createNumberSquare(number);
    
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


// Function to log the number and update the statistics table
function createNumberSquare(number) {
    const container = document.getElementById("number-statistics");

    // Create a new square for the number
    const square = document.createElement("div");
    square.textContent = number;
    square.style.width = "40px";
    square.style.height = "40px";
    square.style.border = "2px solid #333";
    square.style.display = "flex";
    square.style.alignItems = "center";
    square.style.justifyContent = "center";
    square.style.fontSize = "18px";
    square.style.fontWeight = "bold";
    square.style.backgroundColor = "#f5f5f5";

    // Add the new square to the left of the current squares
    container.prepend(square);

    // Remove the oldest square if there are more than 8
    if (container.children.length > MAX_NUMBERS) {
        container.removeChild(container.lastChild);
    }
}


function resetTable(table) {
    const response = fetch(`/reset-table/${table}`);
    if (response.ok) {
        
    }
}
/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

const colors = { "red": [1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36], "black": [2, 4, 6, 8, 10, 11, 13, 15, 17, 20, 22, 24, 26, 28, 29, 31, 33, 35] };
const parity = (num) => num % 2 === 0 ? 'Even' : 'Odd';
const range = (num) => num >= 1 && num <= 18 ? 'Low' : 'High';
//const MAX_NUMBERS = 8;

// Function to log number and update tables
function logNumber(number) {
    
    // Determine color, parity, and range
    const color = colors.red.includes(number) ? 'Red' : colors.black.includes(number) ? 'Black' : 'Green';
    const parityValue = parity(number);
    const rangeValue = range(number);

    // Append data to respective tables
    appendToTable('number-table', number);
    appendToTable('color-table', color);
    appendToTable('parity-table', parityValue);
    appendToTable('range-table', rangeValue);
}

// Function to append data to table
function appendToTable(tableId, value) {
    const table = document.getElementById(tableId).querySelector('tbody');
    const row = document.createElement('tr');
    const cell = document.createElement('td');
    cell.textContent = value;
    row.appendChild(cell);
    table.appendChild(row);
}

// Function to reset all tables
function resetTables() {
    document.querySelectorAll("table tbody").forEach(tbody => tbody.innerHTML = "");
}