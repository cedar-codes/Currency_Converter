# connects REQ socket to localhost:7777
import json

from flask import Flask
import zmq
from dotenv import load_dotenv

import os
import time

app = Flask(__name__)
load_dotenv()
API_KEY = os.getenv("API_KEY")


@app.route('/')
def receive_message():
    """ Uses ZeroMQ to create a socket to build a communication pipeline.
    test_input is a JSON object with your API_KEY, the currency from,
    the currency to, and the amount to be converted.
    Receives a JSON object with the above information, plus the exchange
    rate and the amount converted into the desired currency.
    """
    context = zmq.Context()
    socket = context.socket(zmq.REQ)
    socket.connect("tcp://localhost:7777")
    print("Server connecting...")

    #test_input = {
    #    "api_key": API_KEY,
   #     "from": "USD",
   #     "to": "EUR",
   #     "amount": 100.00
   # }
    
    test_input = {
        "api_key": API_KEY,
        "from": "MXN",
        "to": "JPY",
        "amount": 100.00
    }
    test_from = test_input["from"]
    test_to = test_input["to"]
    test_amount = test_input["amount"]
    print("Sending currency converter request to microservice..." +
          f"{test_from}" + " to" + f" {test_to}" +
          f" amount: {test_amount:.2f}")

    socket.send_json(test_input)

    print("Receiving converted currency...")

    message = socket.recv_json()
    print("Received converted currency and exchange rate: \n"
          + f"converted amount = {message['converted_amount']:.2f}"
          + f" exchange rate = {message['rate']}")
    return message


if __name__ == '__main__':
    app.run(port=5000)
