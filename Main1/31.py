#min,max,sorting of dictionary

stocks = {
    'GOOG' : 506.4,
    'FB' : 85.95,
    'AMZN' : 303.4,
    'YHOO' : 39.28,
    'AAPL' : 99.98
}

print(sorted(zip(stocks.values(),stocks.keys())))
#print(min(zip(stocks.values(),stocks.keys()))) #min wrt values
#print(min(zip(stocks.keys(),stocks.values()))) #min wrt keys

#print(max(zip(stocks.values(),stocks.keys()))) #max wrt values
#print(max(zip(stocks.keys(),stocks.values()))) #max wrt keys

#print(sorted(zip(stocks.values(),stocks.keys()))) #sorted wrt values
#print(sorted(zip(stocks.keys(),stocks.values()))) #sorted wrt keys
