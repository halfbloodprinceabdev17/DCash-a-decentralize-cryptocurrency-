from flask import Flask, jsonify
import random

app = Flask(__name__)
ports = {}


class Port:
    def __init__(self, port_number):
        self.port_number = port_number
        self.received_messages = []

    def send_message(self, message, recipient_port):
        recipient_port.receive_message(message)

    def receive_message(self, message):
        self.received_messages.append(message)

    def exchange_data(self):
        if len(ports) > 1:
            recipient_port = random.choice(list(ports.values()))
            while recipient_port == self:
                recipient_port = random.choice(list(ports.values()))
            message = f"Data from Port {self.port_number} to Port {recipient_port.port_number}"
            self.send_message(message, recipient_port)

    def get_received_messages(self):
        return self.received_messages


@app.route('/')
def index():
    return "Welcome to the Random Data Exchange Network!"


@app.route('/exchange_data')
def exchange_data():
    for port in ports.values():
        port.exchange_data()
    return "Data exchange complete!"


@app.route('/print_received_messages')
def print_received_messages():
    received_messages = {}
    for port_number, port in ports.items():
        received_messages[port_number] = port.get_received_messages()
    return jsonify(received_messages)


if __name__ == '__main__':
    num_ports = 5

    # Create ports
    for i in range(num_ports):
        port = Port(i)
        ports[i] = port

    # Run the Flask app
    app.run(debug=True)
