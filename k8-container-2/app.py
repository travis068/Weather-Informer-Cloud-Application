from flask import Flask, jsonify, request

import csv

app = Flask(__name__)
pvPath = '/rabia_PV_dir/'


@app.route('/')
def index():
    return {"message": "Container 2: App 2 Service Running."}, 200


@app.route('/get-temp', methods=['POST'])
def get_temperature():
    filename = request.json.get('file')
    result = {}
    try:
        # if filename is not None:
        name = request.json.get('name')
        with open(pvPath + filename, mode='r') as dat_file:
            csv_reader = csv.reader(dat_file, delimiter=',')
            for row in csv_reader:
                if row[0] == name:
                    result['file'] = filename
                    result['temperature'] = int(row[3])
            if not bool(result):
                return jsonify({'file': filename, 'error': 'Input file not in CSV format.'}), 400
            else:
                return jsonify(result), 200
    # else:
    #     return jsonify({'file': filename, 'error': 'Invalid JSON input.'}), 400
    except FileNotFoundError:
        return jsonify({'file': filename, 'error': 'File not found.'}), 400
    # except (csv.Error, IOError, OSError):
    #     return jsonify({'file': filename, 'error': 'Input file not in CSV format.'}), 400
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# if __name__ == "__main__":
#     app.run(port=6001, debug=True)
