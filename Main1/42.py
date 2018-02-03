#Dictionary Calculator

stocks = {
    'GOOG' :434,
    'AMZN' :553,
    'FB'   :54,
    'MSFT' :23
}

#(434, GOOG) (553, AMZN)
min_price = min(zip(stocks.values(), stocks.keys()))
print(min_price)
