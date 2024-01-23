import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, r2_score

# Load your data
df = pd.read_csv('real_estate_data.csv')

# Preprocessing
X = df.drop('ROI', axis=1)
y = df['ROI']
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Splitting the dataset
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)

# Model training
rf_model = RandomForestRegressor(n_estimators=100, random_state=42)
rf_model.fit(X_train, y_train)

# Predicting
y_pred = rf_model.predict(X_test)

# Calculating deviations
deviations = y_pred - y_test
deviation_df = pd.DataFrame({'Actual': y_test, 'Predicted': y_pred, 'Deviation': deviations})

# Display the deviations for each prediction
print(deviation_df)
