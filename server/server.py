from flask import Flask, jsonify
import os
import signal

app = Flask(__name__)

@app.route('/home', methods=['GET'])
def home():
    serverId = os.environ['SERVER_ID']
    output = {
        'message': f"Hello from Server: {serverId}",
        'status': 'successful'
    }
    return jsonify(output), 200

@app.route('/heartbeat', methods=['GET'])
def heartbeat():
    return jsonify({}), 200

@app.route('/shutdown', methods=['POST'])
def shutdown():
    print("Shutting down gracefully...")
    os.kill(os.getpid(), signal.SIGINT)
    return jsonify(message='Server shutting down...'), 200

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port='5000')
