import requests
import os.path

from flask import Flask, jsonify, request

app = Flask(__name__)
pvPath = '/rabia_PV_dir/'  # On local = '../../../rabia_PV_dir/'


@app.route('/')
def index():
    return {"message": "Container 1: App 1 Service Running."}, 200


@app.route('/store-file', methods=['POST'])
def store_file():
    try:
        file = request.json.get('file')
        if file is None:
            return jsonify({'file': None, 'error': 'Invalid JSON input.'}), 400
        else:
            try:
                data = request.json.get('data')
                completeName = os.path.join(pvPath, file)
                print(completeName)
                fp = open(completeName, 'w')
                fp.write(data)
                fp.close()
                return jsonify({'file': file, 'message': 'Success.'}), 200
            except (IOError, OSError):
                return jsonify({'file': file, 'error': 'Error while storing the file to the storage.'}), 400
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@app.route('/get-temperature', methods=['POST'])
def get_temperature():
    try:
        data = request.json
        file = data.get('file')
        if file is None:
            return jsonify({'file': None, 'error': 'Invalid JSON input.'}), 400
        else:
            response = requests.post('http://container-2-service:6001/get-temp', json=data)
            return response.json()
    except Exception as e:
        return jsonify({'error': str(e)}), 500


# if __name__ == '__main__':
#      app.run(port=6000, debug=True)
