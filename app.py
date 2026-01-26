from flask import Flask
import os, sys
from src.exeption import CustmeException
from src.logger import logging

app =  Flask(__name__)

@app.route('/', methods = ['GET', 'POST'])
def index():
    try:
        raise Exception("we are testing")
    except Exception as e:
        abc = CustmeException(e,sys)
        logging.info(abc.error_message)
        return "Welcome to my ml model"

if __name__ == "__main__":
    app.run(debug=True)
