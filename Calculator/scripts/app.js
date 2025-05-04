document.addEventListener('DOMContentLoaded', function() {
    const display = document.getElementById('display');
    const buttons = document.querySelectorAll('.button');
    let currentInput = '';
    let operator = '';
    let previousInput = '';

    buttons.forEach(button => {
        button.addEventListener('click', function() {
            const value = this.textContent;

            if (value === 'C') {
                currentInput = '';
                operator = '';
                previousInput = '';
                display.textContent = '0';
            } else if (value === '=') {
                if (currentInput && previousInput && operator) {
                    currentInput = eval(`${previousInput} ${operator} ${currentInput}`);
                    display.textContent = currentInput;
                    previousInput = currentInput;
                    operator = '';
                }
            } else if (['+', '-', '*', '/'].includes(value)) {
                if (currentInput) {
                    if (previousInput && operator) {
                        previousInput = eval(`${previousInput} ${operator} ${currentInput}`);
                    } else {
                        previousInput = currentInput;
                    }
                    currentInput = '';
                    operator = value;
                    display.textContent = `${previousInput} ${operator}`;
                }
            } else {
                currentInput += value;
                display.textContent = `${previousInput} ${operator} ${currentInput}`;
            }
        });
    });
});

function clearDisplay() {
    document.getElementById('display').value = '';
}

function appendToDisplay(value) {
    document.getElementById('display').value += value;
}

function calculateResult() {
    const display = document.getElementById('display');
    try {
        display.value = eval(display.value);
    } catch (error) {
        display.value = 'Error';
    }
}