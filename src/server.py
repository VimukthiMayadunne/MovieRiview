from flask import Flask, request, jsonify, Response
from flask_cors import CORS
from flask_json_schema import JsonSchema, JsonValidationError

from schemas.infoSchema import dataRecived

app = Flask(__name__)
CORS(app)
schema = JsonSchema(app)


@app.route("/")
def hello():
    return jsonify(isError=False, message="Welcome To Movie Review Classifier ", statusCode=200), 200


@app.errorhandler(JsonValidationError)
def validation_error(e):
    return jsonify({'error': e.message, 'errors': [validation_error.message for validation_error in e.errors]})


@app.route("/getTreatment", methods=['GET', 'POST'])
@schema.validate(dataRecived)
def treatment():
    if request.method == 'GET':
        return jsonify(isError=False, message="Success", statusCode=200), 200

    elif request.method == 'POST':
        data = request.json
        results = getRivewType(data)
        return jsonify(isError=False, message=results, statusCode=200), 200
    else:
        return jsonify(isError=True, message="Unauthorized method", statusCode=401), 401


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
