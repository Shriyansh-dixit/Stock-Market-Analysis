import mysql.connector
import time
import finnhub

conn = mysql.connector.connect(
    host="",  # Replace with your MySQL server IP
    user="",  # Replace with your MySQL username
    password="",  # Replace with your MySQL password
    database=""
)
cursor = conn.cursor()
finnhub_client = finnhub.Client(api_key="")

def update_stock_data(symbol):
    """Fetch stock data from Finnhub and insert into MySQL"""
    data = finnhub_client.quote(symbol)

    query = """
        INSERT INTO stocks (symbol, price, volume, change_percent)
        VALUES (%s, %s, %s, %s)
    """
    values = (
        symbol, 
        data.get("c", 0),  # Closing price
        data.get("v", 0),  # Volume
        data.get("dp", 0)  # Percent change
    )
    
    cursor.execute(query, values)
    conn.commit()
    print(f"Updated {symbol} data at {time.strftime('%Y-%m-%d %H:%M:%S')}")
    
    query = """ 
            
    """

# Fetch data for multiple stocks every minute
stock_symbols = ["AAPL", "GOOGL", "MSFT", "TSLA","AMZN","META"]

while True:
    for stock in stock_symbols:
        update_stock_data(stock)
    time.sleep(10)
