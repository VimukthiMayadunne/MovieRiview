from flask import Flask, request, jsonify, Response, render_template
from flask_cors import CORS
from flask_json_schema import JsonSchema, JsonValidationError

from schemas.infoSchema import dataRecived
from src.classifier import loadModule

app = Flask(__name__)
CORS(app)
schema = JsonSchema(app)
model = loadModule()


@app.route("/")
def root():
    return render_template('home.html')


@app.errorhandler(JsonValidationError)
def validation_error(e):
    return jsonify({'error': e.message, 'errors': [validation_error.message for validation_error in e.errors]})


@app.route("/gettype", methods=['GET', 'POST'])
@schema.validate(dataRecived)
def treatment():
    if request.method == 'GET':
        review = [request.args.get('review')]
        results = model.predict(review)
        response = results.tolist()
        value= 'Positive' if response[0] == 'pos' else 'Negative'
        return render_template('response.html', movie=request.args.get('movie'), type=value,
                               review=request.args.get('review'))

    elif request.method == 'POST':
        data = request.json
        review = [data.get('review')]
        results = model.predict(review)
        response = results.tolist()
        print(response)
        return jsonify(isError=False, message=response[0], statusCode=200), 200
    else:
        return jsonify(isError=True, message="Unauthorized method", statusCode=401), 401


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
    # from waitress import serve
    # serve(app, host="0.0.0.0", port=8080)
