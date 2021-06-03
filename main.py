from forex_python.converter import CurrencyRates
c = CurrencyRates()
x = c.get_rates('USD')   # you can directly call get_rates('USD')
print(x)
