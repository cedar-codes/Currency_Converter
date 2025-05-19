# Currency_Converter

# How to Request Data:
Uses ZeroMQ to create a communication pipeline socket.
Requires an API key from UniRate API:
* API is free with unlimited calls: https://unirateapi.com/ *

context = zmq.Context()
    socket = context.socket(zmq.REQ)
    socket.connect("tcp://localhost:7777")
    print("Server connecting...")

test_input = {
    "api_key": API_KEY,
    "from": "USD",
    "to": "EUR",
    "amount": 100.00
}

socket.send_json(test_input)

# How to Receive Data:
Set up a ZeroMQ socket in the microservice (currency_converter.py):
context = zmq.Context()
    socket = context.socket(zmq.REP)
    socket.bind("tcp://localhost:7777")

Receives data as JSON object from Main Program (test_service.py).
data = socket.recv_json()

Makes an API call to receive the currency exchange rate:
response = requests.get(url, params=api_params)
(api_params is the JSON data received, but does not include the amount to be converted)

Then, sends JSON object through socket:
converted_currency = {
                "from": data["from"],
                "to": data["to"],
                "amount": data["amount"],
                "rate": response_data["rate"],
                "converted_amount": rate * data["amount"]
            }
            
socket.send_json(converted_currency)

Back in the Main Program, data is communicated back through the pipeline by calling:
message = socket.recv_json()

# UML Diagram:

![Microservice A UML ](https://github.com/user-attachments/assets/e163d6e5-85b6-4b75-aa60-160a1716789f)

# Communication Contract:
