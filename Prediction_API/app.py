from flask import Flask, jsonify, request
import joblib
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)

# Load the machine learning model
model = joblib.load("model.pkl")

class Prediction(Resource):
    def post(self):
        if request.is_json:
            data = request.get_json()
            height = float(data["height"])
        else:
            height = float(request.form["Enter height in cm's"])

        # Make a prediction using the loaded model
        weight = model.predict([[height]])

        # Round the weight to two decimal places
        weight = round(weight[0], 2)

        # Prepare the prediction response
        response = {"height": height, "weight": weight}

        # Return the prediction as a JSON response
        return jsonify(response)
    
api.add_resource(Prediction,"/prediction")


if __name__ == "__main__":
    app.run(host = "0.0.0.0", port = 5000)