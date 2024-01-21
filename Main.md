pip install pandas numpy matplotlib seaborn scikit-learn flask

from flask import Flask, render_template
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, r2_score
from io import BytesIO
import base64

app = Flask(__name__)

def plot_feature_importances(importances, features):
    indices = np.argsort(importances)
    plt.figure(figsize=(8, 6))
    plt.title('Feature Importances')
    plt.barh(range(len(indices)), importances[indices], color='b', align='center')
    plt.yticks(range(len(indices)), [features[i] for i in indices])
    plt.xlabel('Relative Importance')
    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    image_png = buffer.getvalue()
    buffer.close()
    graphic = base64.b64encode(image_png)
    graphic = graphic.decode('utf-8')
    return graphic

@app.route('/')
def index():
    # Load your data (replace with the path to your dataset)
    df = pd.read_csv('real_estate_data.csv')

    # Data preprocessing
    X = df.drop('ROI', axis=1)
    y = df['ROI']
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)

    # Train-test split
    X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)

    # Model training
    rf_model = RandomForestRegressor(n_estimators=100, random_state=42)
    rf_model.fit(X_train, y_train)
    y_pred = rf_model.predict(X_test)

    # Model evaluation
    mse = mean_squared_error(y_test, y_pred)
    r2 = r2_score(y_test, y_pred)
    results = {
        'mse': mse,
        'r2': r2
    }

    # Feature importance plot
    importances = rf_model.feature_importances_
    feature_graphic = plot_feature_importances(importances, X.columns)

    return render_template('index.html', results=results, feature_graphic=feature_graphic)

if __name__ == '__main__':
    app.run(debug=True)
