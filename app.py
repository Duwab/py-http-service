from flask import Flask, jsonify, request
import subprocess

app = Flask(__name__)

@app.route('/ps')
def ps_command():
    try:
        ps_output = subprocess.check_output(['ps'])
        return ps_output
    except subprocess.CalledProcessError as e:
        return "Error executing 'ps' command: {}".format(e)

# Route to execute bash command
@app.route('/execute', methods=['GET'])
def execute_command():
    command = request.args.get('command')

    if not command:
        return jsonify({'error': 'command should be specified'}), 400

    try:
        result = subprocess.check_output(command, shell=True)
        return jsonify({'stdout': result})
    except subprocess.CalledProcessError as e:
        return jsonify({'error': 'error executing command'}), 500


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
