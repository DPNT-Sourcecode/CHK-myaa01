
from collections import Counter
# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    sku_prices = {
        'A': 50,
        'B': 30,
        'C': 20,
        'D': 15,
        'E': 40,
    }
    special_offers = {
        'B': {
            'amount': 2,
            'offer_price': 45
        }
    }
    if not all(sku in sku_prices for sku in skus):
        return -1

    if len(skus) == 0:
        return 0

    letter_counts = Counter(skus)
    price = 0

    count_E = letter_counts.pop('E')
    set_frequency, count_E = divmod(count_E, 2)
    while letter_counts['B'] > 0 and set_frequency > 0:
        letter_counts['B'] -= 1
    price += (sku_prices['E'] * count_E)

    count_A = letter_counts.pop('A')
    set_frequency, count_A = divmod(count_A, 5)
    price += (200 * set_frequency)
    set_frequency, count_A = divmod(count_A, 3)
    price += (130 * set_frequency)
    price += (sku_prices['A'] * count_A)

    for letter, count in letter_counts.items():
        if letter in special_offers:
            set_amount = special_offers[letter]['amount']
            set_frequency, count = divmod(count, set_amount)
            price += (special_offers[letter]['offer_price'] * set_frequency)

        price += (sku_prices[letter] * count)

    return price

