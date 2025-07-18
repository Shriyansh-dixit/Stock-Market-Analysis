import mysql.connector
import matplotlib.pyplot as plt
import pandas as pd

def fetch_stock_data(symbol="AAPL"):
    # Connect to MySQL database
    conn = mysql.connector.connect(
        host="",
        user="",
        password="",
        database=""
    )
    cursor = conn.cursor()
    
    # Fetch last 10 records for the given symbol
    query = """
    SELECT timestamp, price FROM stocks
    WHERE symbol = %s
    ORDER BY timestamp DESC
    LIMIT 10
    """
    cursor.execute(query, (symbol,))
    data = cursor.fetchall()
    
    # Close connection
    cursor.close()
    conn.close()
    
    return data

def plot_stock(symbol="AAPL"):
    data = fetch_stock_data(symbol)
    
    if not data:
        print("No data found for symbol:", symbol)
        return
    
    # Convert to DataFrame for better handling
    df = pd.DataFrame(data, columns=["Date", "Close Price"])
    df.sort_values("Date", inplace=True)  # Ensure chronological order
    
    # Plot the line graph
    plt.figure(figsize=(10, 5))
    plt.plot(df["Date"], df["Close Price"], marker='o', linestyle='-')
    plt.xlabel("Date")
    plt.ylabel("Close Price")
    plt.title(f"Stock Price Trend for {symbol}")
    plt.xticks(rotation=45)
    plt.grid()
    plt.show()

# Example usage
plot_stock("AAPL")
