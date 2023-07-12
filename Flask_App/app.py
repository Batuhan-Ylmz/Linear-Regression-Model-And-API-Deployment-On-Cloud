from flask import Flask, render_template, request
import requests

app = Flask(__name__)
api_url = app.config.get('base-api-url') 

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    # Get the input height from the form
    height = float(request.form["Enter height in cm's"])
    
    response = requests.post('http://YOUR_PRIVATE_IP_ON_VIRT_MACH:5000/prediction', json = {"height": height})
    
    data = response.json()
    
    weight = float(data["weight"])
    # Prepare the prediction text
    prediction_text = f"The predicted weight for a height of {height} cm is {weight} kg."
    
    return render_template("index.html", prediction_text=prediction_text)

if __name__ == "__main__":
    app.run(host = "0.0.0.0" , port=80)