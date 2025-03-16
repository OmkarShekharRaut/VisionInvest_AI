from flask import Flask, jsonify, request
import psycopg2
from db import connect_db
from model.predict import predict_price

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({"message": "AI Stock Prediction API is running!"})

@app.route("/predict/<symbol>", methods=["GET"])
def predict(symbol):
    conn = connect_db()
    cursor = conn.cursor()
    
    cursor.execute("SELECT id FROM stocks WHERE symbol = %s", (symbol,))
    stock = cursor.fetchone()
    
    if not stock:
        return jsonify({"error": "Stock not found"}), 404

    future_price = predict_price(30)  # Predict 30 days ahead
    return jsonify({"symbol": symbol, "predicted_price": future_price})

if __name__ == "__main__":
    app.run(debug=True, port=5000)
