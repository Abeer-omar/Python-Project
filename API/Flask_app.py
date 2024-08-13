from flask import Flask, request, jsonify
import json
from CaesarPackage import get_cipher


app = Flask(__name__)

@app.route('/', methods=['GET'])
def cipher():

    data = request.args.get('data')

    if not data:
        return jsonify({"error": "No params provided"}), 400

    try:
        params = json.loads(data)  # parse the JSON
    except(TypeError, json.JSONDecodeError):
        return jsonify({"error": "Invalid JSON"}), 400

    #Extract string, key and encryption flag
    string = params.get('string')
    encrypt = params.get('encrypt', True)
    key = params.get('key', None)

    if not string:
        return jsonify({"error": "No string provided"}), 400
    
    result = get_cipher(string, encrypt, key)
    return jsonify({"result": result})


if __name__ == '__main__':
    app.run(debug=True)
