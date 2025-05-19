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
- For which teammate did you implement “Microservice A”?
    - Annmarie Geiger

- What is the current status of the microservice? 
    - Working and fully functioning!

- If the microservice isn’t done, which parts aren’t done and when will they be done?
    - Done, but can help with implementing or if different features wanted.

- How is your teammate going to access your microservice? Should they get your code from GitHub (if so, provide a link to your public or private repo)? Should they run your code locally? Is your microservice hosted somewhere? Etc.
    - Link to GitHub repository: https://github.com/cedar-codes/Currency_Converter
    - Can be run locally by running the following commands in two separate terminals:
        - Start the microservice first by running: python converter_service.py
        - To start the main program, run: python test_service.py
        - These programs require installation of Flask, ZeroMQ, Python, requests, and dotenv.
              - Can be installed by running  python.exe -m pip install ** (after the word install, type the program to be installed) **
              - example:  python.exe -m pip install flask
      
- If your teammate cannot access/call YOUR microservice, what should they do? Can you be available to help them? What’s your availability?
    - I am available after 5PM EST, but can be available to help if you let me know. 

- If your teammate cannot access/call your microservice, by when do they need to tell you? Provide a specific date to ensure they have a clear deadline.
    - By 5/22 would be great!

- Is there anything else your teammate needs to know? Anything you’re worried about? Any assumptions you’re making? Any other mitigations / backup plans you want to mention or want to discuss with your teammate?
    - The test Main Program is written in Python, but ideally the Main Program can be in any language, thanks to using ZeroMQ sockets. There is documentation for changing it to other languages (like JavaScript) at https://zguide.zeromq.org/docs/chapter1/#A-Minor-Note-on-Strings. 
