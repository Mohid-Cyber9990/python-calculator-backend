from flask import Flask, request, jsonify
from calculator import Calculator

app = Flask(__name__)
calculator = Calculator()

@app.route('/add', methods=['POST'])
def add():
    data = request.json
    result = calculator.add(data['a'], data['b'])
    return jsonify(result=result)

@app.route('/subtract', methods=['POST'])
def subtract():
    data = request.json
    result = calculator.subtract(data['a'], data['b'])
    return jsonify(result=result)

@app.route('/multiply', methods=['POST'])
def multiply():
    data = request.json
    result = calculator.multiply(data['a'], data['b'])
    return jsonify(result=result)

@app.route('/divide', methods=['POST'])
def divide():
    data = request.json
    try:
        result = calculator.divide(data['a'], data['b'])
        return jsonify(result=result)
    except ZeroDivisionError:
        return jsonify(error="Division by zero is not allowed"), 400

if __name__ == '__main__':
    app.run(debug=True)