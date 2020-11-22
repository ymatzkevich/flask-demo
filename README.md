# FizzBuzz webapp

Small web application that wraps the famous FizzBuzz problem into a nice REST API.

## Requirements

- Python 3.7

## Installation

`pip install -r requirements.txt`

## Run the app

Here is how to run the app in both development and production mode.

### Development

```bash
export FLASK_APP=src/app.py
export FLASK_ENV=development
flask run
```

The development app should be available on port 5000:
`curl locahost:5000/api/fizzbuzz/13`

### Production

**DO NOT ACTUALLY USE THIS IN PRODUCTION, THIS IS SIMPLIFIED FOR DEMONSTRATION PURPOSES**
```bash
export FLASK_APP=src/app.py
export FLASK_ENV=production
flask run
```

The development app should be available on port 5000:
`curl locahost:5000/api/fizzbuzz/13`

## Unit tests
To run the small test suite, use:
```bash
python -m unittest tests/test_fizzbuzz.py -v
```