function appendToDisplay(value) {
    document.getElementById("display").value += value;
}

function clearDisplay() {
    document.getElementById("display").value = '';
}

function calculateResult() {
    var display = document.getElementById("display");
    try {
        // Handle the square root operation properly
        if (display.value.includes('Math.sqrt(')) {
            display.value = display.value.replace('Math.sqrt(', '');
            display.value = Math.sqrt(eval(display.value));
        } else {
            display.value = eval(display.value);
        }
    } catch (error) {
        display.value = 'Error';
    }
}
