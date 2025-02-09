from flask import Flask, request, jsonify
from flask_cors import CORS
import requests
import math

app = Flask(__name__)
CORS(app)

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True

def is_armstrong(num):
    digits = [int(digit) for digit in str(num)]
    power = len(digits)
    return sum(digit ** power for digit in digits) == num

def get_fun_fact(num):
    url = f"http://numbersapi.com/{num}/math"
    response = requests.get(url)
    return response.text if response.status_code == 200 else "No fun fact found"

@app.route('/api/classify-number', methods=['GET'])
def classify_number():
    number = request.args.get('number')

    if not number or not number.isdigit():
        return jsonify({"number": number, "error": True}), 400

    number = int(number)
    armstrong = is_armstrong(number)
    prime = is_prime(number)
    even = number % 2 == 0
    digit_sum = sum(map(int, str(number)))
    fun_fact = get_fun_fact(number)

    properties = []
    if armstrong:
        properties.append("armstrong")
    properties.append("even" if even else "odd")

    return jsonify({
        "number": number,
        "is_prime": prime,
        "is_perfect": False,  # No perfect number check required
        "properties": properties,
        "digit_sum": digit_sum,
        "fun_fact": fun_fact
    })

if __name__ == "__main__":
    app.run()
