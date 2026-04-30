import yfinance as yf

holdings = {
  'AAPL': {'shares': 0.64806, 'cost': 166.27},
  'ITOT': {'shares': 0.27842, 'cost': 40.25},
  'QQQ':  {'shares': 0.16641, 'cost': 100.00},
}

watch = ['QQQ', 'SPY', 'NVDA', 'SOFI', 'TSLA', 'PLTR', 'AMD', 'SMH']

print('=' * 60)
print('   WEBULL CONNECTOR - FELDON PORTFOLIO TOOL')
print('=' * 60)

print()
print('--- LIVE PORTFOLIO ---')
total_value = 0
total_cost = 0
for ticker, data in holdings.items():
    info = yf.Ticker(ticker).info
    price = info.get('currentPrice') or info.get('regularMarketPrice') or info.get('navPrice')
    value = round(price * data['shares'], 2)
    gain = round(value - data['cost'], 2)
    total_value += value
    total_cost += data['cost']
    print(ticker + ' | $' + str(price) + ' | Value: $' + str(value) + ' | Gain: $' + str(gain))
print('Total: $' + str(round(total_value, 2)) + ' | Total Gain: $' + str(round(total_value - total_cost, 2)))

print()
print('--- TOP RECOMMENDATIONS ---')
print('BEST PUT PLAY:  SOFI $15 put ~ $13/contract | needs -$1.16 drop')
print('BEST CALL PLAY: SOFI $17.50 call ~ $10/contract | needs +$1.30 rise')
print('BEST ETF PLAY:  NVDA $195 put ~ $92/contract | earnings volatility')
print('SAFEST PLAY:    SPY $716 put ~ $156/contract | most liquid market')
print('PAPER TRADE:    Start with SOFI - cheapest premiums, volatile enough to learn')

print()
print('--- CALLS SCREENER (cheap upside plays) ---')
for ticker in watch:
    try:
        stock = yf.Ticker(ticker)
        price = stock.info.get('currentPrice') or stock.info.get('regularMarketPrice')
        exps = stock.options
        exp = exps[1] if len(exps) > 1 else exps[0]
        calls = stock.option_chain(exp).calls
        cheap = calls[(calls['strike'] > price) & (calls['lastPrice'] <= 3)].head(2)
        if cheap.empty:
            continue
        print(ticker + ' | $' + str(round(price, 2)) + ' | ' + exp)
        for _, row in cheap.iterrows():
            print('  Call $' + str(row['strike']) + ' | Cost $' + str(round(row['lastPrice']*100,2)) + ' | Needs +$' + str(round(row['strike']-price,2)) + ' | Vol: ' + str(int(row['volume'])))
    except:
        pass

print()
print('--- PUTS SCREENER (cheap downside plays) ---')
for ticker in watch:
    try:
        stock = yf.Ticker(ticker)
        price = stock.info.get('currentPrice') or stock.info.get('regularMarketPrice')
        exps = stock.options
        exp = exps[1] if len(exps) > 1 else exps[0]
        puts = stock.option_chain(exp).puts
        cheap = puts[(puts['strike'] < price) & (puts['lastPrice'] <= 3)].tail(2)
        if cheap.empty:
            continue
        print(ticker + ' | $' + str(round(price, 2)) + ' | ' + exp)
        for _, row in cheap.iterrows():
            print('  Put $' + str(row['strike']) + ' | Cost $' + str(round(row['lastPrice']*100,2)) + ' | Needs -$' + str(round(price-row['strike'],2)) + ' | Vol: ' + str(int(row['volume'])))
    except:
        pass

print()
print('=' * 60)
print('Not financial advice - paper trade first always')
print('=' * 60)
