portfolio = {
  'AAPL': {'unrealized': 8.72, 'cumulative': 15.25},
  'QQQ':  {'unrealized': 9.94, 'cumulative': 10.25},
  'ITOT': {'unrealized': 3.03, 'cumulative': 3.35},
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
print('--- CURRENT HOLDINGS ---')
total_gain = sum(s['unrealized'] for s in portfolio.values())
for stock, data in portfolio.items():
    print(stock, '| Unrealized: $' + str(data['unrealized']), '| Total Gain: $' + str(data['cumulative']))
print('Total Unrealized Gain: $' + str(round(total_gain, 2)))

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
