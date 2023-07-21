from flask import Flask, jsonify, request
import subprocess
import re

app = Flask(__name__)

@app.route('/ps')
def ps_command():
    try:
        ps_output = subprocess.check_output(['ps'])
        return ps_output
    except subprocess.CalledProcessError as e:
        return "Error executing 'ps' command: {}".format(e)

# Route to execute bash command
# @app.route('/execute', methods=['GET'])
# def execute_command():
#     command = request.args.get('command')

#     if not command:
#         return jsonify({'error': 'command should be specified'}), 400

#     try:
#         result = subprocess.check_output(command, shell=True)
#         return jsonify({'stdout': result})
#     except subprocess.CalledProcessError as e:
#         return jsonify({'error': 'error executing command'}), 500

# Route to execute service action
@app.route('/services/<string:serviceName>', methods=['POST'])
def service_action(serviceName):
    action = request.args.get('action')

    if not serviceName:
        return jsonify({'error': 'serviceName should be specified'}), 400

    if not re.match(r'^[\w-]+$', serviceName):
        return "Invalid serviceName. Only alphanumeric characters, underscore, and dash are allowed.", 400

    if not action:
        return jsonify({'error': 'action should be specified'}), 400

    if not re.match(r'^[\w-]+$', action):
        return "Invalid action. Only alphanumeric characters, underscore, and dash are allowed.", 400

    command = "service {} {}".format(serviceName, action)
    try:
        result = subprocess.check_output(command, shell=True)
        return jsonify({'stdout': result})
    except subprocess.CalledProcessError as e:
        return jsonify({'error': 'error executing command'}), 500


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
