from flask import Flask, render_template, request, jsonify
import math

app = Flask(__name__)

# Route to render the calculator page
@app.route('/')
def index():
    return render_template('index.html')

# API route to calculate the result
@app.route('/calculate', methods=['POST'])
def calculate():
    try:
        # Getting the input values from the frontend
        num1 = float(request.form['num1'])
        num2 = float(request.form['num2'])
        operator = request.form['operator']

        # Performing the calculation based on the operator
        if operator == 'add':
            result = num1 + num2
        elif operator == 'subtract':
            result = num1 - num2
        elif operator == 'multiply':
            result = num1 * num2
        elif operator == 'divide':
            if num2 != 0:
                result = num1 / num2
            else:
                result = "Error! Division by zero."
        elif operator == 'modulus':
            result = num1 % num2
        elif operator == 'exponent':
            result = num1 ** num2
        elif operator == 'sqrt':
            result = math.sqrt(num1)
        else:
            result = "Invalid operator"

        return jsonify(result=result)

    except Exception as e:
        return jsonify(result="Error! Invalid input.")

if __name__ == "__main__":
    app.run(debug=True)
