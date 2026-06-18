stock_prices = {
    "AAPL": 180, "TSLA": 250, "GOOGL": 140, "AMZN": 175, "MSFT": 420
}

def build_portfolio():
    portfolio = {} # Just stores {symbol: quantity}
    print(f"--- Stock Portfolio Tracker ---\nAvailable: {', '.join(stock_prices)}\n")

    # The walrus operator (:=) assigns and checks the condition in one line
    while (symbol := input("Enter symbol (or 'done'): ").upper()) != 'DONE':
        if symbol not in stock_prices:
            print("Stock not found.")
            continue
            
        try:
            qty = int(input(f"Enter quantity for {symbol}: "))
            if qty >= 0:
                # .get() lets us add to existing shares if the user types the same stock twice
                portfolio[symbol] = portfolio.get(symbol, 0) + qty 
            else:
                print("Quantity cannot be negative.")
        except ValueError:
            print("Invalid number.")

    # Build a single report string to use for both printing and saving (DRY principle)
    report = "\n--- Portfolio Summary ---\n"
    for stock, qty in portfolio.items():
        report += f"{stock}: {qty} shares | Value: ${stock_prices[stock] * qty}\n"
    
    # Calculate the grand total in one clean line using a generator expression
    total = sum(stock_prices[s] * q for s, q in portfolio.items())
    report += f"\nTotal Investment Value: ${total}\n"

    print(report)

    # File saving
    if input("Save to file? (y/n): ").lower() == 'y':
        with open("portfolio_report.txt", "w") as f:
            f.write(report)
        print("Saved to 'portfolio_report.txt'.")

if __name__ == "__main__":
    build_portfolio()