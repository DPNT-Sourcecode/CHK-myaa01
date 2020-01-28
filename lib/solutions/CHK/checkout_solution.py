
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
    special_offers = {
        'A': {
            'amount': 3,
            'offer_price': 130,
        },
        'B': {
            'amount': 2,
            'offer_price': 45,
        }
    }
    if not all(sku in registered_skus for sku in skus):
        return -1

    if len(skus) == 0:
        return 0

    letter_counts = Counter(skus)
    price = 0
    for letter, count in letter_counts.items():
        if special_offers[letter]:
            set_amount = special_offers[letter]['amount']
            set_frequency, count = divmod(count, set_amount)
            price += (special_offers[letter]['offer_price'] * set_frequency)
        price += (sku_prices[letter]['price'] * count)

    return price





