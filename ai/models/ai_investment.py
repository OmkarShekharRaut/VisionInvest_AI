import pandas as pd
import numpy as np
import joblib
import psycopg2
from sklearn.preprocessing import MinMaxScaler
from sklearn.ensemble import RandomForestRegressor
from db import connect_db

# Fetch data from PostgreSQL
def fetch_market_data():
    conn = connect_db()
    query = "SELECT date, close_price FROM stock_prices WHERE stock_id = 1 ORDER BY date"
    df = pd.read_sql(query, conn)
    conn.close()
    return df

df = fetch_market_data()

# Data Preprocessing
scaler = MinMaxScaler()
df["close_price_scaled"] = scaler.fit_transform(df[["close_price"]])

X = df.index.values.reshape(-1, 1)  # Use time-based index as feature
y = df["close_price_scaled"]

# Train Model
model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X, y)

# Save Model & Scaler
joblib.dump(model, "ai/model/investment_model.pkl")
joblib.dump(scaler, "ai/model/scaler.pkl")

print("Model trained and saved successfully!")
