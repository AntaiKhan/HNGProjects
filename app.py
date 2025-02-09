from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def is_perfect(num):
    return num == sum(i for i in range(1, num) if num % i == 0)

def is_armstrong(num):
    digits = [int(d) for d in str(num)]
    power = len(digits)
    return num == sum(d ** power for d in digits)

def get_digit_sum(num):
    return sum(int(d) for d in str(num))

def get_fun_fact(num, properties):
    if "armstrong" in properties:
        return f"{num} is an Armstrong number because {' + '.join(f'{d}^{len(str(num))}' for d in str(num))} = {num}"
    if "perfect" in properties:
        return f"{num} is a perfect number because its divisors add up to itself."
    if "prime" in properties:
        return f"{num} is a prime number because it has only two divisors: 1 and itself."
    return f"{num} is an interesting number!"

@app.route('/math/<number>')
def math_properties(number):
    try:
        num = int(number)
    except ValueError:
        return jsonify({"number": number, "error": True}), 400

    properties = []
    if num % 2 != 0:
        properties.append("odd")
    else:
        properties.append("even")
    if is_prime(num):
        properties.append("prime")
    if is_perfect(num):
        properties.append("perfect")
    if is_armstrong(num):
        properties.append("armstrong")

    response = {
        "number": num,
        "is_prime": is_prime(num),
        "is_perfect": is_perfect(num),
        "properties": properties,
        "digit_sum": get_digit_sum(num),
        "fun_fact": get_fun_fact(num, properties),
    }
    return jsonify(response)

if __name__ == "__main__":
    app.run()


@app.route("/")
def home():
    return jsonify({"message": "Hello, AWS!"})
