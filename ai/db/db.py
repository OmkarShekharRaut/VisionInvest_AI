import psycopg2
import os
from dotenv import load_dotenv

load_dotenv()  # Load environment variables

# Correctly fetch DATABASE_URL from environment variables
DATABASE_URL = os.getenv("postgresql://postgres:MoSo$123@localhost:5432/visioninvest_db")  

def connect_db():
    try:
        if not DATABASE_URL:
            raise ValueError("DATABASE_URL is not set in environment variables.")

        conn = psycopg2.connect(DATABASE_URL)
        return conn
    except Exception as e:
        print(f"Database connection error: {e}")
        return None
