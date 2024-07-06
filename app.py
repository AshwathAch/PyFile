from flask import Flask, request, render_template
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
import joblib
import os

app = Flask(__name__)

# File paths
EXCEL_FILE = 'data.xlsx'
MODEL_FILE_COLOUR = 'model_colour.pkl'
MODEL_FILE_PRICE = 'model_price.pkl'

# Load or create the dataset
if os.path.exists(EXCEL_FILE):
    data = pd.read_excel(EXCEL_FILE)
else:
    data = pd.DataFrame(columns=['period', 'price', 'colour', 'date', 'number'])

# Preprocess the data
def preprocess(data):
    # Encoding 'colour' field
    data['colour'] = data['colour'].map({'red': 0, 'green': 1})
    data['date'] = pd.to_datetime(data['date'])
    data['day'] = data['date'].dt.day
    data['month'] = data['date'].dt.month
    data['year'] = data['date'].dt.year
    return data.drop(columns=['date'])

# Train the model
def train_model(data):
    data = preprocess(data)
    X = data[['period', 'price', 'day', 'month', 'year', 'number']]
    y_colour = data['colour']
    y_price = data['price']
    
    X_train, X_test, y_train_colour, y_test_colour = train_test_split(X, y_colour, test_size=0.2, random_state=42)
    X_train, X_test, y_train_price, y_test_price = train_test_split(X, y_price, test_size=0.2, random_state=42)
    
    model_colour = RandomForestClassifier()
    model_price = RandomForestClassifier()
    
    model_colour.fit(X_train, y_train_colour)
    model_price.fit(X_train, y_train_price)
    
    joblib.dump(model_colour, MODEL_FILE_COLOUR)
    joblib.dump(model_price, MODEL_FILE_PRICE)

# Train model on startup
if len(data) > 0:
    train_model(data)

@app.route('/', methods=['GET', 'POST'])
def index():
    prediction_colour = None
    prediction_price = None

    if request.method == 'POST':
        # Handle new input row
        if 'period' in request.form:
            new_row = {
                'period': int(request.form['period']),
                'price': float(request.form['price']),
                'colour': request.form['colour'],
                'date': request.form['date'],
                'number': int(request.form['number'])
            }
            data.loc[len(data)] = new_row
            data.to_excel(EXCEL_FILE, index=False)
            train_model(data)

        # Predict next row
        period = int(request.form.get('period', 0))
        price = float(request.form.get('price', 0))
        date = request.form.get('date')
        number = int(request.form.get('number', 0))

        if period and price and date and number:
            date = pd.to_datetime(date)
            input_data = pd.DataFrame([{
                'period': period,
                'price': price,
                'day': date.day,
                'month': date.month,
                'year': date.year,
                'number': number
            }])
            
            model_colour = joblib.load(MODEL_FILE_COLOUR)
            model_price = joblib.load(MODEL_FILE_PRICE)
            
            prediction_colour = model_colour.predict(input_data)[0]
            prediction_colour = 'red' if prediction_colour == 0 else 'green'
            prediction_price = model_price.predict(input_data)[0]

    return render_template('index.html', prediction_colour=prediction_colour, prediction_price=prediction_price)

if __name__ == '__main__':
    app.run(debug=True)
