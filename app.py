from flask import Flask, jsonify,request
from classifier import get_prediction
app = Flask(__name__)
@app.route("/digits-predicted", methods = ["POST"]) # type: ignore
def data_predict():
    image = request.files.get("digit")
    prediction = get_prediction(image)
    return jsonify({
        "prediction":prediction
    }),200
if __name__ == "__main__":
    app.run(debug=True)