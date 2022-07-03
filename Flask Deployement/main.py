from flask import Flask, render_template, request
import pandas as pd
import numpy as np
import joblib

housing_df = pd.read_excel('C://Users//anike//Zep Analytics//Real Estate Analysis//MagicBricks Cleaned (Excel).xlsx')
cities_list = list(np.sort(housing_df['City'].unique()))
states_list = list(np.sort(housing_df['State/Territory'].unique()))
tiers_list = list(np.sort(housing_df['Tier'].unique()))
transaction_list = list(np.sort(housing_df['Transaction'].unique()))
furnishing_list = list(np.sort(housing_df['Furnishing'].unique()))
status_list = list(np.sort(housing_df['Status'].unique()))

app = Flask(__name__)


@app.route('/')
def home_page():
    prediction = "₹ 0.00"
    return render_template("index.html",
                           price=prediction,
                           cities=cities_list,
                           states=states_list,
                           tiers=tiers_list,
                           trans=transaction_list,
                           furnish=furnishing_list,
                           status=status_list)


@app.route('/predict', methods=["GET", "POST"])
def predict():
    if request.method == 'POST':
        input_df = pd.DataFrame(index=[0])
        input_df['Bedrooms'] = int(request.form.get('Bedrooms'))
        input_df['Bathroom'] = int(request.form.get('Bathrooms'))
        input_df['Area(sqft)'] = float(request.form.get('Area'))
        input_df['Latitude'] = float(request.form.get('Latitude'))
        input_df['Longitude'] = float(request.form.get('Longitude'))
        input_df['Price per sqft'] = float(request.form.get('Price per sqft'))
        for t in tiers_list:
            if t == request.form.get('Tier'):
                input_df['Tier_' + t] = 1
            else:
                input_df['Tier_' + t] = 0
        for s in states_list:
            if s == request.form.get('State/Territory'):
                input_df['State/Territory_' + s] = 1
            else:
                input_df['State/Territory_' + s] = 0
        for t in transaction_list:
            if t == request.form.get('Transaction'):
                input_df['Transaction_' + t] = 1
            else:
                input_df['Transaction_' + t] = 0
        for f in furnishing_list:
            if f == request.form.get('Furnishing'):
                input_df['Furnishing_' + f] = 1
            else:
                input_df['Furnishing_' + f] = 0
        for s in status_list:
            if s == request.form.get('Status'):
                input_df['Status_' + s] = 1
            else:
                input_df['Status_' + s] = 0

        #input_df.to_csv('Input_df.csv', index=False)
        model = joblib.load('GradientBoosting (Price Predictor).joblib')
        pred = np.round(model.predict(input_df)[0], 2)
        if pred > 100:
            prediction = '₹ ' + str(round(pred / 100, 2)) + ' Cr'
        else:
            prediction = '₹ ' + str(pred) + ' Lacs'

    return render_template("index.html",
                           price=prediction,
                           cities=cities_list,
                           states=states_list,
                           tiers=tiers_list,
                           trans=transaction_list,
                           furnish=furnishing_list,
                           status=status_list)


if __name__ == '__main__':
    app.run(debug=True)
