from flask import Flask, jsonify
from .fizzbuzz import fizzbuzz_1_to_number
from .palindrome import palindrome

app = Flask(__name__)


@app.route('/api/fizzbuzz/<int:number>', methods=["GET"])
def get_fizzbuzz(number: int):
    return jsonify(fizzbuzz_1_to_number(number))

@app.route('/api/palindrome/<int:number>', methods=["GET"])
def get_palindrome(number: int):
    return jsonify(palindrome(number))
