import yfinance as yf

holdings = {
  'AAPL': {'shares': 0.648, 'cost': 166.19},
  'QQQ':  {'shares': 0.279, 'cost': 174.91},
  'ITOT': {'shares': 0.598, 'cost': 90.23},
}

etfs = {
  'QQQ':  {'return': 0.18, 'fee': 0.0020, 'risk': 'High',      'focus': 'Nasdaq-100 Tech'},
  'VUG':  {'return': 0.16, 'fee': 0.0004, 'risk': 'High',      'focus': 'Broad Growth'},
  'VGT':  {'return': 0.22, 'fee': 0.0010, 'risk': 'Very High', 'focus': 'Tech Sector'},
  'SMH':  {'return': 0.25, 'fee': 0.0035, 'risk': 'Very High', 'focus': 'Semiconductors'},
  'ITOT': {'return': 0.10, 'fee': 0.0003, 'risk': 'Low',       'focus': 'Total Market'},
}

starting = 328
years = 5
monthly = 200

print('=' * 55)
print('   WEBULL CONNECTOR - FELDON PORTFOLIO TOOL')
print('=' * 55)

print()
print('--- LIVE PORTFOLIO ---')
total_value = 0
total_cost = 0
for ticker, data in holdings.items():
    stock = yf.Ticker(ticker)
    info = stock.info
    price = info.get('currentPrice') or info.get('regularMarketPrice') or info.get('navPrice')
    value = round(price * data['shares'], 2)
    gain = round(value - data['cost'], 2)
    total_value += value
    total_cost += data['cost']
    print(ticker, '| Price: $' + str(price), '| Value: $' + str(value), '| Gain: $' + str(gain))

print('Total Value: $' + str(round(total_value, 2)))
print('Total Gain: $' + str(round(total_value - total_cost, 2)))

print()
print('--- ETF COMPARISON - $328 over 5 years ---')
for t, d in etfs.items():
    v = starting * ((1 + d['return'] - d['fee']) ** years)
    print(t, '|', d['focus'], '| Risk:', d['risk'], '| 5yr: $' + str(round(v, 2)))

print()
print('--- GROWTH PROJECTION with $200/mo military pay ---')
for label, rate in [('Conservative 5pct', 0.05), ('Moderate 8pct', 0.08), ('Aggressive 12pct', 0.12)]:
    v = starting
    for m in range(years * 12):
        v = v * (1 + rate/12) + monthly
    print(label, '| 5yr value: $' + str(round(v, 2)))

print()
print('=' * 55)
print('Note: historical averages only, not financial advice')
print('=' * 55)
