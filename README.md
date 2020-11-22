# FizzBuzz webapp

Small web application that wraps the famous FizzBuzz problem into a nice REST API.

## Requirements

- Python 3.7

## Installation

`pip install -r requirements.txt`

## Run the app

### Development

```bash
export FLASK_APP=src/app.py
export FLASK_ENV=development
flask run
```

### Production

**DO NOT ACTUALLY USE THIS IN PRODUCTION, THIS IS SIMPLIFIED FOR DEMONSTRATION PURPOSES**
```bash
export FLASK_APP=src/app.py
export FLASK_ENV=production
flask run
```

### Unit tests
```bash
python -m unittest tests/test_fizzbuzz.py -v
```