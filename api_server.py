# api_server.py

from flask import Flask, request, jsonify
from my_aria_dialog_api import MyAriaDialogAPI

app = Flask(__name__)

# Initialize the API class with the authentication token
AUTH_TOKEN = 'rand_aria_testing_7enidjsweiw'
api_instance = MyAriaDialogAPI(auth_token=AUTH_TOKEN)

@app.route('/open-connection', methods=['POST'])
def open_connection():
    auth_header = request.headers.get('Authorization')
    auth = {}
    if auth_header and auth_header.startswith('Bearer '):
        auth['api_key'] = auth_header.split(' ')[1]
    success, message = api_instance.OpenConnection(auth=auth)
    status_code = 200 if success else 401
    return jsonify({'success': success, 'message': message}), status_code

@app.route('/close-connection', methods=['POST'])
def close_connection():
    success, message = api_instance.CloseConnection()
    status_code = 200 if success else 400
    return jsonify({'success': success, 'message': message}), status_code

@app.route('/version', methods=['GET'])
def get_version():
    version = api_instance.GetVersion()
    return jsonify({'version': version}), 200

@app.route('/start-session', methods=['POST'])
def start_session():
    success, message = api_instance.StartSession()
    status_code = 200 if success else 400
    return jsonify({'success': success, 'message': message}), status_code

@app.route('/get-response', methods=['POST'])
def get_response():
    data = request.get_json()
    text = data.get('text', '')
    response = api_instance.GetResponse(text)
    if response['success']:
        return jsonify({'response': response['response']}), 200
    else:
        return jsonify({'success': False, 'response': response['response']}), 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
