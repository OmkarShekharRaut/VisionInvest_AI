import psycopg2
from db import connect_db

def insert_stock(symbol, name):
    """Insert a new stock into the database."""
    conn = connect_db()
    cursor = conn.cursor()
    
    try:
        cursor.execute("INSERT INTO stocks (symbol, name) VALUES (%s, %s) ON CONFLICT DO NOTHING", (symbol, name))
        conn.commit()
        print(f"Stock {symbol} ({name}) inserted successfully!")
    except Exception as e:
        print(f"Error inserting stock: {e}")
    
    cursor.close()
    conn.close()

def main():
    """Allow users to insert stock data manually."""
    while True:
        symbol = input("Enter stock symbol (e.g., AAPL): ").strip().upper()
        name = input("Enter stock name (e.g., Apple Inc.): ").strip()

        if symbol and name:
            insert_stock(symbol, name)
        else:
            print("Stock symbol and name cannot be empty!")

        more = input("Do you want to add another stock? (yes/no): ").strip().lower()
        if more != 'yes':
            break

if __name__ == "__main__":
    main()