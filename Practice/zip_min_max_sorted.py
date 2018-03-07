#min,max,sort of a dictionary

stocks = {
    'Goog':504,
    'AMZN':234,
    'FB':32,
    'APPLE':102
}

print(zip(stocks))
print(sorted(stocks))
print(sorted(zip(stocks.values(),stocks.keys())))
print(sorted(zip(stocks.keys(),stocks.values())))

print(min(zip(stocks.keys(),stocks.values())))
print(min(zip(stocks.values(),stocks.keys())))

print(max(zip(stocks.keys(),stocks.values())))
print(max(zip(stocks.values(),stocks.keys())))