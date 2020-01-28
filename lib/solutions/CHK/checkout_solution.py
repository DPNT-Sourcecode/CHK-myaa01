
from collections import Counter
# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    registered_skus = ('A', 'B', 'C', 'D', 'E')
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
        },
        'E': {
            'price': 40,
        }
    }
    special_offers = {
        'A': {
            3: 130,
            5: 200,
        },
        'B': {
            'amount': 2,
            'offer_price': 45,
        }
    }
    if not all(sku in sku_prices for sku in skus):
        return -1

    if len(skus) == 0:
        return 0

    letter_counts = Counter(skus)
    price = 0
    if letter == 'E':
        count = letter_counts[letter]
        set_frequency, count = divmod(count, 2)

        if letter_counts['B'] > 0:
            letter_counts['B'] -= set_frequency
        price += (sku_prices[letter]['price'] * count)

    for letter, count in letter_counts.items():
        if letter in special_offers:
            set_amount = special_offers[letter]['amount']
            set_frequency, count = divmod(count, set_amount)
            price += (special_offers[letter]['offer_price'] * set_frequency)

        price += (sku_prices[letter]['price'] * count)

    return price




