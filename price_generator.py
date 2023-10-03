import psycopg2
from datetime import datetime, timedelta
import random
import time

# Database connection parameters
db_params = {
    "dbname": "postgres",
    "user": "postgres",
    "password": "postgres",
    "host": "localhost",
    "port": "5433"
}

# Create a connection to the PostgreSQL database
conn = psycopg2.connect(**db_params)

# Create a cursor
cur = conn.cursor()

# Specify the stock symbol and start timestamp
symbol = "AAPL"  # Replace with the stock symbol
start_timestamp = datetime(2023, 1, 1)

# Generate and insert stock price data for 365 days
for i in range(100):
    timestamp = start_timestamp + timedelta(days=i)
    open_price = random.uniform(100, 200)
    high_price = open_price + random.uniform(0, 10)
    low_price = open_price - random.uniform(0, 10)
    close_price = random.uniform(low_price, high_price)
    volume = random.randint(1000000, 5000000)
    time.sleep(1)
    print(f"Iteration : {i}")
    # Insert data into the prices table
    id = cur.execute(
        """
        INSERT INTO stock_prices.prices (symbol, timestamp, open, high, low, close, volume)
        VALUES (%s, %s, %s, %s, %s, %s, %s) returning id
        """,
        (symbol, timestamp, open_price, high_price, low_price, close_price, volume),
    )
    conn.commit()
    print(id)
# Commit the transaction and close the cursor and connection
cur.close()
conn.close()
