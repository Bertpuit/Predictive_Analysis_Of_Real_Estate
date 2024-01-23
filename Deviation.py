import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, r2_score

# Load your data
df = pd.read_csv('real_estate_data.csv')

# One-hot encode the categorical variables
df_encoded = pd.get_dummies(df, drop_first=True)

# Preprocessing
X = df_encoded.drop('ROI', axis=1)
y = df_encoded['ROI']

# Standardize the features
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
deviations = y_test - y_pred

# Create a DataFrame for easier visualization
deviation_df = pd.DataFrame({
    'Data Point Index': y_test.index,
    'Actual': y_test,
    'Predicted': y_pred,
    'Deviation': deviations
})

# Sort the DataFrame by Deviation in ascending order
deviation_df = deviation_df.sort_values(by='Deviation', ascending=True)

# Print the sorted DataFrame
print(deviation_df)


# Print the DataFrame
print(deviation_df)
