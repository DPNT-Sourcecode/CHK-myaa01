
from collections import Counter
# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    registered_skus = ('A', 'B', 'C', 'D')
    sku_prices = {
        'A': {
            'price': 50,
        },
        'B': {
            'price': 30,
        },
        'C': {
            'price': 20,
        },
        'D': {
            'price': 15,
        }
    }
    if not all(sku in registered_skus for sku in skus):
        return -1

    if len(skus) == 0:
        return 0

    for

