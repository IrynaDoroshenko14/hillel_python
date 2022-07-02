coin = ('Bitcoin', 'Ether', 'Ripple', 'Litecoin')
code = ('BTC', 'ETH', 'XRP', 'LTC')


def tuples_to_dict(key_tuple, value_tuple):
    coin_code_dict = {}
    for key, value in zip(key_tuple, value_tuple):
        coin_code_dict[key] = value
    return coin_code_dict


new_dict = tuples_to_dict(coin, code)
print(new_dict)
