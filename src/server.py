from flask import Flask, request, jsonify, Response
from flask_cors import CORS
from flask_json_schema import JsonSchema, JsonValidationError

from schemas.infoSchema import dataRecived
from src.classifier import loadModel

app = Flask(__name__)
CORS(app)
schema = JsonSchema(app)
model = loadModel()


@app.route("/")
def hello():
    return jsonify(isError=False, message="Welcome To Movie Review Classifier ", statusCode=200), 200


@app.errorhandler(JsonValidationError)
def validation_error(e):
    return jsonify({'error': e.message, 'errors': [validation_error.message for validation_error in e.errors]})


@app.route("/gettype", methods=['GET', 'POST'])
@schema.validate(dataRecived)
def treatment():
    if request.method == 'GET':
        return jsonify(isError=False, message="Success", statusCode=200), 200

    elif request.method == 'POST':
        data = request.json
        results = model.predict(data.get('review'))
        return jsonify(isError=False, message=results, statusCode=200), 200
    else:
        return jsonify(isError=True, message="Unauthorized method", statusCode=401), 401


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
