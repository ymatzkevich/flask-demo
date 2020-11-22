from flask import Flask, jsonify
from .fizzbuzz import fizzbuzz_1_to_number

app = Flask(__name__)


@app.route('/fizzbuzz/<int:number>', methods=["GET"])
def get_fizzbuzz(number: int):
    return jsonify(fizzbuzz_1_to_number(number))
