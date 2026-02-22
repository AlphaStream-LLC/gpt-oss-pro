from mcp.server.fastmcp import FastMCP

# Initialize FastMCP server for Finance
mcp = FastMCP("finance")

@mcp.tool()
async def get_stock_price(symbol: str) -> str:
    """Get the current stock price for a given symbol."""
    # Simulated data
    prices = {
        "AAPL": "150.00",
        "GOOGL": "2800.00",
        "MSFT": "300.00",
        "TSLA": "900.00"
    }
    return f"The current price of {symbol} is ${prices.get(symbol.upper(), 'UNKNOWN')}"

@mcp.tool()
async def get_portfolio_balance(account_id: str) -> str:
    """Get the balance of a specific portfolio account."""
    # Simulated data
    if account_id == "acc_12345":
        return "Portfolio Balance: $1,250,000.00"
    return "Account not found."

if __name__ == "__main__":
    mcp.run()
