from flask import Flask, request, jsonify
import util

app = Flask(__name__)

@app.route('/get_fuel_names', methods=['GET'])
def get_fuel_names():
    response = jsonify({
        'fuels': util.get_fuel_names()
    })
    response.headers.add('Access-Control-Allow-Origin', '*')

    return response

@app.route('/predict_cardekho_price', methods=['GET','POST'])
def predict_cardekho_price():
    km_driven = int(request.form['km_driven'])
    fuel = request.form['fuel']
    mileage = int(request.form['mileage'])
    engine = int(request.form['engine'])
    seats = int(request.form['seats'])
    no_years = int(request.form['no_years'])

    response = jsonify({
        'estimated_Price': util.get_estimated_price(fuel,km_driven,mileage,engine,seats,no_years)
    })
    response.headers.add('Access-Control-Allow-Origin', '*')

    return response

if __name__ == "__main__":
    print("Starting Python Flask Server For Cardekho Price Prediction...")
    util.load_saved_artifacts()
    app.run()