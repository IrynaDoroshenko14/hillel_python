coin = ('Bitcoin', 'Ether', 'Ripple', 'Litecoin')
code = ('BTC', 'ETH', 'XRP', 'LTC')

coin_code_dict = {}
for key, value in zip(coin, code):
    coin_code_dict[key] = value

print(coin_code_dict)
