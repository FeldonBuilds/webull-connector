import yfinance as yf
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("Feldon Portfolio")

holdings = {
  'AAPL': {'shares': 0.648, 'cost': 166.19},
  'QQQ':  {'shares': 0.279, 'cost': 174.91},
  'ITOT': {'shares': 0.598, 'cost': 90.23},
}

@mcp.tool()
def get_portfolio() -> str:
    """Get live portfolio values and gains"""
    result = "LIVE PORTFOLIO\n" + "-" * 45 + "\n"
    total_value = 0
    total_cost = 0
    for ticker, data in holdings.items():
        info = yf.Ticker(ticker).info
        price = info.get('currentPrice') or info.get('regularMarketPrice') or info.get('navPrice')
        value = round(price * data['shares'], 2)
        gain = round(value - data['cost'], 2)
        total_value += value
        total_cost += data['cost']
        result += f"{ticker} | Price: ${price} | Value: ${value} | Gain: ${gain}\n"
    result += f"Total Value: ${round(total_value, 2)}\n"
    result += f"Total Gain: ${round(total_value - total_cost, 2)}\n"
    return result

@mcp.tool()
def get_price(ticker: str) -> str:
    """Get live price for any stock or ETF"""
    info = yf.Ticker(ticker.upper()).info
    price = info.get('currentPrice') or info.get('regularMarketPrice') or info.get('navPrice')
    name = info.get('longName', ticker)
    return f"{name} ({ticker.upper()}): ${price}"

if __name__ == "__main__":
    mcp.run()
