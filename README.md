# Stock-Portfolio
 Stock Portfolio Tracker is a tool or application that helps investors track and manage their stock investments. It shows the current value of stocks, calculates profit or loss, monitors portfolio performance, and provides real-time market updates, helping users make better investment decisions.

 # 📈 Stock Portfolio Tracker

## Description

Stock Portfolio Tracker is a simple Python-based application that helps users manage and track their stock investments. Users can add stocks from a predefined list, enter the number of shares they own, calculate the value of each holding, view the total portfolio value, and save the portfolio summary to a text file.

## Features

- Add stocks to a portfolio
- Enter quantity of shares
- Calculate stock-wise investment value
- Calculate total investment value
- Validate stock symbols
- Handle invalid inputs
- Save portfolio reports to a file

## Technologies Used

- Python 3
- Dictionaries
- Functions
- Loops
- Exception Handling
- File Handling

## Source Code

```python
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "AMZN": 175,
    "MSFT": 420
}

def build_portfolio():
    portfolio = {}

    print(f"--- Stock Portfolio Tracker ---\nAvailable: {', '.join(stock_prices)}\n")

    while (symbol := input("Enter symbol (or 'done'): ").upper()) != 'DONE':

        if symbol not in stock_prices:
            print("Stock not found.")
            continue

        try:
            qty = int(input(f"Enter quantity for {symbol}: "))

            if qty >= 0:
                portfolio[symbol] = portfolio.get(symbol, 0) + qty
            else:
                print("Quantity cannot be negative.")

        except ValueError:
            print("Invalid number.")

    report = "\n--- Portfolio Summary ---\n"

    for stock, qty in portfolio.items():
        report += f"{stock}: {qty} shares | Value: ${stock_prices[stock] * qty}\n"

    total = sum(stock_prices[s] * q for s, q in portfolio.items())

    report += f"\nTotal Investment Value: ${total}\n"

    print(report)

    if input("Save to file? (y/n): ").lower() == 'y':
        with open("portfolio_report.txt", "w") as f:
            f.write(report)

        print("Saved to 'portfolio_report.txt'.")

if __name__ == "__main__":
    build_portfolio()
```

## How to Run

1. Save the code as `stock.py`
2. Open a terminal in the project directory.
3. Run:

```bash
python stock.py
```

## Example Output

```text
--- Stock Portfolio Tracker ---
Available: AAPL, TSLA, GOOGL, AMZN, MSFT

Enter symbol (or 'done'): GOOGL
Enter quantity for GOOGL: 140
Enter symbol (or 'done'): done

--- Portfolio Summary ---
GOOGL: 140 shares | Value: $19600

Total Investment Value: $19600

Save to file? (y/n): y
Saved to 'portfolio_report.txt'.
```

## Project Structure

```text
Stock-Portfolio-Tracker/
│
├── stock.py
├── README.md
└── portfolio_report.txt
```

## Future Enhancements

- Real-time stock prices using APIs
- Portfolio profit/loss tracking
- Graphical User Interface (GUI)
- Database integration
- Portfolio performance charts

## Author

Developed as a Python mini-project for learning stock portfolio management, file handling, and data processing.
